dots = [[], []]
for _ in range(3):
    x, y = map(int, input().split())

    for idx, a in enumerate([x, y]):
        if a not in dots[idx]:
            dots[idx].append(a)
        else:
            dots[idx].remove(a)

for i in dots:
    print(i[0], end=' ')