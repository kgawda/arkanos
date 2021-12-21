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

    def fabryka_przywitan_miedzynarodowych(hello_w_danym_jezyku):
        def przywitanie(imie):
            return hello_w_danym_jezyku + " " + imie + "!"
        return przywitanie

    przywitaj_po_polsku = fabryka_przywitan_miedzynarodowych("Witaj")
    przywitaj_po_hiszpansku = fabryka_przywitan_miedzynarodowych("Ola")

    assert przywitaj_po_polsku("Mieszko") == "Witaj Mieszko!"
    assert przywitaj_po_hiszpansku("Rodrigez") == "Ola Rodrigez!"

    print(przywitaj_po_polsku.__code__.co_freevars)
    print(przywitaj_po_polsku.__closure__[0].cell_contents)

    ### wrapper ###

    def podaj_kod_do_sejfu():
        return 6734958

    def podaj_kod_do_sejfu_logowane():
        print("Rozpoczęto podawanie kodu do sejfu")
        result = podaj_kod_do_sejfu()
        print("Kod do sejfu gotowy")
        return result

    print(podaj_kod_do_sejfu_logowane())


    def funkcja_z_logowaniem(f):
        ...

    print(funkcja_z_logowaniem(podaj_kod_do_sejfu)())
    """
    Rozpoczęto wykonanie funkcji
    Zakończono wykonanie funkcji
    6734958
    """


if __name__ == '__main__':
    main()