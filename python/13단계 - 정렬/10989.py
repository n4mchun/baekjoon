# 메모리 초과: 10,000,000개의 원소로 정렬 -> 카운팅 정렬 사용
from sys import stdin

N = int(stdin.readline()[:-1])
table = [0] * 10001

for _ in range(N):
    table[int(stdin.readline()[:-1])] += 1

for idx, x in enumerate(table):
    if x:
        for i in range(x):
            print(idx)