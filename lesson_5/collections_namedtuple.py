from collections import namedtuple

object_name = namedtuple('object_name', 'key_1, key_2, key_3')  # по сути, создание класса object_name
# object_name = namedtuple('object_name', 'key_1 key_2 key_3')
# дополнительный параметр rename=True
# переименует недопустимые параметры
# (в номер позиции)
# параметры можно передавать в виде списка

# test = object_name(1, 'sdfsdf', (4, 6, 7))
#
# print(test.key_1)
# print(test.key_2)
# print(test.key_3)

# методы namedtuple
# ._make(iterable) - создание экземпляра с параметрами, переданными в iterable
# ._asdict() - преобразование в OrderedDict
# ._replaced(**kwargs) - изменить элемент в namedtuple p2._replaced(x=7)
# ._fields - возвращает кортеж с именами полей
# p._fields            # view the field names ('x', 'y')

# Color = namedtuple('Color', 'red green blue')
# Pixel = namedtuple('Pixel', Point._fields + Color._fields)
# Pixel(11, 22, 128, 255, 0)  # Pixel(x=11, y=22, red=128, green=255, blue=0)

# с версии 3.7 есть возможность добалять значение по умолчанию
new_point = namedtuple('new_point', 'x, y, z', defaults=[0, 0])
p5 = new_point(45)
print(p5)
print(p5._fields_defaults)
# ._fields_default - возвращает значения по умолчанию


dct = {'x': 1, 'y': 3, 'z': 34}
p6 = new_point(**dct)  # преобразование 'a': 123 -> a=123
print(p6)