# https://programmers.co.kr/learn/courses/30/lessons/42576

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    aDic = {}
    for parti in participant:
        if (parti in aDic):
            aDic[parti] += 1
        else:
            aDic[parti] = 1
    for comp in completion:
        aDic[comp] -= 1
        if (aDic[comp] == 0):
            del aDic[comp]
    answer = list(aDic.keys())[0]
    return answer

print(solution(participant, completion))