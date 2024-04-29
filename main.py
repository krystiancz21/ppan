def oblicz_h_index(id_artykulow, cytowania):
    """
    Funkcja oblicza indeks Hirscha dla danych cytowań artykułów.
    :param id_artykulow: Lista identyfikatorów artykułów
    :param cytowania: Lista liczb cytowań odpowiadających artykułom
    :return: Indeks Hirscha (h-index)
    """
    # Tworzenie listy par (id artykułu, liczba cytowań) i sortowanie jej według liczby cytowań malejąco
    pary = list(zip(id_artykulow, cytowania))
    pary.sort(key=lambda x: x[1], reverse=True)

    # Obliczanie h-index
    h_index = 0
    for i, (_, cyt) in enumerate(pary):
        if i < cyt:
            h_index += 1
        else:
            break

    return h_index


def ewaluacja_jednostki(dane_autorow):
    """
    Funkcja zwraca wykaz artykułów zaklasyfikowanych do ewaluacji jednostki oraz oblicza wynik ewaluacji.

    :param dane_autorow: Lista zawierająca dane dla każdego autora w formacie:
                         [(lista_id_artykulow, lista_punktow), ...]
    :return: (lista_artykulow_do_ewaluacji, wynik_ewaluacji)
    """
    # Słownik do przechowywania sumy punktów dla każdego artykułu
    punkty_artykulow = {}

    # Przetwarzanie danych każdego autora
    for id_artykulow, punkty in dane_autorow:
        for id_art, pkt in zip(id_artykulow, punkty):
            if id_art in punkty_artykulow:
                punkty_artykulow[id_art] += pkt
            else:
                punkty_artykulow[id_art] = pkt

    # Lista artykułów do ewaluacji (wszystkie artykuły)
    artykuly_do_ewaluacji = list(punkty_artykulow.keys())

    # Wynik ewaluacji (suma punktów wszystkich artykułów)
    wynik_ewaluacji = sum(punkty_artykulow.values())

    return artykuly_do_ewaluacji, wynik_ewaluacji

# Przykładowe dane wejściowe
dane_autorow = [
    (['Art1', 'Art2'], [10, 20]),
    (['Art3', 'Art4'], [30, 40]),
    (['Art5', 'Art6'], [50, 60])
]

# Wywołanie funkcji
artykuly_do_ewaluacji, wynik_ewaluacji = ewaluacja_jednostki(dane_autorow)

# Wyświetlenie wyników
print("Artykuły do ewaluacji:", artykuly_do_ewaluacji)
print("Wynik ewaluacji:", wynik_ewaluacji)