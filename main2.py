def czy_pierwsza(*args):
    wyniki = []
    for n in args:
        if n < 2:
            wyniki.append(False)
            continue
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                wyniki.append(False)
                break
        else:
            wyniki.append(True)
    return wyniki
print(czy_pierwsza(2,3,5,11,13,19,29,4))
