import sys
input = sys.stdin.readline

# 주어지는 문자열 길이 S, 비밀번호로 사용할 길이 P
S, P = map(int, input().split())
# 문자열 words
words = str(input())
# 각 단어의 최소 필요 수
checkinglist = list(map(int, input().split()))

# S 에서 찾은 ACGT의 개수를 담을 리스트. checkinglist 와 비교될 예정
checkcount = [0] * 4
result = 0

# checkcount 와 checkinglist 의 비교에서 만족한 수
checktotal = 0

def countword(word):
    global checkinglist, checkcount, checktotal
    if word == "A":
        checkcount[0] += 1
            # >= 라고 하면 안됨. 그럼 다음 계산에서 count 가 커졌을 때도 checktotal의 값이 올라가게 됨
        if checkcount[0] == checkinglist[0]:
            checktotal += 1
    elif word == "C":
        checkcount[1] += 1
        if checkcount[1] == checkinglist[1]:
            checktotal += 1
    elif word == "G":
        checkcount[2] += 1
        if checkcount[2] == checkinglist[2]:
            checktotal += 1
    elif word == "T":
        checkcount[3] += 1
        if checkcount[3] == checkinglist[3]:
            checktotal += 1

def removeword(w):
    global checkinglist, checkcount, checktotal
    if w == "A":
        # 먼저 checktotal 을 빼줘야함.
        if checkcount[0] == checkinglist[0]:
            checktotal -= 1
        checkcount[0] -= 1
    elif w == "C":
        if checkcount[1] == checkinglist[1]:
            checktotal -= 1
        checkcount[1] -= 1
    elif w == "G":
        if checkcount[2] == checkinglist[2]:
            checktotal -= 1
        checkcount[2] -= 1
    elif w == "T":
        if checkcount[3] == checkinglist[3]:
            checktotal -= 1
        checkcount[3] -= 1

# 0 일수도 있으니, 0 인 부분은 미리 체크. + 할 때만 체크되는 함수들이므로
for i in range(4):
    if checkinglist[i] == 0:
        checktotal += 1

# 초기 P 탐색
for i in range(P):
    countword(words[i])

# 초기 P 탐색 후 result 에 입력
if checktotal == 4:
    result += 1
    
# 초기 P 만큼 탐색한 뒤 P 다음 글자부터 S 까지 탐색
for i in range(P, S):
    j = i - P
    countword(words[i])
    removeword(words[j])
    if checktotal == 4:
        result += 1
    

print(result)