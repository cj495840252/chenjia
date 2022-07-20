import threading


count = 0


def sum1(lock):
    lock.acquire()
    global count
    for i in range(1000000):
        count += 1
    lock.release()
    print("sum1", count)


def sum2(lock):
    lock.acquire()
    global count
    for i in range(1000000):
        count += 1
    lock.release()
    print("sum2", count)


if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=sum1, name="sum1", args=(lock,))
    t2 = threading.Thread(target=sum2, name="sum2", args=(lock,))
    t1.start()
    t2.start()