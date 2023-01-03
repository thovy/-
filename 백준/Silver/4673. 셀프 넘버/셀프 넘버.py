allNumList = set(range(1,10001))
dList = set()

for i in allNumList:
    for j in str(i):
        i += int(j)
    dList.add(i)

answer = sorted(allNumList - dList)
for a in answer:
    print(a)