# https://programmers.co.kr/learn/courses/30/lessons/42578

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def makeHash(clothes):
    table = {}
    for clothe in clothes:
        if (not clothe[1] in table):
            table[clothe[1]] = []
        table[clothe[1]].append(clothe[0])
    return table

def pickClothes(table):
    answer = 1
    for value in table.values():
        length = len(value) + 1
        answer = answer*length

    return answer - 1

def solution(clothes):
    answer = 0
    table = makeHash(clothes)
    answer = pickClothes(table)
    return answer

print(solution(clothes))