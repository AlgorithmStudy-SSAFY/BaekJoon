import sys
sys.stdin = open('input_1789.txt', 'r')

# 백준 1789 수들의합

S = int(input())
n = 1
sumV = 0

while True:
    sumV += n
    if sumV + n < S:
        n += 1
    else:
        break

print(n)

