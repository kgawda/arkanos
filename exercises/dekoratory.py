import functools

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
        def wrapper():
            print("Rozpoczęto wykonanie funkcji", f.__name__)
            result = f()
            print("Zakończono wykonanie funkcji", f.__name__)
            return result
        return wrapper

    # print(funkcja_z_logowaniem(podaj_kod_do_sejfu)())
    podaj_kod_do_sejfu = funkcja_z_logowaniem(podaj_kod_do_sejfu)
    assert podaj_kod_do_sejfu() == 6734958

    @funkcja_z_logowaniem  # ==> podaj_kod_do_innego_sejfu = funkcja_z_logowaniem(podaj_kod_do_innego_sejfu)
    def podaj_kod_do_innego_sejfu():
        return 8745093

    print(podaj_kod_do_innego_sejfu())

    def funkcja_z_logowaniem2(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print("Rozpoczęto wykonanie funkcji", f.__name__)
            result = f(*args, **kwargs)
            print("Zakończono wykonanie funkcji", f.__name__)
            return result
        #wrapper.__name__ = f.__name__
        #wrapper.__doc__ = f.__doc__
        # albo:
        #functools.update_wrapper(wrapper, f)
        # albo:
        #użyć @functools.wraps(f)
        return wrapper

    @funkcja_z_logowaniem2
    def identycznosc(x):
        return x

    assert identycznosc(5) == 5
    assert identycznosc.__name__ == "identycznosc"

    ### dekorator z argumentami
    def funkcja_z_logowaniem_wielojezyczna(start_w_jezyku, end_w_jezyku):
        def dekorator(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                print(start_w_jezyku, f.__name__)
                result = f(*args, **kwargs)
                print(end_w_jezyku, f.__name__)
                return result
            return wrapper
        return dekorator

    # dekorator z argumentami?
    # to tak naprawdę wywołanie funkcji, która przyjmie argumenty i zwróci dekorator
    # np.: funkcja functools.wraps(f) dopiero zwróci właściwy dekorator
    # O ile dekorator jest fabryką wrapperów, to np.  funkcja_z_logowaniem_wielojezyczna
    # jest fabryką fabryk wrapperów.

    @funkcja_z_logowaniem_wielojezyczna("Buongiorno", "Arivederci")
    def test(x):
        return x

    test(1)

if __name__ == '__main__':
    main()