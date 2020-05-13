def linearProbing( hash, hashSize, arr, sizeOfArray):
    for x in arr:
        if(arr.index(x)==sizeOfArray):
            break
        if(hash[x%hashSize]==-1):
            hash[x%hashSize] = x
        else:
            # print('Else')
            i= (x+1)%hashSize
            while(i!=x):
                # print(i)
                if(hash[i]==-1):
                    hash[i]=x
                    break
                else:
                    i=(i+1)%hashSize
                