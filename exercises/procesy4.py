import multiprocessing
import time

def f(q):
    print("Hello")
    time.sleep(3)
    q.put(33 ** 33)
    time.sleep(3)

print("Start!")
if __name__ == '__main__':
    time.sleep(3)
    q = multiprocessing.Queue()
    proc = []
    for i in range(10):
        proc.append(multiprocessing.Process(target=f, args=(q,), name=f"SuperProces{i}"))
    for p in proc:
        p.start()
    print("Wynik obliczeń:", q.get())
    for p in proc:
        p.join()

