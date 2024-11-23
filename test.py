from properties_of_relations import (
    is_reflexive,
    is_symmetric,
    is_antisymmetric,
    is_transitive,
)

matrix1 = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
matrix2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
matrix3 = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
matrix4 = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
matrix5 = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]

assert not is_reflexive(matrix1)
assert is_symmetric(matrix1)
assert is_antisymmetric(matrix1)
assert is_transitive(matrix1)

assert is_reflexive(matrix2)
assert is_symmetric(matrix2)
assert is_antisymmetric(matrix2)
assert is_transitive(matrix2)

assert not is_reflexive(matrix3)
assert is_symmetric(matrix3)
assert not is_antisymmetric(matrix3)
assert not is_transitive(matrix3)

assert is_reflexive(matrix4)
assert not is_symmetric(matrix4)
assert is_antisymmetric(matrix4)
assert is_transitive(matrix4)

assert not is_reflexive(matrix5)
assert not is_symmetric(matrix5)
assert is_antisymmetric(matrix5)
assert not is_transitive(matrix5)
