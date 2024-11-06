def get_matrix(n, m, value):
    matrix = []

    for _ in range(n):
        row = []
        matrix.append(row)

        for _ in range(m):
            row.append(value)

    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print("result 1:")
print(result1)
print("\nresult 2:")
print(result2)
print("\nresult 3:")
print(result3)