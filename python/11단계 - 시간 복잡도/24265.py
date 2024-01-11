'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

# 코드1 의 수행 횟수 : ((n-1)*n)//2
# 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수 : (n**2 - n) // 2 -> 2

n = int(input())
print(((n-1)*n)//2)
print(2)