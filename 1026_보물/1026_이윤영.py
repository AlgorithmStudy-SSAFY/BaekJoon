import sys
sys.stdin = open('input_1026.txt', 'r')

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

A.sort() # 오름차순으로 정렬을 해서 가장 작은값과 B의 가장큰값이 서로 곱해지도록 배치한다.
B.sort(reverse=True)

s = 0

for i in range(N):
    s += A[i]*B[i]

print(s)