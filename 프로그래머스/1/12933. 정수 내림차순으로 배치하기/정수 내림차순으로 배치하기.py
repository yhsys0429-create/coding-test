def solution(n):
    n1 = sorted(str(n),reverse=True)
    return int("".join(n1))
    