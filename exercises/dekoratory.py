def main():
    ### zasięg widzenia zmiennych ##

    def fabryka_przywitan():
        def przywitanie(imie):
            return "Hello " + imie + "!"
        # print(przywitanie)
        return przywitanie

    przywit = fabryka_przywitan()
    # print(przywit)
    # print(przywit("Adam"))
    assert przywit("Adam") == "Hello Adam!"


if __name__ == '__main__':
    main()