import os
import re
import time  # Import the time module
from collections import Counter
import socket

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def count_words(text):
    text = text.lower()
    words = text.split()
    return len(words), Counter(words)

# Dictionary of contractions
contractions = {
    "I'm": "I am",
    "It's": "It is",
    "I'll": "I will",
    "you're": "you are",
    "You're": "You are",
    "can't": "can not",
    "couldn't": "could not",
    "don't": "do not",
    "won't": "will not",
    "that's": "thats is",
    "don’t": "do not",
    "that’s": "that is",
    "build ’em": "build them",
    "you’ve": "you have",
    "you’ll": "you will"
}
# Function to handle contractions
def handle_contractions_new(text):
    pattern = re.compile(r'\b(' + '|'.join(contractions.keys()) + r')\b')
    return pattern.sub(lambda x: contractions[x.group()], text)

def handle_contractions(text):
    text = text.replace("—", " ")
    text = handle_contractions_new(text)
    return text

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Paths to text files
file1_path = '/home/data/IF.txt'
file2_path = '/home/data/AlwaysRememberUsThisWay.txt'

# Read and process the text files
file1_text = read_file(file1_path)
file2_text = read_file(file2_path)

# contraction handling for AlwaysRememberUsThisWay file only
file1_word_count, file1_word_freq = count_words(file1_text)
expanded_text = handle_contractions_new(file2_text)
file2_word_count, file2_word_freq = count_words(expanded_text)

total_word_count = file1_word_count + file2_word_count

# Get the top 3 words for each file
file1_top_words = file1_word_freq.most_common(3)
file2_top_words = file2_word_freq.most_common(3)

# contraction handling for both files
expanded_text1_contraction = handle_contractions(file1_text)
expanded_text2_contraction = handle_contractions_new(file2_text)
file1_word_count_contraction, file1_word_freq_contraction = count_words(expanded_text1_contraction)
file2_word_count_contraction, file2_word_freq_contraction = count_words(expanded_text2_contraction)

total_word_count_contraction = file1_word_count_contraction + file2_word_count_contraction

# Get the top 3 words for each file
file1_top_words_contraction = file1_word_freq_contraction.most_common(3)
file2_top_words_contraction = file2_word_freq_contraction.most_common(3)

# Get the IP address
ip_address = get_ip_address()

# Write the results to the output file
result_path = '/home/data/output/result.txt'
os.makedirs('/home/data/output', exist_ok=True)

with open(result_path, 'w') as result_file:
    result_file.write(f"Container IP Address: {ip_address}\n")
    
    result_file.write(f"IF.txt Word Count (without contractions): {file1_word_count}\n")
    result_file.write(f"IF.txt Word Count(Contractions Handled): {file1_word_count_contraction}\n")
    result_file.write(f"AlwaysRememberUsThisWay.txt Word Count(Contractions Handled): {file2_word_count_contraction}\n")
    result_file.write(f"AlwaysRememberUsThisWay.txt Word Count(Contractions Handled): {file2_word_count}\n")
    result_file.write(f"Total Word Count (without contractions): {total_word_count}\n")
    result_file.write(f"Total Word Count: {total_word_count_contraction}\n")
    result_file.write(f"Top 3 Words in IF.txt (without contractions): {file1_top_words}\n")
    result_file.write(f"Top 3 Words in IF.txt: {file1_top_words_contraction}\n")
    result_file.write(f"Top 3 Words in AlwaysRememberUsThisWay.txt (without contractions): {file2_top_words}\n")
    result_file.write(f"Top 3 Words in AlwaysRememberUsThisWay.txt: {file2_top_words_contraction}\n")
    
    

    
    
    
    

# Print the results
with open(result_path, 'r') as file:
    print(file.read())