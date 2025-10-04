while True:
    user_input = input("Введите число или 'стоп': ")
    if user_input.lower() == "стоп":
        break
    try:
        num = float(user_input)
        print("Вы ввели число:", num)
    except ValueError:
        print("Ошибка: введите число или 'стоп'.")