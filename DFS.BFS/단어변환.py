begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    from collections import deque 

    answer = 0

    start = list(begin)
    end = list(target)
    nextWords = []

    for word in words:
        nextWords.append(list(word))
    
    readyQ = deque()
    readyQ.append(start)
    time = 0
    visited = [False for _ in nextWords]

    while (readyQ):
        
        for i in range(len(readyQ)):
            curWord = readyQ.popleft()

            # nextWord랑 한 글자만 다른지 비교한다.
            for idx, nextWord in enumerate(nextWords):
                if (visited[idx]): continue

                onlyOne = False
                isNext = False
                
                for j in range(len(nextWord)):
                    if (curWord[j] != nextWord[j]):
                        if (onlyOne):
                            onlyOne = False
                            isNext = False
                            break
                        else:
                            onlyOne = True
                            isNext = True
                
                if (isNext):
                    if (nextWord == end):
                        return time + 1
                    readyQ.append(nextWord)
                    visited[idx] = True
        time += 1
    return 0

print(solution(begin, target, words))