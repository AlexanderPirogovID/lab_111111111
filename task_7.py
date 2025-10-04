import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
def is_positive(number):
    return number > 0
r = 5
print("Площадь круга с радиусом", r, ":", calculate_circle_area(r))
n = -3
print(n, "положительное?", is_positive(n))
