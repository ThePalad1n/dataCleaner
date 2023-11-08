
# load text
filename = 'chapter1.txt'
file = open(filename, 'r', encoding="utf-8")
text = file.read()
file.close()



import re
words = re.split(r'\W+', text)
print(words[:100])