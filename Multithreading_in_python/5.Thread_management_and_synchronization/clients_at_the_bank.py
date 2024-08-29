import time
from queue import Empty, Queue, LifoQueue, PriorityQueue, Full
from threading import Thread, Lock, RLock, Event

from time import sleep

import os
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock


clients = ['Виктор', 'Ирина', 'Андрей']


def simulate_client_behavior(client_name, event):
    print(f'{client_name} вошел в банк')
    if not event.is_set():
        simulate_cashier_work(client_name, event)
        event.wait() 
        print(f'{client_name} обслужен и покидает банк')


def simulate_cashier_work(client_name, event):
    print(f'Обслуживаю клиента {client_name}')
    sleep(0.2)
    event.set()
    print(f'Клиент {client_name} обслужен')


def main():
    events = []
    for i in range(3):
        event = Event()
        events.append(event)

    for index in range(0, len(clients)):
        thread = Thread(target=simulate_client_behavior,
                        args=(
                            clients[index],
                            events[index]
                        ))
        thread.start()
        thread.join()
    
    print('Все клиенты обслужены. Банк закрывается.')


main()
