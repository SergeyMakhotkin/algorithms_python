# нужно хранить дефолтные значения консольных аргументов, анализировать, ввел ли пользователь при запуске аргументы,
# использовать введенные параметры

from collections import ChainMap
import argparse  # для работы с ключами в командной строке

defaults_args = {'ipaddress': 'localhost', 'port': 7777}

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ipaddress')
parser.add_argument('-p', '--port')

args = parser.parse_args()
input_args = {key: value for key, value in vars(args).items() if value}
# vars возвращает словарь атрибут:значение  - определенные аргументы add_argument и значения


settings = ChainMap(input_args, defaults_args)
print(settings['ipaddress'])
print(settings['port'])
