#!/usr/bin/python3
if __name__ == '__main__':
    def square_matrix_simple(matrix=[]):
        result = []
        for arr in matrix:
            square = map(lambda elem: elem ** 2, arr)
            result.append(list(square))
        return result
