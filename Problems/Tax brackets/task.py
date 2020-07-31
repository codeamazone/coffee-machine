income = int(input())
if income in range(0, 15528):
    percent = 0
elif income in range(15528, 42708):
    percent = 15
elif income in range(42708, 132407):
    percent = 25
else:
    percent = 28
result = income * percent / 100
print(f'The tax for {income} is {percent}%. That is {result:.0f} dollars!')
