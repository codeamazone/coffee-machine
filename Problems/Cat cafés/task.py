cafes = []
no_of_cats = []
while True:
    cafe = input()
    if cafe == 'MEOW':
        break
    split_name = cafe.split()
    cafes.append(split_name[0])
    no_of_cats.append(int(split_name[1]))
    result = no_of_cats.index(max(no_of_cats))
print(cafes[result])
