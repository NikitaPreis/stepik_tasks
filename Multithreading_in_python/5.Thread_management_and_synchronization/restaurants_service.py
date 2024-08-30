from threading import Thread, Condition

from queue import Queue

from time import sleep

visitors = ['Алиса', 'Владимир', 'Сергей']


cv = Condition()


def make_coffee(visitors, q):
    while True:
        with cv:
            if q.empty():
                sleep(0.1)
                continue
            else:
                visitor = q.get()
                if visitor == 'stop':
                    break
                print(f'Готовим кофе для {visitor}')
                sleep(1)
                print(f'Кофе для {visitor} готов')
                cv.notify(n=1)
                continue


def take_coffee(visitors, q):
    for visitor in visitors:
        print(f'{visitor} зашел в кафе')
    index = 0
    while index <= len(visitors):
        # for visitor in visitors:
        if index == len(visitors):
            q.put('stop')
            break
        # print(f'{visitors[index]} зашел в кафе')
        q.put(visitors[index])
        with cv:
            cv.wait(timeout=3)
            print(f'{visitors[index]} получил свой кофе')
            index += 1
            continue


# def take_coffee(visitors, q):
#     index = 0
#     while index <= len(visitors):
#         # for visitor in visitors:
#         if index == len(visitors):
#             q.put('stop')
#             break
#         print(f'{visitors[index]} зашел в кафе')
#         q.put(visitors[index])
#         with cv:
#             cv.wait(timeout=10)
#             print(f'{visitors[index]} получил свой кофе')
#         index += 1

    # for index in range(3):
    #     with cv:
    #         cv.wait()
    #         print(f'{visitors[index]} получил свой кофе')



# def take_coffee(visitors, q, cv):
#     index = 0
#     while index <= len(visitors):
#         # for visitor in visitors:
#         if index == len(visitors):
#             q.put('stop')
#         print(f'{visitors[index]} зашел в кафе')
#         q.put(visitors[index])
#         with cv:
#             cv.wait()
#             print(f'{visitors[index]} получил свой кофе')
#         index += 1


def main():
    # cv = Condition()
    q = Queue()

    barista_thread = Thread(target=make_coffee,
                            args=(visitors,
                                  q,
                                #   cv
                                  )
                            )
    visitor_thread = Thread(target=take_coffee,
                            args=(visitors,
                                  q,
                                #   cv
                                  )
                            )
    barista_thread.start()
    visitor_thread.start()
    barista_thread.join()
    visitor_thread.join()
    print('Все посетители получили свой кофе. Работа завершена.')


main()
