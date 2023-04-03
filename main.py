import math
def ilosc_opakowan(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela, ilosc_paneli_w_opakowaniu):
    powierzchnia_pokoju = (dlugosc_podlogi * szerokosc_podlogi) * 1.1 # dodajemy 10% na straty
    powierzchnia_panela = dlugosc_panela * szerokosc_panela
    ilosc_paneli = math.ceil(powierzchnia_pokoju / powierzchnia_panela)
    ilosc_opakowan = math.ceil(ilosc_paneli / ilosc_paneli_w_opakowaniu)
    return ilosc_opakowan

print(ilosc_opakowan(4, 5, 1, 0.5, 25))