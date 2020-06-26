def func(num,i,l):
    l.append(l[i]+l[i-1])
    print(l[-1],end=" ")
    if(i!=num-1):
        func(num,i+1,l)

for x in range(int(input())):
    num = int(input())
    if(num==1):
        print(1)
        continue
    print(1,end=" ")
    l = [0,1]
    func(num,1,l)
    print()