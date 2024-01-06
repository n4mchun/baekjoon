n, m = map(int, input().split())

bucket_list = [x for x in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    i-=1; j-=1

    temp = bucket_list[i:j+1][::-1]
    for idx, v in zip(range(i, j+1), temp):
        bucket_list[idx] = v
[print(x) for x in bucket_list]