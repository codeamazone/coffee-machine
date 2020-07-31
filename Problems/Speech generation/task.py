digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
phone_number = input()
for digit in phone_number:  # '0123456789'
    print(digits[int(digit)])
