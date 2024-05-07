def sort_by_length(data):
    sorted_data = sorted(data, key=lambda x: len(x[0]))
    return sorted_data

def sort_articles(dane_autorow):
    sort_data = []
    for id_article, points in dane_autorow:
        row = sorted(zip(id_article, points), key=lambda x: x[1], reverse=True)
        sort_data.append(row)

    return sort_data

def ewaluacja_jednostki(dane_autorow):
    sorted_articles = sort_articles(dane_autorow)
    print(sorted_articles)

    artykuly_do_ewaluacji = []
    suma_punktow = 0
    liczba_autorow = len(dane_autorow)

    # Przetwarzanie danych każdego autora
    for index in range(len(sorted_articles)):
        wybrane_artykuly = sorted_articles[index][:3]
        artykuly_do_ewaluacji.extend(wybrane_artykuly)
        # Usuwanie pierwszych trzech elementów z listy
        sorted_articles[index] = sorted_articles[index][3:]
        suma_punktow += sum([pkt for _, pkt in wybrane_artykuly])

    # print(sorted_articles)
    # print('###')
    # print(artykuly_do_ewaluacji)




    # Lista ID artykułów do ewaluacji
    lista_artykulow_do_ewaluacji = [id_art for id_art, _ in artykuly_do_ewaluacji]

    # Obliczanie wyniku ewaluacji
    if liczba_autorow > 0:
        wynik_ewaluacji = suma_punktow / liczba_autorow
    else:
        wynik_ewaluacji = 0

    return lista_artykulow_do_ewaluacji, wynik_ewaluacji


# Przykładowe dane wejściowe
dane_autorow = [
    (['Art1', 'Art2', 'Art3'], [10, 20, 5]),
    (['Art4', 'Art5'], [30, 40]),
    (['Art6'], [50]),
    ([], [])
]

dane_autorow2 = [
    (['Art1', 'Art2', 'Art3', 'Art4'], [15, 20, 5, 10]),
    (['Art5', 'Art6'], [30, 40]),
    (['Art7'], [50]),
    ([], [])
]

dane_autorow3 = [
    (['Art5', 'Art6'], [30, 40]),
    ([], []),
    (['Art1', 'Art2', 'Art3', 'Art4'], [15, 20, 5, 10]),
    (['Art7'], [50]),
]

# Wywołanie funkcji
# ewaluacja_jednostki(dane_autorow2)
artykuly_do_ewaluacji, wynik_ewaluacji = ewaluacja_jednostki(dane_autorow)

# Wyświetlenie wyników
print("Artykuły do ewaluacji:", artykuly_do_ewaluacji)
print("Wynik ewaluacji:", wynik_ewaluacji)


###############################################################33

# 2. Na potrzeby ewaluacji wymagane jest złożenie 3 artykułów przez każdego autora.

# 3. W przypadku, gdy autor ma tylko 2 artykuły, trzeci artykuł może być uzupełniony
# artykułem innego autora, przy czym dowolny autor może złożyć maksymalnie 4 artykuły.

# 4. W przypadku, gdy autor ma tylko 1 artykuł, drugi artykuł może być uzupełniony
# artykułem innego autora, przy czym dowolny autor może złożyć maksymalnie 4 artykuły.
# Brak trzeciego artykułu to kara dla jednostki.

# 5. W przypadku, gdy autor nie ma artykułów, nic nie składa i jego wkład punktowy wynosi 0
# punktów, jest to kara dla jednostki.
