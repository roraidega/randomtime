"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""

import time
def time_1():
    xod = 30 * 60
    Vash_hod = 0
    while Vash_hod != 'off':
        if xod > 0:
            start = time.time()
            Vash_hod = input('Ваш ход - ')
            end = time.time()
            xod = xod - (end - start)
            print('Осталось', round(xod / 60))
        else:
            print('Время закончилось')
            break
    return xod / 60

xod = time_1()


print('Оставшееся время в конце игры -', round(xod))