n, x = map(int, input().split())
a = input().split()

[print(num, end=' ') for num in a if int(num) < x]