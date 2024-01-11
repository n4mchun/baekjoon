N = int(input())

for i in range(1, N):
    if i + sum([int(x) for x in str(i)]) == N:
        print(i)
        break
else:
    print(0)