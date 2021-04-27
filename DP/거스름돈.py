# https://programmers.co.kr/learn/courses/30/lessons/12907

n = 5
money = [1, 2, 5]

def solution(n, money):
    coinList = [0 for col in range(n)]
    money.sort()

    dp = [1 for col in range(n+1)]
    for j in range(1,n+1):
        if (j % money[0]):
            dp[j] = 0
    
    for i in range(1, len(money)):
        for j in range(money[i],n+1):
            dp[j] = dp[j] + dp[j-money[i]]

    answer = dp[-1]
    return answer % 1000000007

print(solution(n, money))