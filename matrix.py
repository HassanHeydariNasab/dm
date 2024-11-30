class Matrix:
    def __init__(self, matrix: list[list[bool]]):
        if len(matrix) != 0:
            cols = len(matrix[0])
            for i in range(len(matrix)):
                if len(matrix[i]) != cols:
                    raise ValueError("Malformed matrix")
        self.m = matrix
        self.r = len(matrix)
        self.c = 0 if self.r == 0 else len(matrix[0])

    def __repr__(self):
        return str(self.m)

    def __mul__(self, other):
        if isinstance(other, bool):
            result: Matrix = Matrix(self.m)
            for i in range(len(self.m)):
                for j in range(len(self.m[0])):
                    result.m[i][j] = result.m[i][j] and other
            return result

        elif isinstance(other, Matrix):
            if self.c != other.r:
                raise ArithmeticError(
                    "Can't multiply Matrix with incompatible dimensions"
                )
            result: Matrix = Matrix([[False] * self.c for _ in range(other.r)])
            for i in range(self.r):
                for j in range(other.c):
                    sum = False
                    for element_index in range(self.c):
                        sum = sum or (
                            self.m[i][element_index] and other.m[j][element_index]
                        )
                    result.m[i][j] = sum
            return result

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Matrix):
            if self.r != other.r or self.c != other.c:
                return False
            for i in range(self.r):
                for j in range(self.c):
                    if self.m[i][j] != other.m[i][j]:
                        return False
            return True
        raise ArithmeticError(
            "Can't compare Matrix with object of type " + type(other).__name__
        )

    def is_reflexive(self) -> bool:
        for i in range(len(self.m)):
            if not self.m[i][i]:
                return False
        return True

    def is_symmetric(self) -> bool:
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                if self.m[i][j] != self.m[j][i]:
                    return False
        return True

    def is_antisymmetric(self) -> bool:
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                if self.m[i][j] and self.m[j][i] and i != j:
                    return False
        return True

    def is_transitive(self) -> bool:
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                for k in range(len(self.m)):
                    if self.m[i][j] and self.m[j][k] and not self.m[i][k]:
                        return False
        return True

    def is_transitive2(self) -> bool:
        return True
