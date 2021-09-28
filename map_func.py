# map позволяет преобразовать некую последовательность в другую.
# отображение(map) позволяет применить специальную функцию для всех
# элементов последовательности.
# 'map(функция, последовательность)'

from lambda_func import lambda_function

seq1 = (1, 2, 3, 4, 5)
seq2 = (6, 7, 8, 9, 10)
seq3 = (11, 12, 13, 14, 15)
print(map(lambda_function, seq1, seq2, seq3))
print(list(map(lambda_function, seq1, seq2, seq3)))
# <map object at 0x00000000025AB040>
# [18, 21, 24, 27, 30]