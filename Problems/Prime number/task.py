number = int(input())
if number >= 1:
    if number == 1:
        print('This number is not prime')
    elif number == 2:
        print('This number is prime')
    else:
        for _i in range(2, number):
            result = number % _i
            if result == 0:
                print('This number is not prime')
                break
        else:
            print('This number is prime')
