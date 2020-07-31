chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
money = int(input())

if money < chicken:
    print('None')
elif money < goat:
    if money < 2 * chicken:
        print('1 chicken')
    else:
        print((money // chicken), 'chickens')
elif money < pig:
    if money < 2 * goat:
        print('1 goat')
    else:
        print((money // goat), 'goats')
elif money < cow:
    if money < 2 * pig:
        print('1 pig')
    else:
        print((money // pig), 'pigs')
elif money < sheep:
    if money < 2 * cow:
        print('1 cow')
    else:
        print((money // cow), 'cows')
else:
    print((money // sheep), 'sheep')
