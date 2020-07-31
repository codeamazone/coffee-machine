class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = 0.5 * (self.a * self.b)  # calculate the area here


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]
right_triangle = RightTriangle(input_c, input_a, input_b)
if right_triangle.c ** 2 == right_triangle.a ** 2 + right_triangle.b ** 2:
    print(right_triangle.area)
else:
    print('Not right')
