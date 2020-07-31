pos1 = int(input())
pos2 = int(input())

result_3 = (pos1 == 1 == pos2) or (pos1 == 8 == pos2) or (pos1 == 8 and pos2 == 1) or (pos1 == 1 and pos2 == 8)
result_5 = (pos2 == 1 < pos1 < 8) or (pos1 == 8 > pos2 > 1) or (pos1 == 1 < pos2 < 8) or (pos2 == 8 > pos1 > 1)
if result_3:
    print(3)
elif result_5:
    print(5)
else:
    print(8)
