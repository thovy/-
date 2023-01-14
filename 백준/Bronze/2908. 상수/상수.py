A, B = map(str, input().split())

index=2
answer=''
while(index >= 0):
    if A[index] == B[index]:
        index-=1
        continue
    elif A[index] > B[index]:
        answer=A[2]+A[1]+A[0]
        break;
    elif A[index] < B[index]:
        answer=B[2]+B[1]+B[0]
        break;
    else:
        break;
        
print(answer)