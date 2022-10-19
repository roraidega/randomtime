"""
Во время хоккейных матчей на игроков может накладываться дисциплинарный штраф — удаление с поля на 2 или 10 минут.
Программа должна:
1) Спрашивать «Удалить с поля?» и запрашивать количество минут штрафа.
2) Печатать сообщение: «Вы удалена с поля на _ минут(-ы)» и ставить паузу в работе на это время.
3) Спустя 2 или 10 минут печатать новое сообщение: «Возвращайтесь на поле!»
Дабы не ждать 2 и 10 минут сделайте 2 и 10 секунд.
"""
import time
while True:
    timeflag = input('Удалить с поля?(да/нет)')
    if timeflag == 'нет':
        break
    elif timeflag == 'да':
        timeout = int(input('Введите кол-во минут: '))
        print('Вы удалены с поля на', str(timeout), 'минут(ы)')
        time.sleep(timeout)
        print('Вернитесь на поле!')
    else:
        print('Попробуйте еще раз')