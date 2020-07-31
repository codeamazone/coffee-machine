# put your python code here
a = int(input())
b = int(input())
counter = 0
result = 0

for x in range(a, b + 1):
    if (x % 3) == 0:
        result += x
        counter += 1

print(result / counter)
