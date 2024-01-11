# 시간 초과 : input() -> sys.stdin.readline()
from sys import stdin

N = int(stdin.readline()[:-1])
arr = [int(stdin.readline()[:-1]) for _ in range(N)]
[print(x) for x in sorted(arr)]