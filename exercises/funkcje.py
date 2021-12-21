def main():
    argumenty = ["Hello", "world", "!"]
    # print(argumenty[0], argumenty[1], argumenty[2])
    print(*argumenty)

    argumenty_kluczowe = {'end': '...\n'}
    # print("Hop", end='...\n')
    print("Hop", **argumenty_kluczowe)

    # def suma(a=0, b=0, c=0, d=0, e=0, f=0, g=0, ...):
    def suma(*args):
        """Sumuje argumenty
        >>>suma(1, 2)
        3
        """
        return sum(args)

    assert suma(1, 2, 3) == 1 + 2 + 3

def kwadrat(x):
    """Zwraca kwadrat danej liczby.

    Przykłady:
    >>> kwadrat(5)
    25

    >>> kwadrat(-1)
    1
    """
    return x ** 2


if __name__ == '__main__':
    main()
