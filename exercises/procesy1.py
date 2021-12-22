import urllib.request
import concurrent.futures
import time

def f(url):
    t1 = time.perf_counter()
    urllib.request.urlopen(url).read()
    t2 = time.perf_counter()
    return f"Czas {t2-t1} s dla {url}"

dane = [
    'https://wp.pl',
    'https://onet.pl',
    'https://google.com',
    'https://alx.pl',
]

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for wynik in executor.map(f, dane):
            print(wynik)

