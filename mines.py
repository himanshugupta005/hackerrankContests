r,c=map(int,input().split('x'))
count=0
for i in range(r):
    for j in range(c):
        if (i+j)%2!=0:
            count+=1
print(count)        