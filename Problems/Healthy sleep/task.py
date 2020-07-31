recommended = int(input())
limit = int(input())
actual_sleep = int(input())

if actual_sleep < recommended:
    print('Deficiency')
else:
    if actual_sleep <= limit:
        print('Normal')
    if actual_sleep > limit:
        print('Excess')
