# Задача 2: Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 

print("Задача 2: Найдите сумму цифр трехзначного числа.")
a = int(input("Введите число: "))

if 99<a<1000:
    b=a%10
    c=(a%100)//10
    d=a//100
    sum=b+c+d
    print(sum)
else:
     print('Введите трехзначное число')
    
#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
#Вместе они сделали S журавликов. Сколько журавликов сделал каждый 
#ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#*Пример:*

#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

print("Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?")
a = int(input("Введите число журавликов: "))

if a%6==0:
    petya=a/6
    katya=petya*4
    print('Петя и Сережа =', petya,"Катя =", katya)
else:
     print("некорректное число")


#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
#за проезд и получали билет с номером. Счастливым билетом называют такой билет 
#с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая 
#проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no

print("Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались  за проезд и получали билет с номером. Счастливым билетом называют такой билет  с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. ")
bilet = int(input("Введите номер билета: "))

if 99999<bilet<1000000:
    number1=bilet%1000
    a1= number1%10
    b1=(number1%100)//10
    c1=number1//100
    sum1=a1+b1+c1
    number2=bilet//1000
    a2= number2%10
    b2=(number2%100)//10
    c2=number2//100
    sum2=a2+b2+c2
    if sum1==sum2:
        print('Счастливый)')
    else:
        print('Не очень счастливый')
else:
     print('Неверный номерок')
     
     
#Задача 8: Требуется определить, можно ли от шоколадки размером n ? m долек 
#отломить k долек, если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no
print("Задача 8: Требуется определить, можно ли от шоколадки размером n ? m долек  отломить k долек, если разрешается сделать один разлом по прямой между дольками  (то есть разломить шоколадку на два прямоугольника).")
n = int(input("Введите n "))
m = int(input("Введите m "))
k = int(input("Сколько долек отломить? "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да сможем отломить')
else:
    print('Невозможно отломить')