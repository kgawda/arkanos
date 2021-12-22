import threading
import time

def f():
    print("Hello", threading.get_ident())
    time.sleep(0.2)

t1 = threading.Thread(target=f, daemon=True)
t2 = threading.Thread(target=f, daemon=True)
t1.start()
t2.start()
print("Wątek wystartował z", threading.get_ident())
t1.join()  # zaczkaj aż wątek zakończy działanie
t2.join()
