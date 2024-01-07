n = int(input())

for i in range(n):
    repeat_size, st = input().split()

    for c in st:
        print(c * int(repeat_size), end='')
    print()