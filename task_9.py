import random

nums = [random.randint(-10, 10) for _ in range(15)]
positives = [x for x in nums if x > 0]
squares = [x**2 for x in nums]

print("Исходный список:", nums)
print("Положительные числа:", positives)
print("Квадраты чисел:", squares)