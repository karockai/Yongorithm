# https://programmers.co.kr/learn/courses/30/lessons/42586

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    from collections import deque 

    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while (progresses):
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        
        cnt = 0
        while (progresses and progresses[0] >= 100 ):
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        
        if (cnt): answer.append(cnt)
 
    return answer

print(solution(progresses, speeds))