# https://programmers.co.kr/learn/courses/30/lessons/42885

people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    from collections import deque 
    people.sort()
    people = deque(people)
    answer = 0
    while (people):
        boatWeight = 0
        while (True):
            if (people and boatWeight + people[-1] <= limit):
                boatWeight += people.pop()
            elif (people and boatWeight + people[0] <= limit):
                boatWeight += people.popleft()
            else:
                break
        answer += 1
            
    return answer

print(solution(people, limit))