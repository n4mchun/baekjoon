N, M = map(int, input().split())
cards = [int(x) for x in input().split()]

min_diff = 300000
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = (cards[i] + cards[j] + cards[k])
            if total <= M and M-total < min_diff:
                min_diff = M-total
print(M-min_diff)