word = input()
half = int(len(word) / 2)
half1 = word[0:half]
half2 = word[half:len(word)]
half2_reversed = ''
index = len(half2)
while index > 0:
    half2_reversed += half2[index - 1]
    index -= 1
if half1 == half2_reversed:
    print('Palindrome')
else:
    print('Not palindrome')
