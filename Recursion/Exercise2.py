def func(c,m):
    if(m>c):
        return
    else:
        print(str(m),end = " ")
        func(c,m+1)


func(int(input()),1)