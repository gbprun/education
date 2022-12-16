# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from math import sqrt

Ax = int(input("Укажите x для точки А: "))
Ay = int(input("Укажите y для точки А: "))
Bx = int(input("Укажите x для точки B: "))
By = int(input("Укажите y для точки B: "))

distance = sqrt( ((Bx - Ax)**2) + ((By - Ay)**2) )
print(f"A ({Ax},{Ay}); B ({Bx},{By}) -> {round(distance, 3)}")