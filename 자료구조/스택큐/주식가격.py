# https://programmers.co.kr/learn/courses/30/lessons/42584


prices = [1, 2, 3, 2, 3]
def solution(prices):
    from collections import deque 

    answer = deque()
    time = 0
    stack = []
    stack.append([prices[-1], 0])
    answer.append(0)

    for i in range(len(prices)-2, -1, -1):
        time += 1

        # 스택을 덜어내는 경우
        while (stack and prices[i] <= stack[-1][0]):
            stack.pop()

        if (stack):
            answer.appendleft(time - stack[-1][1])
        else:
            answer.appendleft(time)
        stack.append([prices[i],time])

    return list(answer)

print(solution(prices))