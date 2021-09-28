# reduce применяется когда требуется обработать список значений таким образом,
# чтобы свести процесс к единственному результату.
# 'reduce(функция, последовательность, инициализатор)'

seq = (1, 2, 3, 4, 5)
get_sum = lambda a, b: a + b


def reduce(fn, seq, initializer=None):
    it = iter(seq)
    # print(it)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
        # print(value)
    return value


summed_numbers = reduce(get_sum, seq)
print('Сумма всех чисел: ', summed_numbers)

sentences = [
    "Вечер.", "Стало темнеть.",
    "Пришлось собираться домой."
]
wsum = lambda acc, sentence: acc + len(sentence.split())
number_of_words = reduce(wsum, sentences, 0)
print('Количество слов: ', number_of_words)
