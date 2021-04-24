# https://programmers.co.kr/learn/courses/30/lessons/12904


# s =	"abcdcba"
# s = "abacde"
s = "aaaaa"
s = "aaaa"

def oddSearch(letters, idx):
    length = 1
    lp = idx
    rp = idx
    lChk = True
    rChk = True
    while (0 < lp and rp < len(letters) - 1):
        lp -= 1
        rp += 1
        if (letters[lp] != letters[rp]):
            return length
        length += 2
    return length

# 짝수는 오른쪽부터 검사한다. 
def evenSearch(letters, idx):
    # 오른쪽 검사
    lp = idx
    rp = idx + 1
    length = 1

    if (letters[lp] != letters[rp]):
        return length
    length += 1
    while (0 < lp and rp < len(letters) - 1):
        lp -= 1
        rp += 1
        if (letters[lp] != letters[rp]):
            return length
        length += 2
    return length

def solution(s):
    letters = list(s)
    length = 1
    for i in range(0, len(letters)-1):
        length = max(length, oddSearch(letters, i), evenSearch(letters, i))

    return length

print(solution(s))