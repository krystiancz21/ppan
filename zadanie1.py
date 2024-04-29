def oblicz_h_index(quotations):
    quotations.sort(reverse=True)

    # Obliczanie h-index
    h_index = 0
    for i, cyt in enumerate(quotations):
        if i < cyt:
            h_index += 1
        else:
            break

    return h_index


h_idx1 = [5,3,1]
h_idx2 = [22,13,76,54,2,6,31,3,1]

print(oblicz_h_index(h_idx1))

print(oblicz_h_index(h_idx2))
