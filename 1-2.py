# С Ботом

from random import randint
def input_dat(name):
    x = int(input(f"{name}, сколько конфет заберете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x
def p_print(name, k, counter, amount):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {amount} конфет.")
def bot_calc(amount):
    k = randint(1,29)
    while amount-k <= 28 and amount > 29:
        k = randint(1,29)
    return k
p1 = input("Введите имя первого игрока: ")
p2 = "Bot"
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
        k = bot_calc(amount)
        counter2 += k
        amount -= k
        move = True
        p_print(p2, k, counter2, amount)
if move:
    print(f"Выиграл {p1}")
else:
    print(f"Выиграл {p2}")
