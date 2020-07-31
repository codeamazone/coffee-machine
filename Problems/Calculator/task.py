# put your python code here
number1 = float(input())
number2 = float(input())
operation = input()

if number2 == 0 and operation in ['/', 'div', 'mod']:
    print('Division by 0!')
elif operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '/':
    print(number1 / number2)
elif operation == '*':
    print(number1 * number2)
elif operation == 'mod':
    print(number1 % number2)
elif operation == 'pow':
    print(number1 ** number2)
elif operation == 'div':
    print(number1 // number2)
