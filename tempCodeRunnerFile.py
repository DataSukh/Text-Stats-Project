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