score = int(input())
maximum = int(input())
result = (score / maximum) * 100

if result < 60:
    print('F')
elif 60 <= result < 70:
    print('D')
elif 70 <= result < 80:
    print('C')
elif 80 <= result < 90:
    print('B')
else:
    print('A')
