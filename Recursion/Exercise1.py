def func(c):
    if(c<1):
        return
    else:
        print(str(c),end = " ")
        func(c-1)


func(int(input()))