ROW = 9

matrix = []
for i in range(ROW):
    matrix += [int(x) for x in input().split()]

max_value = max(matrix)
idx = matrix.index(max_value)

print(max_value)
print(idx // ROW + 1, idx % ROW + 1)