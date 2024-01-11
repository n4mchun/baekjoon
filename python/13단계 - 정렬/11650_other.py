# sort 메소드는 기본적으로 앞 순서부터 정렬을 해준다!
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()
for i in data:
    print(i[0], i[1])