from threading import Thread, Semaphore

from time import sleep

name_list = [
    "Клиент Веселый Шутник",
    "Клиент Читающий Поэт",
    "Клиент Спешащий Бизнесмен",
    "Клиент Мечтающий Путешественник",
    "Клиент Меланхоличный Художник",
    "Клиент Загадочная Улыбка",
    "Клиент Задумчивый Философ",
    "Клиент Вечно Опаздывающий",
    "Клиент Гадающий на Кофейной Гуще",
    "Клиент Неугомонный Блогер"
]


cafe_semaphore = Semaphore(3)


def client(client_name):
    with cafe_semaphore:
        print(f'{client_name} нашел свободный столик и заказывает кофе')
        sleep(.5)
        print(f'{client_name} насладился кофе и освобождает столик для следующих гостей')


def main():
    threads = []
    for client_name in name_list:
        thread = Thread(target=client,
                        args=(client_name,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

main()
