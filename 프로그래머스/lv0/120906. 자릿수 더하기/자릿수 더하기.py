def solution(n):
    answer = 0
    if n < 10:
        return n
    while n >= 10:
        answer += n % 10
        n = n // 10
    answer += n
    return answer