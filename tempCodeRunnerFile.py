with open(r"C:\Users\dell\Downloads\input_1.txt", "r") as file:
    data = file.read()
print(data)

# Cleaning the data.
# Removing the Punctuation
import string
removed_punctuation = data.translate(str.maketrans('', '', string.punctuation))
print(removed_punctuation)

# Removinng whitespaces \n \t \s
removed_whitespaces = " ".join(data.split())
print(removed_whitespaces)