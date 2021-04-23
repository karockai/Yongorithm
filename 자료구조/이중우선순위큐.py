# https://programmers.co.kr/learn/courses/30/lessons/42628

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = 	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]

import heapq

cnt = 0
delList = []
# 1:++, 0:--
def countLen(flag):
    global cnt

    if (flag == True):
        cnt += 1
    else:
        cnt -= 1
    

def insert(maxHeap, minHeap, num):
    heapq.heappush(minHeap, num)
    heapq.heappush(maxHeap, -num)
    countLen(True)
    
    
# flag :: 1 => maxheap 삭제, -1 => minheap 삭제
def delHeap(maxHeap, minHeap, flag):
    if (cnt <= 0): return
    if (flag == 1):
        curNum = heapq.heappop(maxHeap) * (-1)
        tmpList = []
        while (True):
            tmpNum = heapq.heappop(minHeap)
            if (tmpNum == curNum):
                for i in tmpList:
                    heapq.heappush(minHeap, i)
                break
            tmpList.append(tmpNum)

    elif (flag == -1):
        curNum = heapq.heappop(minHeap) * (-1)
        tmpList = []
        while (True):
            tmpNum = heapq.heappop(maxHeap)
            if (tmpNum == curNum):
                for i in tmpList:
                    heapq.heappush(maxHeap, i)
                break
            tmpList.append(tmpNum)
    countLen(False)




def solution(operations):
    maxHeap = []
    minHeap = []
    
    for operation in operations:
        op = list(map(str,operation.split()))
        print('--------op:', op)
        print('max:', maxHeap)
        print('min:', minHeap)
        if (op[0] == 'I'):
            insert(maxHeap, minHeap, int(op[1]))
        elif (op[0] == 'D'):
            delHeap(maxHeap, minHeap, int(op[1]))
        else:
            print('ERROR')

        
    if (cnt <= 0): return [0,0]
    else: return [-maxHeap[0], minHeap[0]]

print(solution(operations))