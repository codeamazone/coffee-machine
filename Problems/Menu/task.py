pizza = 'Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy'
salad = 'Caesar salad, Green salad, Tuna salad, Fruit salad'
soup = 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'
order = input()
available_food = ['pizza', 'salad', 'soup']

if order not in available_food:
    print('Sorry, we don\'t have it in the menu')
elif order == 'pizza':
    print(pizza)
elif order == 'salad':
    print(salad)
elif order == 'soup':
    print(soup)
