# пример класса для хранения координат точки на плоскости

class Point:
    color = 'red'
    circle = 2


Point.color = 'black'
print(Point.circle)

# увидеть все атрибуты класса
print(Point.__dict__)


# создание экземпляра класса
a = Point()
b = Point()

# type() - отобразить тип переменной
print(type(a))

# проверка типа сравнением
type(a) == Point
isinstance(a, Point)

# Динамическое добавление нового свойства.
Point.type_pt = 'disc'
setattr(Point, 'prop', 1)

# Удаление атрибута из класса
del Point.color
delattr(Point, 'prop')
print(Point.__dict__)


# Проврека существования аттрибута класса
hasattr(Point, 'prop') # возвращает true \ false
