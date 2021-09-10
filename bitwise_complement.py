l=list(map(int,input().split()))
sum=0
for i in l:
    sum=sum+~i
if sum %10==0:
    print('YES')
else:
    print('NO')
