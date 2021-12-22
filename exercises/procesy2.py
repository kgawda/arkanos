import multiprocessing

def f():
    print("Hello")

print("Start!")
if __name__ == '__main__':
    pr1 = multiprocessing.Process(target=f)
    pr1.start()
    pr1.join()
