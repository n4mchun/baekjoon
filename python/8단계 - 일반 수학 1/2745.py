num, system = input().split()
system = int(system)

result = 0
for i, n in enumerate(num[::-1]):
    n = ord(n)
    if n >= 65:
        n -= 55
    else:
        n -= 48
    result += n * system**i
print(result)