from decimal import Decimal
import numpy as np
import timeit

## ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
## przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

def zad1(kod1, kod2):
    clean = lambda x: int(x.replace('-', ''))
    kod1, kod2 = clean(kod1), clean(kod2)
    return ["%02d-%03d" % divmod(kod, 1000) for kod in range(kod1 + 1, kod2)]

## zwracamy listę kodów z podanego zakresu
## (uwzględniajać zasadę, że nie ma kodu pocztowego z trzema zerami -000)

def zad11(kod1, kod2):
    clean = lambda x: int(x.replace('-', ''))
    kod1, kod2 = clean(kod1), clean(kod2)
    return ["%02d-%03d" % divmod(kod, 1000)
            for kod in [x for x in range(kod1 + 1, kod2) if divmod(x,1000)[1]!=0]]

## ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
## NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
## 1-n = [1,2,3,4,5,...,10]
## np. n=10
## wejście: [2,3,7,4,9], 10
## wyjście: [1,5,6,8,10]

def zad2(l, n):
    return list(set(range(1,n+1))-set(l))

## ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5,
## DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
## test

def zad3():
    return [Decimal(20 + x * 5)/10 for x in range(8)] 
    

def zad31():
    return list(map(Decimal,np.arange(2,6,0.5)))


print(zad1("79-900", "80-155"))
print(zad11("79-900", "80-155"))
print(zad2([2,3,7,4,9], 10))
print(zad3())
print(zad31())

##import timeit
##timeit.timeit(f'x = [Decimal(20 + x * 5)/10 for x in range(8)]', setup='from decimal import Decimal')
##timeit.timeit(f'x = list(map(Decimal,np.arange(2,6,0.5)))', setup='from decimal import Decimal; import numpy as np')

