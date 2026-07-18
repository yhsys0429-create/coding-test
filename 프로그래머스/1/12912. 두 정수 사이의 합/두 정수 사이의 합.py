def solution(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    if a == b:
        return a or b
    answer = 0
    if a < b:
        for i in range(a,b+1):
            answer += i
    return answer        