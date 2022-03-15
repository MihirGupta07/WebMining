
# DA1 Q3
# Mihir Gupta
# 19BC0619

# Importing NLTK
from nltk.tokenize import word_tokenize, LineTokenizer

# Tokenizing a Line
para = "Web mining is the application of data mining techniques to discover patterns from the World Wide Web"
word_tokens = word_tokenize(para)
print("Tokenizing a line:")
print(word_tokens)
print()

# Tokenizing multiple lines
file = open("MyTextFile.txt", "r")
para = file.read()
word_tokens = word_tokenize(para)
print("Tokenizing multiple lines:")
print(word_tokens)
print()

# Tokenizing a WebPage(Line by line)
file = open("MyHTMLFile.html", "r")
para = file.read()
word_tokens = LineTokenizer().tokenize(para)
print("Tokenizing a WebPage:")
print(word_tokens)
print()
