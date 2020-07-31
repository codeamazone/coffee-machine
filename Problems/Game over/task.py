scores = input().split()
correct = 0
incorrect = 0
for char in scores:
    if incorrect == 3:
        print('Game over')
        print(correct)
        break
    if char == 'I':
        incorrect += 1
    if char == 'C':
        correct += 1
else:
    print('You won')
    print(correct)
