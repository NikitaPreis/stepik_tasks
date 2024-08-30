from threading import Thread, Barrier

from time import sleep, time

from random import randint

car_models = ["Toyota", "BMW", "Audi", "Mercedes", "Ford", "Honda", "Nissan", "Chevrolet", "Volkswagen", "Kia"]


def car_race(car_model, barrier):
    barrier.wait()
    start_time = time()
    drive_duration = randint(1, 5)
    sleep(drive_duration)
    race_time = time() - start_time
    print(f'Автомобиль {car_model} финишировал за {race_time:.2f} секунд')


def main():
    barrier = Barrier(len(car_models))
    threads = []

    for car_model in car_models:
        thread = Thread(target=car_race,
                        args=(car_model,
                              barrier))
        thread.start()


main()

