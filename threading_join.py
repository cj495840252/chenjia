import threading


count = 0


def sum1():
    global count
    for i in range(1000000):
        count += 1
    print("sum1", count)


def sum2():
    global count
    for i in range(1000000):
        count += 1
    print("sum2", count)


if __name__ == '__main__':
    t1 = threading.Thread(target=sum1, name="sum1")
    t2 = threading.Thread(target=sum2, name="sum2")
    t1.start()
    t1.join()
    t2.start()
