n, m = map(int, input().split())

bucket_list = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    
    for idx in range(i-1, j):
        bucket_list[idx] = k
[print(x, end=' ') for x in bucket_list]