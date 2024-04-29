def ewaluacja_jednostki(dane_autorow):
    """
    Funkcja zwraca wykaz artykułów zaklasyfikowanych do ewaluacji jednostki oraz oblicza wynik ewaluacji.

    :param dane_autorow: Lista zawierająca dane dla każdego autora w formacie:
                         [(lista_id_artykulow, lista_punktow), ...]
    :return: (lista_artykulow_do_ewaluacji, wynik_ewaluacji)
    """
    artykuly_do_ewaluacji = []
    suma_punktow = 0
    liczba_autorow = len(dane_autorow)

    # Przetwarzanie danych każdego autora
    for id_artykulow, punkty in dane_autorow:
        # Sortowanie artykułów autora według punktów malejąco
        pary = sorted(zip(id_artykulow, punkty), key=lambda x: x[1], reverse=True)

        # Wybór 3 najlepszych artykułów, jeśli jest ich mniej, wybieramy wszystkie
        wybrane_artykuly = pary[:3]
        artykuly_do_ewaluacji.extend(wybrane_artykuly)

        # Sumowanie punktów wybranych artykułów
        suma_punktow += sum([pkt for _, pkt in wybrane_artykuly])

    # Obliczanie wyniku ewaluacji
    if liczba_autorow > 0:
        wynik_ewaluacji = suma_punktow / liczba_autorow
    else:
        wynik_ewaluacji = 0

    # Lista ID artykułów do ewaluacji
    lista_artykulow_do_ewaluacji = [id_art for id_art, _ in artykuly_do_ewaluacji]

    return lista_artykulow_do_ewaluacji, wynik_ewaluacji


# Przykładowe dane wejściowe
dane_autorow = [
    (['Art1', 'Art2', 'Art3'], [10, 20, 5]),
    (['Art4', 'Art5'], [30, 40]),
    (['Art6'], [50]),
    ([], [])
]

# Wywołanie funkcji
artykuly_do_ewaluacji, wynik_ewaluacji = ewaluacja_jednostki(dane_autorow)

# Wyświetlenie wyników
print("Artykuły do ewaluacji:", artykuly_do_ewaluacji)
print("Wynik ewaluacji:", wynik_ewaluacji)

# def ewaluacja_jednostki(dane_autorow):
#     """
#     Funkcja zwraca wykaz artykułów zaklasyfikowanych do ewaluacji jednostki oraz oblicza wynik ewaluacji.
#
#     :param dane_autorow: Lista zawierająca dane dla każdego autora w formacie:
#                          [(lista_id_artykulow, lista_punktow), ...]
#     :return: (lista_artykulow_do_ewaluacji, wynik_ewaluacji)
#     """
#     # Słownik do przechowywania sumy punktów dla każdego artykułu
#     punkty_artykulow = {}
#
#     # Przetwarzanie danych każdego autora
#     for id_artykulow, punkty in dane_autorow:
#         for id_art, pkt in zip(id_artykulow, punkty):
#             if id_art in punkty_artykulow:
#                 punkty_artykulow[id_art] += pkt
#             else:
#                 punkty_artykulow[id_art] = pkt
#
#     # Lista artykułów do ewaluacji (wszystkie artykuły)
#     artykuly_do_ewaluacji = list(punkty_artykulow.keys())
#
#     # Wynik ewaluacji (suma punktów wszystkich artykułów)
#     wynik_ewaluacji = sum(punkty_artykulow.values())
#
#     return artykuly_do_ewaluacji, wynik_ewaluacji
#
# # Przykładowe dane wejściowe
# dane_autorow = [
#     (['Art1', 'Art2'], [10, 20]),
#     (['Art3', 'Art4'], [30, 40]),
#     (['Art5', 'Art6'], [50, 60])
# ]
#
# # Wywołanie funkcji
# artykuly_do_ewaluacji, wynik_ewaluacji = ewaluacja_jednostki(dane_autorow)
#
# # Wyświetlenie wyników
# print("Artykuły do ewaluacji:", artykuly_do_ewaluacji)
# print("Wynik ewaluacji:", wynik_ewaluacji)