import csv
from collections import Counter
from transformers import AutoTokenizer
from tqdm import tqdm

file_path = 'cleaned_output_text.txt'
model_name = 'bert-base-uncased'  
output_csv = 'Bert_tokenizer_Top30_Results.csv'  

def count_and_get_top_words(file_path, model_name, output_csv, max_chunk_length=512, overlap=50, top_n=30):
    
    # Loading tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Reading the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Splitting text into small parts
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length - overlap)]

    # Initializing counter for token counts
    total_token_counts = Counter()

    # Tokenizing each chunk and updating the counter
    for chunk in tqdm(chunks, desc="Tokenizing", unit="chunk"):
        
        # Using encode_plus for tokenization
        encoding = tokenizer.encode_plus(
            text=chunk,
            add_special_tokens=False,
            return_tensors='pt',
            truncation=True
        )
        
        # Extracting tokens from the tensor
        tokens = tokenizer.convert_ids_to_tokens(encoding['input_ids'][0].tolist())
        total_token_counts.update(tokens)

    # Getting the top N tokens
    top_tokens = total_token_counts.most_common(top_n)

    # Saving results to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Token', 'Count'])
        csv_writer.writerows(top_tokens)


count_and_get_top_words(file_path, model_name, output_csv)
print(f'Results saved')