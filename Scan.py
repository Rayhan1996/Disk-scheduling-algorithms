f=[98,183,37,122,14,124,65,67]

n= int(input("Enter the Head of the Queue: "))

f.insert(0,n)

f.append(0)
ln= len(f)
print(ln)
f.sort()
idx=0
for i in range(ln):
    if f[i]==n:
        idx=i
        break

dm=[]
print("Path: ",end='')
for i in range(idx,-1,-1):
    print(f[i],end=" ")
    dm.append(f[i])
for i in range(idx+1,ln):
    print(f[i],end=" ")
    dm.append(f[i])

print()

temp = [ ]
for i in range(1,len(f)):
    print('abs({}-{})'.format(f[i],f[i-1]),end='+')
    temp.append(abs(f[i]-f[i-1]))

sum=0

for i in range(ln-1):

    temp= dm[i+1]-dm[i]
    if temp<0 :
        temp*=-1
    sum+=temp

print("\nTotal Distance is: ",sum)