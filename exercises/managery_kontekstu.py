import contextlib
import time

def main():
    with open('managery_kontekstu.py') as f:
        dane = f.read()
    print(dane[:12])

    with contextlib.suppress(ZeroDivisionError):
        1/0

    @contextlib.contextmanager
    def pomiar_czasu():
        t1 = time.perf_counter()
        try:
            yield t1
        finally:
            t2 = time.perf_counter()
            print("To zajęło", t2 - t1, "s")

    with contextlib.suppress(ZeroDivisionError):
    # używamy supporess żeby pokazać obsługę błędu przez pomiar_czasu (finally),
    # a jednocześnie żeby wykonanie tego skryptu nie kończyło się błędem
        with pomiar_czasu():  # opcjonalnie: as started_at:
            time.sleep(1.2/0)


if __name__ == '__main__':
    main()
