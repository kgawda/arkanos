import threading
import time

def f(lock):
    while True:
        with lock:  # to nie jest dobry pomysł żeby długo przebywać "pod lockiem"
            print("Działa wątek", threading.get_ident(), '*' * (threading.get_ident() % 16))
            time.sleep(1)
        time.sleep(0.000001)  # <- potrzebne żeby płynnie przełączało się między wątkami (w szczególności na Linux)

if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=f, args=(lock,), daemon=True)
    t2 = threading.Thread(target=f, args=(lock,), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
