# функция для нахождения наибольшей суммы подмассива
def max_subarray(arr):
    # инициализация макс. суммы, текущей суммы, 
    # начального, конечного и промежуточного индексов
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    s = 0

    # перебор массива по индексам
    for i in range(len(arr)):
        current_sum += arr[i]
	# нахождение макс. элемента
        if current_sum > max_sum:
	    # замена текущей суммы на макс., начального индекса на промежуточный 
	    # и конечный индекс на переменную i
            max_sum = current_sum
            start = s
            end = i

	# проверка суммы на отрицательность (если да, то текущая сумма равна 0 
	# и промежуточный индекс равен сумме i + 1)
        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return arr[start:end + 1], max_sum

# создание массива с размером 10 
array = [int(input()) for i in range(10)]

# поиск подмассива с наибольшей суммой в массиве array
result = max_subarray(array)

# вывод подмассива и суммы его элементов
print("Подмассив с максимальной суммой:", result[0])
print("Сумма элементов этого подмассива:", result[1])
