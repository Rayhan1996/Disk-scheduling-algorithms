f=[98,183,37,122,14,124,65,67]

n= int(input("Enter the Head of the Queue: "))

f.insert(0,n)

f.append(0)
f.append(350)
ln= len(f)
print("lenth of list : ",ln)

f.sort()

idx=0
for i in range(ln):
    if f[i]==n:
        idx=i
        break

dm=[]
print("Path: ",end='')
for i in range(idx,ln):
    print(f[i],end=" ")
    dm.append(f[i])
for i in range(0,idx):
    print(f[i],end=" ")
    dm.append(f[i])

print()
sum=0

for i in range(ln-1):

    temp= dm[i+1]-dm[i]
    if temp<0 :
        temp*=-1
    sum+=temp



empty= []
for i in range(1,len(f)):
    print('abs({}-{})'.format(f[i],f[i-1]),end='+')
    empty.append(abs(f[i]-f[i-1]))

print("\nTotal Distance is: ",sum)