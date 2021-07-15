#coding=utf-8

x = int(input("Введите число N:"))
print("Квадраты натуральных чисел от 1 до N:")
for i in range(1, x + 1):
    print(i ** 2, end=" ")
