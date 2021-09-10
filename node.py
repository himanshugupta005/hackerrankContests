st=input()
node=int(input())
rd=int(input())

out=(st[node:]+st[node:].replace(' ',''))*rd
print(*out)