'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

# 코드1 의 수행 횟수 : (n-2) * (n-1) * n / 6
# 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수 : (n-2) * (n-1) * n / 6 -> 3

n = int(input())

if n < 3:
    print(0)
else:
    res = [1]
    for i in range(3, n):
        res.append(res[-1] + i-1)
    print(sum(res))
print(3)