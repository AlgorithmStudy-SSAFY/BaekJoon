N = int(input())
lst = list(map(int, input().split()))

def find(a, h):      # 벌 위치, 꿀 위치
    res = 0
    if a<h:     # 벌, 꿀      3, 6
        for i in range(1, h-a+1):    # 4
            if not v[a+i]:
                res += lst[a+i]
    elif a>h:   # 꿀, 벌
        for i in range(h-a):
            if not v[a+i]:
                res += lst[a+i]


v = [0]*N       # 벌이 있으면 1
while True:
    for i in range(N):
        v[i] = 1
        for j in range(N):
            if not v[j]:
                v[j] = 1
            for h in range(N):
                if not v[h]:
                    find(i, h)
                    find(j, h)
