# Эта программа демонстрирует списковое включение(включение в список).

numbers = [1, 2, 3, 4, 5]
squared_numbers = []

# в цикле
for x in numbers:
    squared_numbers.append(x * x)
print(squared_numbers)

# списковое включение (синтаксический сахар)
squared_numbers = (x * x for x in numbers)
print(list(squared_numbers))
