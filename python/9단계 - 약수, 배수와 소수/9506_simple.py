while True:
    N = int(input())

    if N == -1:
        break

    divisor = []
    for i in range(1, N):
        if N % i == 0:
            divisor.append(i)

    if sum(divisor) == N:
        print(f'{N} = {" + ".join([str(x) for x in divisor])}')
    else:
        print(f'{N} is NOT perfect.')