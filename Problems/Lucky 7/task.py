n = int(input())  # number of lines to come
for _i in range(n):
    number = int(input())
    if number % 7 == 0:
        print(number ** 2)
