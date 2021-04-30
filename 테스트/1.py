numbers = [1]

def solution(numbers):
    table = {}
    answer = -1
    overHalf = len(numbers)//2
    if (len(numbers) == 1):return numbers[0]
    for number in numbers:
        if (number in table):
            table[number] += 1
            if (table[number] > overHalf): return number
        else:
            table[number] = 1
    
    return answer

print(solution(numbers))