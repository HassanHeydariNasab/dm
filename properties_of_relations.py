# Assume that the matrix is a binary square matrix

def is_reflexive(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return False
    return True


def is_symmetric(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def is_antisymmetric(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] and matrix[j][i] and i != j:
                return False
    return True


def is_transitive(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] and matrix[j][k] and not matrix[i][k]:
                    return False
    return True
