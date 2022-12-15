# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
    
#    *Примеры:*    
#    - 5, 25 -> да
#    - 4, 16 -> да
#    - 25, 5 -> да
#    - 8, 9 -> нет

def check_square(a, b):
    return True if a * a == b or b * b == a else False


a = int(input("Ввеидите 1-е число: "))
b = int(input("Ввеидите 1-е число: "))

result = check_square(a, b)
print("Да" if result else "Нет")
