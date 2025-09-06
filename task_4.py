s=int(input("Введите начальное число"))
e=int(input("Введите конечное число"))
m=0
for i in range(s,e+1):
    if i%2==0: print(i)
    m+=1
if m==0: print("В этом диапазоне четных чисел нет")