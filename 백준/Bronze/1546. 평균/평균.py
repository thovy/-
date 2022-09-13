n = input()
scoreList = list(map(int, input().split()))

maxScore = max(scoreList)
sumScore = sum(scoreList)

answer = (sumScore * 100 / maxScore / int(n))

print(answer)