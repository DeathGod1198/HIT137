from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import csv
from collections import Counter
from tqdm import tqdm
import warnings

# Suppressing warnings
warnings.filterwarnings("ignore")

# Loading BioBERT model and tokenizer
model_name = "dmis-lab/biobert-base-cased-v1.2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Path to the cleaned text file
cleaned_text_file_path = 'cleaned_output_text_small.txt'

# Chunking size for processing data
max_length = 512  # Maximum tokens for BioBERT input

# Reading the text from the cleaned text file
with open(cleaned_text_file_path, 'r', encoding='utf-8') as text_file:
    input_text = text_file.read()

# Tokenizing and process the input text
tokens = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=max_length, add_special_tokens=True)

# Tokenized input split into chunks for BERT processing
token_ids = tokens['input_ids'][0]  # Access the first batch of tokenized input
attention_mask = tokens['attention_mask'][0]

# Spliting tokenized input into smaller chunks that the model can handle (max 512 tokens per chunk)
chunks = [token_ids[i:i + max_length] for i in range(0, len(token_ids), max_length)]
masks = [attention_mask[i:i + max_length] for i in range(0, len(attention_mask), max_length)]
total_chunks = len(chunks)

entities = []

# Processing the chunks
with tqdm(total=total_chunks, desc="Processing Chunks") as pbar:
    for chunk, mask in zip(chunks, masks):
        # Convert token IDs back to input format for the model
        inputs = {'input_ids': chunk.unsqueeze(0), 'attention_mask': mask.unsqueeze(0)}

        # Forwarding pass through the model
        with torch.no_grad():
            outputs = model(**inputs)

        # Get predicted labels (logits -> labels)
        predictions = torch.argmax(outputs.logits, dim=2)

        # Extract predicted tokens and their corresponding labels
        predicted_labels = predictions.squeeze().tolist()
        tokens_in_chunk = tokenizer.convert_ids_to_tokens(chunk.tolist())

        current_entity = ""
        for token, label_id in zip(tokens_in_chunk, predicted_labels):
            label_str = model.config.id2label[label_id]

            # Ignore special tokens like [CLS] and [SEP]
            if token in ['[CLS]', '[SEP]']:
                continue

            if label_str.startswith("B-"):  # Beginning of a new entity
                if current_entity:
                    entities.append(current_entity.strip())
                current_entity = token.replace("##", "") + " "  # Start new entity
            elif label_str.startswith("I-"):  # Inside an entity
                current_entity += token.replace("##", "") + " "
            else:
                if current_entity:  # End the entity
                    entities.append(current_entity.strip())
                    current_entity = ""

        if current_entity:  # Catch any entity not yet added
            entities.append(current_entity.strip())

        pbar.update(1)

# Count the occurrences of each entity
entity_counts = Counter(entities)

# Save results to a CSV file
csv_file_path = 'bio_entities_debug.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Entity', 'Count'])

    for entity, count in entity_counts.items():
        csv_writer.writerow([entity, count])

print(f'Results saved to {csv_file_path}')