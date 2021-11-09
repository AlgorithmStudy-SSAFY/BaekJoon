import sys
sys.stdin = open('input_3584.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # 노드의 수
    TREE = [0] * (N+1)
    for i in range(N-1):
        parent, child = map(int,input().split())
        TREE[child] = parent
    # 테스트 케이스의 가장 마지막줄에 가장 가까운 공통 조상을 구할 두 노드가 주어짐
    A, B = map(int,input().split())

    A_list = [0, A]
    B_list = [0, B]

    while TREE[A]:
        A_list.append(TREE[A])
        A = TREE[A]

    while TREE[B]:
        B_list.append(TREE[B])
        B = TREE[B]

    cnt = 1

    while A_list[-cnt] == B_list[-cnt]:
        cnt += 1

    print(A_list[-cnt+1])
