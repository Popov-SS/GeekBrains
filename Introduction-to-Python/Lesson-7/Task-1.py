# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = {len(i) for i in self.matrix}
        if len(self.columns) != 1:
            print('В этой матрице неравное количество элементов в строках. Её нельзя сложить с другой матрицей.')

    def __str__(self):
        self.matrix = [[str(j) for j in i] for i in self.matrix]
        print_matrix = ''
        for i in self.matrix:
            print_matrix += ' '.join(i) + '\n'
        return print_matrix

    def __add__(self, other):
        if self.columns != other.columns or self.rows != other.rows:
            return 'Матрицы нельзя сложить.'
        sum_matrix = [[] for _ in self.matrix[0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum_matrix[i].append(int(self.matrix[i][j]) + int(other.matrix[i][j]))
        return Matrix(sum_matrix)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
matrix_3 = Matrix([[100, 200, 300], [400, 500, 600], [700, 800, 900]])
print(matrix_1)
print(matrix_1 + matrix_2 + matrix_3)
