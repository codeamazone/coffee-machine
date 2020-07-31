index = input()
if float(index) < 2:
    print('Analytic')
elif 2 <= float(index) <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
