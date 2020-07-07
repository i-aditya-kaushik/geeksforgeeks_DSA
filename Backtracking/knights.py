import math
def solve(m, n):
    '''
    :param M: number of rows
    :param N: number of columns
    :return: total possibilities
    '''
    ans= (n*m-1)*n*m
    if(n>=1 and m>=2):
        ans-=(4*(n-1)*(m-2))
    if(n>=2 and m>=1):
        ans-=(4*(n-2)*(m-1))
    return int(ans%(math.pow(10,9)+7))
