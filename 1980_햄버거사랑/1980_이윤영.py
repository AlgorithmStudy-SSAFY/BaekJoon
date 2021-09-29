import sys
sys.stdin = open('input_1980.txt', 'r')

N, M, T = map(int,input().split())

hamburger = 0
coke = 0

while T >= N:
    if T % N == 0:
        hamburger += T // N
        break
    if T != M and T >= N :
        T -= N
        hamburger += 1
    elif T == M:
        T -= M
        hamburger += 1
if T % N != 0 and T % M != 0 and (T % N)%M != 0 and (T%M)%N != 0 and T != 0:
    coke = T
else:
    hamburger = 0
    if T % M == 0:
        hamburger += T//M
        coke = 0

print(f'{hamburger} {coke}')

# 더 작은수로 나누고, 몫이 햄버거.. 횟수만큼 햄버거 최대로 먹고 남은시간 콜라마신시간
# 나머지 버거를 먹을 수 있는지
#