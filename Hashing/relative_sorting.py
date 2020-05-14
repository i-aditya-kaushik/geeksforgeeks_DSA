def func(a,b):
    for x in b:
        if x in a:
            for y in range(a.count(x)):
                print(x,end=" ")
                a.remove(x)
    a.sort()
    for x in a:
        print(x,end=" ")
    print()

for x in range(int(input())):
    l = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    func(a,b)