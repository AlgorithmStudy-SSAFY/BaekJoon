# 백준 1789. 수들의 합

S = int(input()) # 서로 다른 N개의 자연수의 합

total = 0
i = 1
while total <= S:
    i += 1
    total += i

print(i-1)