# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота

from random import randint
def input_dat(name):
    x = int(input(f"{name}, сколько конфет заберете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x
def p_print(name, k, counter, amount):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {amount} конфет.")
p1 = input("Имя первого игрока: ")
p2 = input("Имя второго игрока: ")
amount = 117
move = randint(0,2)
if move:
    print(f"Первый ходит {p1}")
else:
    print(f"Первый ходит {p2}")
counter1 = 0 
counter2 = 0
while amount > 28:
    if move:
        k = input_dat(p1)
        counter1 += k
        amount -= k
        move = False
        p_print(p1, k, counter1, amount)
    else:
        k = input_dat(p2)
        counter2 += k
        amount -= k
        move = True
        p_print(p2, k, counter2, amount)
if move:
    print(f"Выиграл {p1}")
else:
    print(f"Выиграл {p2}")
