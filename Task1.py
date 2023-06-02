# Найдите сумму цифр трехзначного числа.
num = int(input("Введите трехзначное число  "))
summ = 0
while num > 0:
    x = num%10
    summ = summ + x 
    num = num//10
print("Сумма цифр трехзначного числа =", summ)
