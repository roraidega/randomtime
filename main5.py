"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
import random
import time
while True:
    print('Подбрасываем кубики')
    Kub_1 = random.randint(1, 6)
    Kub_2 = random.randint(1, 6)
    Kub_3 = Kub_2 + Kub_1
    time.sleep(2)
    print('Кубик 1 -', Kub_1)
    print('Кубик 2 -', Kub_2)
    print('Общаая сумма кубиков -', Kub_3)
    time.sleep(1)