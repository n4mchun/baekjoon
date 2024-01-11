M = int(input())
N = int(input())

table = [False,False] + [True]*(N-1)
primes=[]

for i in range(2,N+1):
    if table[i]:
        if i >= M:
            primes.append(i)
        for j in range(2*i, N+1, i):
            table[j] = False

if len(primes) < 1:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))