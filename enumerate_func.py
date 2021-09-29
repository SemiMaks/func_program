# Встроенная функция enumerate  возвращает индекс элемента и сам
# элемент последовательности в качестве кортежа.
# 'enumerate(последовательность)'

lazy = enumerate(['a', 'b', 'c'])
print(list(lazy))
# [(0, 'a'), (1, 'b'), (2, 'c')]

convert = lambda tup: tup[1].upper() + str(tup[0])
lazy = map(convert, enumerate(['a', 'b', 'c']))
print(list(lazy))
# ['A0', 'B1', 'C2']
