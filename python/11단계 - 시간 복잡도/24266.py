'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

# 코드1 의 수행 횟수 : n**3
# 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수 : n**3 -> 3

n = int(input())
print(pow(n, 3))
print(3)