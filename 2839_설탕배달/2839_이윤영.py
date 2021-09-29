import sys
sys.stdin = open('input_2839.txt', 'r')

# 백준 2839 브론즈1 설탕배달

TC = int(input())

for test_case in range(1, TC+1):
    SUGAR = int(input())

    # if 만약에 5kg로 나눴는데 나머지가 3으로 나눠떨어지는 경우:
        # 5kg 나눈 cnt 세고
        # 5kg의 나머지 나누기 3한 cnt도 세서
        # 둘을 합친다.
    # else: 5kg로 나눈 나머지가 3으로 나눠떨어지지않는 경우
        # if 3kg으로 나눴을때 나머지가 0인경우
        # else: 0이 아닌경우 -1 출력
SUGAR = int(input())
cnt = 0

if (SUGAR%5)%3 == 0:
    cnt += (SUGAR//5)
    cnt += (SUGAR%5)//3
elif (SUGAR%5)%3 != 0:
    for i in range((SUGAR//5),0,-1):
        if (SUGAR-(5*i))%3 == 0:
            cnt += i
            cnt += (SUGAR-(5*i))//3
            break
    else:
        cnt = -1
    if cnt == -1 and SUGAR % 3 == 0:
        cnt += (SUGAR // 3)+1

print(cnt)