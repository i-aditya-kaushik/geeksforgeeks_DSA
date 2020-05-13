def func(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    print(len(l1.union(l2)))

n = int(input())
for x in range(n):
    ab = list(map(int,input().split()))
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    func(l1,l2)