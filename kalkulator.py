def dodawanie(a, b): # a,b - dowolne liczby
    return a + b

def odejmowanie(a, b): # a,b - dowolne liczby
    return a - b

def mnozenie(a,b): # a,b - dowolne liczby
    return a * b

def dzielenie(a,b): # a,b - dowolne liczby
    if b == 0:
        print("Nie wolno dzielić przez zero!")
    else:
        return a / b

def wyswietlWynik(wynik):
    print("Wynik działania wynosi", wynik)

def kalkulator(a,b,znak): # a,b - dowolne liczby; znak - znak działania
    if type(a) == int and type(b) == int:
        if znak == "+":
            wyswietlWynik(dodawanie(a,b))
        elif znak == "-":
            wyswietlWynik(odejmowanie(a,b))
        elif znak == "*":
            wyswietlWynik(mnozenie(a,b))
        elif znak == "/":
            wyswietlWynik(dzielenie(a,b))
    else:
        raise TypeError("Błędny typ danych!")