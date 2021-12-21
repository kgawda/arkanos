def main():
    argumenty = ["Hello", "world", "!"]
    # print(argumenty[0], argumenty[1], argumenty[2])
    print(*argumenty)

    argumenty_kluczowe = {'end': '...\n'}
    # print("Hop", end='...\n')
    print("Hop", **argumenty_kluczowe)

    # def suma(a=0, b=0, c=0, d=0, e=0, f=0, g=0, ...):
    def suma(*args):
        return sum(args)

    assert suma(1, 2, 3) == 1 + 2 + 3


if __name__ == '__main__':
    main()
