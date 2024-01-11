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

print(int((n-2) * (n-1) * n / 6)) # nC3 -> 중복없이 뽑는 경우의 수
print(3)