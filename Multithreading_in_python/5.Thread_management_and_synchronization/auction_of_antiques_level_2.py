import time
from queue import Empty, Queue, LifoQueue, PriorityQueue, Full
from threading import Thread, Lock, RLock, Event

from time import sleep

import os
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock

import random


# События для старта аукциона
auction_start_painting = Event()
auction_start_clock = Event()

# Функция, представляющая участника аукциона
def bidder(name):
    print(f'Участник {name} готов к аукциону за картину.')
    print(f'Участник {name} готов к аукциону за антикварные часы.')
    if not auction_start_clock.is_set() and not auction_start_painting.is_set():
        auction_start_clock.wait()
        auction_start_painting.wait()
        print(f'Участник {name} делает ставку на редкую картину.')
        print(f'Участник {name} делает ставку на антикварные часы.')


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

    sleep(3)
    print('Аукцион за картину начинается!')
    print('Аукцион за антикварные часы начинается!')
    auction_start_clock.set()
    auction_start_painting.set()

    for thread in threads:
        thread.join()

    print('Аукцион за картину завершился!')
    print('Аукцион за антикварные часы завершился!')
    winner_clock = random.choice(bidder_names)
    winner_painting = random.choice(bidder_names)
    print(f'Победитель аукциона за антикварные часы: {winner_clock}')
    print(f'Победитель аукциона за редкую картину: {winner_painting}')

main()
