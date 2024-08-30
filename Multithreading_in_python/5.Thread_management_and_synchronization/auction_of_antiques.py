import time
from queue import Empty, Queue, LifoQueue, PriorityQueue, Full
from threading import Thread, Lock, RLock, Event

from time import sleep

import os
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock


# Событие для старта аукциона
auction_start = Event()

# Функция, представляющая участника аукциона
def bidder(name):
    print(f'Участник {name} готов к аукциону.')
    if not auction_start.is_set():
        auction_start.wait()
    print(f'Участник {name} делает ставку на редкую картину.')


# Имена участников аукциона
bidder_names = ['Сергей', 'Борис', 'Виктор', 'Евдоким', 'Егор']

# Создание потоков-участников и запуск потоков
def main():
    threads = []
    for bidder_name in bidder_names:
        thread = Thread(target=bidder,
                        args=(bidder_name,))
        thread.start()
        threads.append(thread)

    print('Аукцион начинается!')
    auction_start.set()

    for thread in threads:
        thread.join()

main()
