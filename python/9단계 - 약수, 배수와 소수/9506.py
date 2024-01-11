while True:
    N = int(input())

    if N == -1:
        break

    divisor = []
    for i in range(1, int(N**(1/2)) + 1):
        if N % i == 0:
            divisor.append(i)
            if N//i not in divisor:
                divisor.append(N//i)

    divisor = sorted(divisor)[:-1]

    if sum(divisor) == N:
        print(f'{N} = {" + ".join([str(x) for x in divisor])}')
    else:
        print(f'{N} is NOT perfect.')