recommended = int(input())
limit = int(input())
actual_sleep = int(input())

if actual_sleep < recommended:
    print('Deficiency')
elif actual_sleep <= limit:
    print('Normal')
elif actual_sleep > limit:
    print('Excess')
