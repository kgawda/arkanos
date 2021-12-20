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






if __name__ == "__main__":
    main()
