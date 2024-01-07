origin = [1, 1, 2, 2, 2, 8]
pieces = list(map(int, input().split()))

for x, y in zip(origin, pieces):
    print(x - y, end=' ')