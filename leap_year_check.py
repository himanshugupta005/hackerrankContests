y=int(input())
if(y==1900):
    print("False")
elif (y==2000):
    print("True")
else:
    if(y%4==0):
        print("True")
    else:
        print("False")