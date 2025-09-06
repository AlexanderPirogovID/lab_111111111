num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
num3 = int(input("Введите третье целое число: "))
if num1 <= num2 and num1 <= num3:
    min_num = num1
elif num2 <= num1 and num2 <= num3:
    min_num = num2
else:
    min_num = num3
print(f"Наименьшее число: {min_num}")