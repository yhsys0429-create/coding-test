def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
        
    aver = answer / len(arr)
      
    return aver