# https://programmers.co.kr/learn/courses/30/lessons/42842
brown = 24
yellow = 24


def getCandList(brown, yellow):
    sumColor = brown + yellow
    candList = []
    for col in range(3, (sumColor // 3) + 1):
        row = sumColor // col
        if (sumColor % col != 0): continue
        elif (col > row):break
        elif (brown != row * 2 + col * 2 - 4): continue
        return [row, col]
    return False

def solution(brown, yellow):
    return getCandList(brown, yellow)

print(solution(brown, yellow))