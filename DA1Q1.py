
# DA1 Q1
# Mihir Gupta
# 19BC0619

text_file = open("./MyTextFile.txt", "r")
input_file = text_file.read()
text_file.close()

stop_words = [
    ".",
    ",",
    "a",
    "they",
    "the",
    "his",
    "so",
    "and",
    "were",
    "from",
    "that",
    "of",
    "in",
    "only",
    "with",
    "to",
]

input_split = input_file.split()
filtered_list = []
for word in input_split:
    if word not in stop_words:
        filtered_list.append(word)
print(filtered_list)
