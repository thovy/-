import sys
sys.stdin = open('input.txt')

def cal_digit(n):
    while len(n) > 1:
        answer = 0
        for i in n:
            answer += int(i)
        n = str(answer)
    return n

def superDigit(n, k):
    cn = cal_digit(n)

    result = cn * k

    if len(result) > 1:
        result = cal_digit(result)

    return result



n, k = map(str, input().split())

result = superDigit(n, int(k))

print(result)