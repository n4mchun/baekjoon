N = int(input())
sorted_data = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
for i in sorted_data:
    print(i[0], i[1])