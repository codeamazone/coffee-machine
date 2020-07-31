_sum = 0
result = 0
while True:
    number = int(input())
    _sum += number
    result += (number ** 2)
    if _sum == 0:
        print(result)
        break
