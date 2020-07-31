phrase = input()
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
for character in phrase:
    if character not in vowels and character not in consonants:
        break
    if character in vowels:
        print('vowel')
    elif character in consonants:
        print('consonant')
