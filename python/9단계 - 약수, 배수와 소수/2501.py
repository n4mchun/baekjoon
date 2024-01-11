N, K = map(int, input().split())

divisor = []
for i in range(1, int(N**(1/2)) + 1):
    if N % i == 0:
        divisor.append(i)
        if N//i not in divisor:
            divisor.append(N//i)

if len(divisor) < K:
    print(0)
else:
    print(sorted(divisor)[K-1])