def areIsomorphic(string1,string2):
    m = len(string1) 
    n = len(string2) 
    if m != n: 
        return False
    m1 = [-1] * 256 
    m2 = [-1] * 256 
    for i in range(n): 
        # print(m2)
        # print(m1)
        if m2[ord(string1[i])] == -1: 
            if m1[ord(string2[i])] == 1: 
                return 0
            m1[ord(string2[i])] = 1
            m2[ord(string1[i])] = string2[i] 
        elif m2[ord(string1[i])] != string2[i]: 
            return 0
    return 1
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(areIsomorphic(s,p)):
            print(1)
        else:
            print(0)