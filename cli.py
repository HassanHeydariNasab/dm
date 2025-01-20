from utils import input_matrix

m = input_matrix(True)

print(m.is_transitive())
print("tc", m.transitive_closure())
print("tc?", m.transitive_closure().is_transitive())
print("w", m.transitive_closure_using_warshall_alg())
print("w?", m.transitive_closure_using_warshall_alg().is_transitive())
# print(m**3, m * m * m)
