class Coffeemachine:
    water_for_espresso = 250
    beans_for_espresso = 16
    water_for_latte = 350
    milk_for_latte = 75
    beans_for_latte = 20
    water_for_cappuccino = 200
    milk_for_cappuccino = 100
    beans_for_cappuccino = 12
    main_menu_statement = 'Write action (buy, fill, take, remaining, exit): '

    def __init__(self):
        self.available_water = 400
        self.available_milk = 540
        self.available_beans = 120
        self.available_cups = 9
        self.available_cash = 550
        self.state = 'main_menu'

    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.available_water} of water')
        print(f'{self.available_milk} of milk')
        print(f'{self.available_beans} of coffee beans')
        print(f'{self.available_cups} of disposable cups')
        print(f'${self.available_cash} of money')
        print(self.main_menu_statement)

    def take(self):
        print(f'I gave you $ {self.available_cash}')
        self.available_cash -= self.available_cash
        print(self.main_menu_statement)

    def espresso(self):
        if self.available_water >= self.water_for_espresso and self.available_beans >= self.beans_for_espresso and self.available_cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.available_water -= self.water_for_espresso
            self.available_beans -= self.beans_for_espresso
            self.available_cups -= 1
            self.available_cash += 4
        elif self.available_water < self.water_for_espresso:
            print('Sorry, not enough water!')
        elif self.available_beans < self.beans_for_espresso:
            print('Sorry, not enough coffee beans!')
        elif self.available_cups < 0:
            print('Sorry, not enough disposable cups!')

    def latte(self):
        if self.available_water >= self.water_for_latte and self.available_milk >= self.milk_for_latte and self.available_beans >= self.beans_for_latte and self.available_cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.available_water -= self.water_for_latte
            self.available_milk -= self.milk_for_latte
            self.available_beans -= self.beans_for_latte
            self.available_cash += 7
            self.available_cups -= 1
        elif self.available_water < self.water_for_latte:
            print('Sorry, not enough water!')
        elif self.available_milk < self.milk_for_latte:
            print('Sorry, not enough milk!')
        elif self.available_beans < self.beans_for_latte:
            print('Sorry, not enough coffee beans!')
        elif self.available_cups < 1:
            print('Sorry, not enough disposable cups!')

    def cappuccino(self):
        if self.available_water >= self.water_for_cappuccino and self.available_milk >= self.milk_for_cappuccino and self.available_beans >= self.beans_for_cappuccino and self.available_cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.available_water -= self.water_for_cappuccino
            self.available_milk -= self.milk_for_cappuccino
            self.available_beans -= self.beans_for_cappuccino
            self.available_cash += 6
            self.available_cups -= 1
        elif self.available_water < self.water_for_cappuccino:
            print('Sorry, not enough water!')
        elif self.available_milk < self.milk_for_cappuccino:
            print('Sorry, not enough milk!')
        elif self.available_beans < self.beans_for_cappuccino:
            print('Sorry, not enough coffee beans!')
        elif self.available_cups < 1:
            print('Sorry, not enough disposable cups!')

    def load_main_menu(self):
        self.state = 'main_menu'
        print(self.main_menu_statement)

    def interpret_input(self, action):
        if self.state == 'main_menu':
            if action == 'remaining':
                coffee_machine.remaining()
            elif action == 'take':
                coffee_machine.take()
            elif action == 'buy':
                self.state = 'select_coffee'
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            elif action == 'fill':
                self.state = 'refill_water'
                print('Write how many ml of water do you want to add: ')
        elif self.state == 'select_coffee':
            if action == '1':
                coffee_machine.espresso()
                coffee_machine.load_main_menu()
            elif action == '2':
                coffee_machine.latte()
                coffee_machine.load_main_menu()
            elif action == '3':
                coffee_machine.cappuccino()
                coffee_machine.load_main_menu()
            elif action == 'back':
                coffee_machine.load_main_menu()
        elif self.state == 'refill_water':
            self.available_water += int(action)
            self.state = 'refill_milk'
            print('Write how many ml of milk do you want to add:')
        elif self.state == 'refill_milk':
            self.available_milk += int(action)
            self.state = 'refill_beans'
            print('Write how many grams of coffee beans do you want to add:')
        elif self.state == 'refill_beans':
            self.available_beans += int(action)
            self.state = 'refill_cups'
            print('Write how many disposable cups of coffee do you want to add:')
        elif self.state == 'refill_cups':
            self.available_cups += int(action)
            coffee_machine.load_main_menu()


coffee_machine = Coffeemachine()

print('Write action (buy, fill, take, remaining, exit): ')
while True:
    user_input = input()
    if user_input == 'exit':
        break
    else:
        coffee_machine.interpret_input(user_input)
