from collections import Counter

with open('cleaned_output_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

#Counting words
word_counts = Counter(text.split())

# Getting top 30 common words
top_30_words = word_counts.most_common(30)

# Storing top 30 words and their counts into CSV file
import csv

with open('top_30_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Word', 'Count'])
    csv_writer.writerows(top_30_words)