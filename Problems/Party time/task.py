names_list = []
while True:
    name = input()
    if name == '.':
        print(names_list)
        print(len(names_list))
        break
    names_list.append(name)
