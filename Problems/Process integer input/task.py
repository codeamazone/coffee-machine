number = int
while number:
    number = int(input())
    if number < 10:
        continue
    elif number > 100:
        break
    print(number)
