# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти

quarter = int(input("Укажите координатную четверть: "))

# Проверка на корректность введенной четверти
if quarter < 1 or quarter > 4:
    print("Четверть должна быть от 1 до 4")
elif quarter == 1:
    print(f"x от 0 до +∞")
    print(f"y от 0 до +∞")
elif quarter == 2:
    print(f"x от 0 до -∞")
    print(f"y от 0 до +∞")
elif quarter == 3:
    print(f"x от 0 до -∞")
    print(f"y от 0 до -∞")
elif quarter == 4:
    print(f"x от 0 до +∞")
    print(f"y от 0 до -∞")