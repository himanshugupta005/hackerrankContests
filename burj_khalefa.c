#include<stdio.h>

void main()
{
    int n;
    int num;
    int rem;
    long long binary=0;
    int temp=1;
    int lastnum;
    int num1;
    printf("enter the value");
    scanf("%d",&lastnum);
    for(num=0;num<=lastnum;num++)
    {
        binary=0;
        temp=1;
        num1=num;
        while(num1>0)
        {
            rem=num1%2;
            num1=num1/2;
            binary=binary+rem*temp;
            temp=temp*10;
        }
        printf("%ld\n",binary);
        }
}
    
    


