a=input()
a=a.split(",")
b=""
c=0
d=0
for x in a :
    for y in a:
        if(y==x):
            c=c+1
        if(c>d):
            b=x
            d=c
        c=0
print(b)