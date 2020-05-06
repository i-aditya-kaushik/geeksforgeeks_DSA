def josephus(n,k):
    if(n==1):
        return 1
    return (josephus(n - 1, k) + k-1) % n + 1
    


n = int(input())
k = int(input())
print(josephus(n,k))