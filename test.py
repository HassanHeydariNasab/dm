from matrix import Matrix

m1 = Matrix(
    [
        [False, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
    ]
)
m2 = Matrix(
    [
        [True, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
    ]
)
m3 = Matrix(
    [
        [False, True, False, False],
        [True, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
    ]
)
m4 = Matrix(
    [
        [True, True, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
    ]
)
m5 = Matrix(
    [
        [False, True, False, False],
        [False, False, True, False],
        [True, False, False, False],
        [False, False, False, True],
    ]
)
m6 = Matrix(
    [
        [False, True, False, False],
        [False, False, True, False],
        [True, False, False, False],
        [False, False, False, True],
    ]
)
m7 = Matrix(
    [
        [False, False, True, False],
        [True, False, False, False],
        [False, False, False, True],
    ]
)

assert not m1.is_reflexive()
assert m1.is_symmetric()
assert m1.is_antisymmetric()
assert m1.is_transitive()
assert m1 == m1
assert m5 == m6
assert m6 != m7
assert (m1 * True) == m1
assert m1 * m1 == m1
assert m2 * m2 == m2
assert m3 * m3 == Matrix(
    [
        [True, True, False, False],
        [True, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
    ]
)
try:
    result = m6 * m7
    assert False
except ArithmeticError:
    assert True
except Exception:
    assert False

assert m2.is_reflexive()
assert m2.is_symmetric()
assert m2.is_antisymmetric()
assert m2.is_transitive()

assert not m3.is_reflexive()
assert m3.is_symmetric()
assert not m3.is_antisymmetric()
assert not m3.is_transitive()

assert m4.is_reflexive()
assert not m4.is_symmetric()
assert m4.is_antisymmetric()
assert m4.is_transitive()

assert not m5.is_reflexive()
assert not m5.is_symmetric()
assert m5.is_antisymmetric()
assert not m5.is_transitive()
