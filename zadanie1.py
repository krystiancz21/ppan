def simple_count_hirsch_index(quotations):
    quotations.sort(reverse=True)

    # Obliczanie h-index
    h_index = 0
    for i, cyt in enumerate(quotations):
        if i < cyt:
            h_index += 1
        else:
            break

    return h_index


def count_hirsch_index(list_citation):
    list_citation.sort(reverse=True)
    # Calculation h-index
    h_index = sum(1 for i, cyt in enumerate(list_citation) if i < cyt)
    return h_index


# Test
h_idx1 = [5, 3, 1]
print(simple_count_hirsch_index(h_idx1))

h_idx2 = [22, 13, 76, 54, 2, 6, 31, 3, 1]
print(simple_count_hirsch_index(h_idx2))
print(count_hirsch_index(h_idx2))

articles_number = int(input("Number of articles: "))

articles = []
for i in range(articles_number):
    item = int(input(f"Give number of cites for {i+1} article: "))
    articles.append(item)

result = count_hirsch_index(articles)

print("Author's Hirsch index: ", result)
