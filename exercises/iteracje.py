def main():
    l = [1, 2, 3]

    result = 0
    for x in l:
        result += x
    assert result == 1 + 2 + 3

    result = 0
    iterator = iter(l)
    # iter(l) ==> l.__iter__()
    # next(i) ==> i.__next__()
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    result += next(iterator)
    result += next(iterator)
    result += next(iterator)
    # result += next(iterator)  # StopIteration
    assert result == 1 + 2 + 3

    result = 0
    iterator = iter(l)
    while True:
        try:
            x = next(iterator)
        except StopIteration:
            break
        result += x  # tu użyteczny kod pętli for
    assert result == 1 + 2 + 3

    # praktyczny przykład
    r = range(5)
    iterator = iter(r)
    pierwszy_element = next(iterator)
    # kolejne_elementy = list(iterator)
    kolejne_elementy = []
    for x in iterator:
        kolejne_elementy.append(x)

    result = 0
    with open('iteracje.py') as f:
        for line in f:
            if line.lstrip().startswith('#'):
                result += 1
            #print(">>>", line, end="")


    def jeden_dwa_trzy():
        print("zaraz podam 1")
        yield 1
        print("zaraz podam 2")
        yield 2
        print("zaraz podam 3")
        yield 3
        print("koniec generowania")

    l = []
    for x in jeden_dwa_trzy():
        print(x)
        l.append(x)
    assert l == [1, 2, 3]

    def my_map(function, iterable):
        for item in iterable:
            yield function(item)

    assert list(map(int, ["1", "23"])) == [1, 23]
    assert list(my_map(int, ["1", "23"])) == [1, 23]

    l = [1, 2, 3]
    for i in range(len(l)):
        print(i, l[i])
    for i, elem in enumerate(l):
        print(i, elem)

    import itertools
    assert list(itertools.chain([1, 2], "ab")) == [1, 2, "a", "b"]

    def my_map2(function, iterable):
        yield from map(function, iterable)
        # to samo co:
        # for x in map(function, iterable):
        #     yield x


class MyRange:  # iterable (iterowalny)
    class MyRangeIterator:  # iterator
        def __init__(self, n):
            self.max = n
            self.current = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = self.current
            if result >= self.max:
                raise StopIteration()
            self.current += 1
            return result

    def __init__(self, n):
        self.max = n

    def __iter__(self):  # to jest to, co jest wywoływane przez iter()
        return self.MyRangeIterator(self.max)

def demo_my_range():
    r = MyRange(5)  # powinno działać tak samo jak range(5)
    assert list(r) == [0, 1, 2, 3, 4]
    assert list(r) == [0, 1, 2, 3, 4]
    for x in MyRange(5):
        # MyRange(5) zwraca obiekt iterowany
        # interpreter pobiera iterator przez iter()
        #   iterator jest zwracany przez MyRange.__iter__
        #   czyli jest to obiekt klasy MyRangeIterator
        # przy każdym kroku pętli interpreter wykonuje next()
        #   co wywołuje __next__() w iteratorze
        print(x)


if __name__ == "__main__":
    main()
    demo_my_range()
