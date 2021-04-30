day = 6
k = 1
day = 6
k = 25


def solution(day, k):
    answer = []
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day += (k - 1)

    for month in months:
        curDay = day % 7 

        answer.append(1) if (curDay == 5 or curDay == 6) else answer.append(0)
    
        day += month

    return answer

print(solution(day, k))