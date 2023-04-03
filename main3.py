def cezar(wiadomosc, klucz, alfabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    wynik = ""
    for znak in wiadomosc:
        if znak.upper() not in alfabet:
            wynik += znak
            continue
        przesuniecie = klucz % len(alfabet)
        index = alfabet.index(znak.upper())
        if znak.isupper():
            nowy_index = (index + przesuniecie) % len(alfabet)
            wynik += alfabet[nowy_index]
        else:
            nowy_index = (index + przesuniecie) % len(alfabet)
            wynik += alfabet[nowy_index].lower()
    return wynik
