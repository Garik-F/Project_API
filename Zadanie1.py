# импортируем модуль random
import random
# инициализация переменных
number = int(input())
min_size = 2
max_size = 10
massiv_index = []
# задаем размерность массива
massiv_size = random.randint(min_size, max_size)
# создаем массив размерностью massiv_size рандомными числами в диапозоне от -10^4 до 10^4
array_massiv = [random.randint(-10 ** 4 - 1, 10 ** 4) for i in range(massiv_size)]
# перебор элементов массива
print(array_massiv)
for i in range(len(array_massiv)):
    for j in range(i, len(array_massiv)):
        if array_massiv[i] + array_massiv[j] == number:
            massiv_index.append(i)
            massiv_index.append(j)
        else:
            continue
# вывод массива
print(massiv_index)

