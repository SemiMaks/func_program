# Формат определения лямбда-функции:
# 'lambda список_аргументов: выражение'

lambda_function = lambda x, y, c: x + y + c
print('Результат выражение лямбда функции составляет: ', lambda_function(3, 4, 5))

func = lambda_function
print('Результат выражение лямбда функции, присвоенной func, составляет: ', func(1, 3, 4))

dic = {
    'функция': lambda_function
}
print('В словаре по ключу отражается результат выражения лямбда функции: ', dic['функция'](5, 6, 7))
