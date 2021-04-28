# https://programmers.co.kr/learn/courses/30/lessons/42587

priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    from collections import deque 
    readyQ = priorities[:]
    readyQ.sort(reverse=True)
    readyQ = deque(readyQ)
    
    maxPri = 0
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]
    
    priorities = deque(priorities)
    answer = 0
    while (priorities):
        tmp = priorities.popleft()
        if (tmp[0] == readyQ[0]):
            readyQ.popleft()
            answer += 1
            if (tmp[1] == location): return answer
        else:
            priorities.append(tmp)
        
    return 




print( solution(priorities, location))