class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['  '.join([f'{num:<2}' for num in line]) for line in self.matrix])

    def __getitem__(self, i):
        return self.matrix[i]

    def __add__(self, other):
        try:
            res = [[self.matrix[i][j] + other[i][j] for j in range(len(self.matrix[i]))]
                                                    for i in range(len(self.matrix))]
            return Matrix(res)
        except IndexError:
            return 'Разные матрицы'

if __name__ == '__main__':
    m1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
    print(f'Отображение матрицы\n{m1}')
    print()
    m2 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
    print(f'Сложение матриц\n{m1 + m2}')
    print()
    m3 = Matrix([[1, 2], [3, 4]])
    print(m1 + m3)
