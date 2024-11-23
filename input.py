from properties_of_relations import is_reflexive

matrix = []
longestRow = 0

while True:
    rowInput = input(f"Enter row {len(matrix)+1}: ")
    if rowInput == "":
        break
    row = [bool(s) for s in rowInput.split(" ")]
    if len(row) > longestRow:
        longestRow = len(row)
    matrix.append(row)

# fill short rows with zero
for row in matrix:
    if len(row) < longestRow:
        row += [False] * (longestRow - len(row))
while len(matrix) < longestRow:
    matrix.append([False] * longestRow)

print(matrix)
print("is_reflexive:", is_reflexive(matrix))
