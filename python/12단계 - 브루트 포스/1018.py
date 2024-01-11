N, M = map(int, input().split())

chess = [[x for x in input()] for _ in range(N)]
min_count = 999
for i in range(N-8+1):
    for j in range(M-8+1):
        count = [0, 0]
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0: # 이게 중요
                    if chess[a][b] != 'B':
                        count[0] += 1
                    if chess[a][b] != 'W':
                        count[1] += 1
                else:
                    if chess[a][b] != 'W':
                        count[0] += 1
                    if chess[a][b] != 'B':
                        count[1] += 1
        if min(count) < min_count:
            min_count = min(count)
print(min_count)