import threading

a = 0

def f1():
    global a
    for _ in range(1000000):
        a += 1

def f2():
    global a
    for _ in range(1000000):
        a -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=f1, daemon=True)
    t2 = threading.Thread(target=f2, daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(a)
