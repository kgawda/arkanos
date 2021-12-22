import multiprocessing

def f(q):
    print("Hello")
    q.put(33 ** 33)

print("Start!")
if __name__ == '__main__':
    q = multiprocessing.Queue()
    pr1 = multiprocessing.Process(target=f, args=(q,),)
    pr1.start()
    pr1.join()

    print("Wynik obliczeń:", q.get())
