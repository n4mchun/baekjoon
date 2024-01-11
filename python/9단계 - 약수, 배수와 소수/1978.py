_ = input()
nums = map(int, input().split())

prime_count = 0
for num in nums:
    if num == 1:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime_count += 1
print(prime_count)