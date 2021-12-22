import threading

a = 0

def f1(lock):
    global a
    for _ in range(1000000):
        #lock.acquire()
        with lock:
            a += 1
        #lock.release()

def f2(lock):
    global a
    for _ in range(1000000):
        with lock:
            a -= 1

if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=f1, args=(lock,), daemon=True)
    t2 = threading.Thread(target=f2, args=(lock,), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(a)
