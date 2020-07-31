phrase = input()
for char in phrase:
    if char.isupper():
        phrase = phrase.replace(char, '_' + char.lower())
print(phrase)
