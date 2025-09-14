# Read the entire file into a variable called 'data'
with open(r"C:\Users\dell\Downloads\input_1.txt", "r") as file:
    data = file.read()
print(data)

# Cleaning the data.
data = data.replace("didn't", "did not").replace("you'd", "you would")
# Removing the Punctuation
import string
removed_punctuation = data.translate(str.maketrans('', '', string.punctuation))
print(removed_punctuation)

# Removinng whitespaces \n \t \s and lowering the data
normalization = " ".join(removed_punctuation.split()).lower()
print(normalization)

# Tokenization
tokenized_data = normalization.split()
print(tokenized_data)

# Statistics
word_count = len(tokenized_data)
char_count = len(normalization)
unique_words = len(set(tokenized_data)) 
avg_word_length = sum(len(word) for word in tokenized_data) / word_count
most_common = max(set(tokenized_data), key=tokenized_data.count)
count = tokenized_data.count(most_common)

# Output
output = (
    f"Word count: {word_count}\n"
    f"Unique words: {unique_words}\n"
    f"Characters (with spaces): {len(normalization)}\n"
    f"Characters (no spaces): {len(removed_punctuation.replace(' ',''))}\n"
    f"Average word length: {avg_word_length:.2f}\n"
    f"Most common word(s): {most_common} ({count})\n"
)

print(output)
