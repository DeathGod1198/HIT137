import pandas as pd
import os
import zipfile
import re

# Specifying path to the zipped folder containing CSV files
folder_path = 'Assignment 2.zip'

# Extracting all CSV files from the folder
with zipfile.ZipFile(folder_path, 'r') as zip_ref:
    zip_ref.extractall('extracted_folder')

# Creating a dictionary to identify columns I want to copy from the file
column_mapping = {
    'CSV1.csv': 'SHORT-TEXT',
    'CSV2.csv': 'TEXT',
    'CSV3.csv': 'TEXT',
    'CSV4.csv': 'TEXT'
}

# Creating a list to store text from all CSV files
combine_texts = []

# Looping through CSV files in extracted folder
for filename, column_name in column_mapping.items():
    file_path = os.path.join('extracted_folder', filename)
    
    # Reading CSV files using pandas
    df = pd.read_csv(file_path)
    
    # Extracting texts from specified columns
    texts = df[column_name].tolist()
    
    # Copying texts to the list
    combine_texts.extend(texts)

# Joining all texts in a single string
combine_texts_final = '\n'.join(combine_texts)

# Defining function to remove numbers and symbols and converting texts to lowercase for tokenizer efficiency
def clean_and_lower(text):
    
    # Removing symbols and integers using regex and converting to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    return cleaned_text

# Cleaning and converting the combined texts to lowercase"
combine_texts_cleaned = clean_and_lower(combine_texts_final)

# Writing the cleaned text to a new .txt file
cleaned_output_file_path = 'cleaned_output_text.txt'
with open(cleaned_output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combine_texts_cleaned)

print(f'Cleaned and lowercase text extracted and stored in {cleaned_output_file_path}')