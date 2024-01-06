n, m = map(int, input().split())

bucket_list = [x for x in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1; j -= 1
    
    bucket_list[i], bucket_list[j] = bucket_list[j], bucket_list[i]
[print(x, end=' ') for x in bucket_list]