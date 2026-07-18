def solution(s):
    arr = s.split()
    
    num_list = []
    for i in arr:
        num_list.append(int(i))
    min_val = min(num_list)
    max_val = max(num_list)
    
    return (f"{min_val} {max_val}")