from threading import Thread, Barrier

from time import sleep

employee_times = {
    'Алиса': 4.44, 
    'Боб': 7.33, 
    'Чарли': 7.75, 
    }


def team_meeting(barrier, name, time_to_arrive):
    print(f'{name} начал(а) идти на совещание.')
    sleep(time_to_arrive)
    print(f'{name} прибыл(а) на совещание, затратив {time_to_arrive} секунд.')
    barrier.wait()


def team_meeting_start_message():
    print('Совещание началось!')


def main():
    barrier = Barrier(len(employee_times),
                      action=team_meeting_start_message)
    for name, time_to_arrive in employee_times.items():
        Thread(target=team_meeting, args=(barrier, name, time_to_arrive)).start()

main()
