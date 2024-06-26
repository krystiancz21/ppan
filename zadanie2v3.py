def test_wrapper(func):
    def wrapper():
        print("== Only test ===")
        func()
        print("=== end test ===")
    return wrapper

def sort_articles(dane_autorow):
    sort_data = []
    for id_article, points in dane_autorow:
        row = sorted(zip(id_article, points), key=lambda x: x[1], reverse=True)
        sort_data.append(row)

    return sort_data

def ewaluacja_jednostki(dane_autorow):
    artykuly_sorted = sort_articles(dane_autorow)
    artykuly_do_ewaluacji = []
    pula_artykulow = []
    suma_punktow = 0
    liczba_autorow = len(dane_autorow)

    # Przetwarzanie danych każdego autora
    for index in range(len(artykuly_sorted)):
        if len(artykuly_sorted[index]) >= 3:
            wybrane_artykuly = artykuly_sorted[index][:3]
            reszta_artykulow = artykuly_sorted[index][3:]
        else:
            wybrane_artykuly = artykuly_sorted[index]
            reszta_artykulow = []

        artykuly_do_ewaluacji.extend(wybrane_artykuly)
        suma_punktow += sum([pkt for _, pkt in wybrane_artykuly])
        pula_artykulow.extend(reszta_artykulow)

    # Dodawanie artykułów z puli do autorów, którzy mają mniej niż 3 artykuły
    for index in range(len(artykuly_sorted)):
        while len(artykuly_sorted[index]) < 3 and pula_artykulow:
            artykul = pula_artykulow.pop(0)
            artykuly_sorted[index].append(artykul)
            artykuly_do_ewaluacji.append(artykul)
            suma_punktow += artykul[1]

    # Obliczanie wyniku ewaluacji
    wynik_ewaluacji = suma_punktow / liczba_autorow if liczba_autorow > 0 else 0

    # Lista ID artykułów do ewaluacji
    lista_artykulow_do_ewaluacji = [id_art for id_art, _ in artykuly_do_ewaluacji]

    return lista_artykulow_do_ewaluacji, wynik_ewaluacji

def wczytaj_dane():
    dane_autorow = []
    liczba_autorow = int(input("Podaj liczbę autorów: "))
    for i in range(liczba_autorow):
        print(f"--- Autor {i+1} ---")
        print("Zostaw puste pola, jeśli dany autor nie posiada artykułów")
        id_artykulow_input = input("Podaj ID artykułów oddzielone przecinkami: ")
        punkty_input = input("Podaj punkty dla każdego artykułu oddzielone przecinkami: ")

        if id_artykulow_input.strip() and punkty_input.strip():
            id_artykulow = id_artykulow_input.split(',')
            punkty = list(map(int, punkty_input.split(',')))
        else:
            id_artykulow = []
            punkty = []

        dane_autorow.append((id_artykulow, punkty))
    return dane_autorow

@test_wrapper
def testing():
    dane_autorow2 = [
        (['Art1', 'Art2', 'Art3', 'Art4'], [15, 20, 5, 10]),
        (['Art5', 'Art6'], [30, 40]),
        (['Art7'], [50]),
        ([], [])
    ]

    # Wywołanie funkcji
    artykuly_do_ewaluacji, wynik_ewaluacji = ewaluacja_jednostki(dane_autorow2)

    # Wyświetlenie wyników
    print("Artykuły do ewaluacji:", artykuly_do_ewaluacji)
    print("Wynik ewaluacji:", wynik_ewaluacji)


# only test
testing()

# Wywołanie funkcji wczytania danych i ewaluacji
dane_autorow = wczytaj_dane()
artykuly_do_ewaluacji, wynik_ewaluacji = ewaluacja_jednostki(dane_autorow)

# Wyświetlenie wyników
print("Artykuły do ewaluacji:", artykuly_do_ewaluacji)
print("Wynik ewaluacji:", wynik_ewaluacji)


