import sys
n = int(sys.stdin.readline())

a = [0]*n
for i in range(n):
    a[i] = int(sys.stdin.readline())

stack = []    # 수열을 보며 쌓을 스택
num = 1        # 우리가 수열을 보며 스택에 넣을 자연수의 시작
result = True    # 입력되는 수열 a 로 만드는 게 불가능 한 경우 No 를 인쇄해야함
answer = ""

# 현재 수열이 나태낸 수가 4 라면 스택에 num 을 차례로 1, 2, 3, 4 를 push 해야함.
for i in range(n):
    if a[i] >= num:    # 현재 수열이 나타내는 수가 넣은 수(num)보다 크다면 같아질 때까지 num 을 스택에 쌓기
        while a[i] >= num:
            stack.append(num)
            num += 1
            answer += "+\n"    # num 을 스택에 쌓으니 '+' 인쇄
        stack.pop()    # 같아지면 같아진 수열 값을 밖으로 빼내기
        answer += "-\n"
    else:    # 현재 수열이 나타내는 수가 넣은 수(num) 보다 작다면 작아질 때까지 pop() 꺼냄
        n = stack.pop()    # 빼낸 수를 n 이라고 하면
        if n > a[i]:    # 빼낸 수가 수열에서 나타내는 수보다 크다면. 엥 작으면...?
            print("NO")
            result = False
            break
        else:
            answer += "-\n"
if result:
    print(answer)