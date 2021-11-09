import sys
sys.stdin = open('input_1003.txt', 'r')

# 시간초과
def fibo(n):
    global zero_cnt, one_cnt

    if n==0:
        zero_cnt += 1
        return 0
    elif n==1:
        one_cnt += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

TC = int(input())
for test_case in range(TC):
    N = int(input())
    zero_cnt = 0
    one_cnt = 0

    fibo(N)

    print(zero_cnt,one_cnt)


