import threading


def dance(n):
    global user
    user = "chenjia"
    print(threading.current_thread().native_id, threading.current_thread().name)

    # for i in range(n):
    #     print("dance", i)


def sing(n):
    global user
    print(user)
    print(threading.current_thread().native_id, threading.current_thread().name)
    # for i in range(n):
    #     print("sing", i)


if __name__ == '__main__':
    print(threading.current_thread().native_id, threading.current_thread().name)
    print(threading.current_thread())
    t1 = threading.Thread(target=dance, name="dance", args=(5,))
    t2 = threading.Thread(target=sing, name="sing", kwargs={"n": 5})
    t1.start()
    t2.start()