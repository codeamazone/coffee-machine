numbers = []
while True:
    number = input()
    if number == '.':
        break
    numbers.append(int(number))
print(sum(numbers) / len(numbers))
