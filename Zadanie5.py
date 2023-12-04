# функция для создания матрицы размера 4*4
def generate_4x4_matrix():
    matrix = [[int(input()) for _ in range(4)] for _ in range(4)]
    return matrix

# функция для нахождения определителя матрицы размера 4*4
def determinant_4x4(matrix):
    # формула для нахождения определителя матрицы
    det = (
        matrix[0][0] * matrix[1][1] * matrix[2][2] * matrix[3][3] +
        matrix[0][0] * matrix[1][2] * matrix[2][3] * matrix[3][1] +
        matrix[0][0] * matrix[1][3] * matrix[2][1] * matrix[3][2] -
        matrix[0][0] * matrix[1][3] * matrix[2][2] * matrix[3][1] -
        matrix[0][0] * matrix[1][2] * matrix[2][1] * matrix[3][3] -
        matrix[0][0] * matrix[1][1] * matrix[2][3] * matrix[3][2] -

        matrix[0][1] * matrix[1][0] * matrix[2][2] * matrix[3][3] -
        matrix[0][1] * matrix[1][2] * matrix[2][3] * matrix[3][0] -
        matrix[0][1] * matrix[1][3] * matrix[2][0] * matrix[3][2] +
        matrix[0][1] * matrix[1][3] * matrix[2][2] * matrix[3][0] +
        matrix[0][1] * matrix[1][2] * matrix[2][0] * matrix[3][3] +
        matrix[0][1] * matrix[1][0] * matrix[2][3] * matrix[3][2] +

        matrix[0][2] * matrix[1][0] * matrix[2][1] * matrix[3][3] +
        matrix[0][2] * matrix[1][1] * matrix[2][3] * matrix[3][0] +
        matrix[0][2] * matrix[1][3] * matrix[2][0] * matrix[3][1] -
        matrix[0][2] * matrix[1][3] * matrix[2][1] * matrix[3][0] -
        matrix[0][2] * matrix[1][1] * matrix[2][0] * matrix[3][3] -
        matrix[0][2] * matrix[1][0] * matrix[2][3] * matrix[3][1] -

        matrix[0][3] * matrix[1][0] * matrix[2][1] * matrix[3][2] -
        matrix[0][3] * matrix[1][1] * matrix[2][2] * matrix[3][0] -
        matrix[0][3] * matrix[1][2] * matrix[2][0] * matrix[3][1] +
        matrix[0][3] * matrix[1][2] * matrix[2][1] * matrix[3][0] +
        matrix[0][3] * matrix[1][1] * matrix[2][0] * matrix[3][2] +
        matrix[0][3] * matrix[1][0] * matrix[2][2] * matrix[3][1]
    )

    return det

# Создание и вывод случайной матрицы 4x4
matrix = generate_4x4_matrix()
print("Сгенерированная матрица 4x4:")
for row in matrix:
    print(row)

# вызов функции определителя матрицы 4*4
determinant = determinant_4x4(matrix)
print("\nОпределитель матрицы 4x4:", determinant)
