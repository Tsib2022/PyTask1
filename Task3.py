print("Введите шестизначное число")
num = int(input())
summ1 = 0
summ2 = 0
while num > 999:
    x = num%10
    summ1 = summ1 + x 
    num = num//10
# print(summ1)
while num > 0:
    x2=num%10
    summ2 = summ2+x2
    num=num//10
# print(summ2)
if summ1 == summ2: print("Yes")
else: print("No")
