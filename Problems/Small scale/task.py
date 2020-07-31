numbers = []
number = input()
while number:
    if number == ".":
        break
    numbers.append(float(number))
    number = input()
print(min(numbers))
