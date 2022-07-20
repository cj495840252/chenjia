import multiprocessing
import time
import os


def dance(num):
    # print("p1 progress pid = ", os.getpid())
    print("father progress pid = ", os.getppid())
    print(multiprocessing.current_process().name, multiprocessing.current_process().pid)
    for i in range(num):
        time.sleep(0.1)
        print("dance", i)


def sing(num):
    print("p2 progress pid = ", os.getpid())
    print("father progress pid = ", os.getppid())
    print(multiprocessing.current_process().name, multiprocessing.current_process().pid)

    for i in range(num):
        time.sleep(0.3)
        print("sing", i)


if __name__ == '__main__':
    print("main progress pid = ", os.getpid())
    print(multiprocessing.current_process().name, multiprocessing.current_process().pid)
    p1 = multiprocessing.Process(target=dance, args=(5,), name="dance")
    p2 = multiprocessing.Process(target=sing, kwargs={'num': 5}, name="sing")
    p1.start()
    p2.start()
