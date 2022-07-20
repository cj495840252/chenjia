import multiprocessing
import time


def task():
    # print("Mission in progress")
    time.sleep(2)
    name = multiprocessing.current_process().name
    print(name)


if __name__ == '__main__':

    p1 = multiprocessing.Process(target=task)
    # p1.daemon = True
    p1.start()
    time.sleep(0.5)
    print("main end")
    p1.terminate()
