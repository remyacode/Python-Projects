def bs(arr,tar):
    b=arr[0]
    l=arr[len(arr)-1]
    

    while(b<=l):
        m=(b+l)//2
        if(arr[m]==tar):
            return m
        elif(tar<arr[m]):
            l=m-1
        else:
            b=m+1
print('2 is at index:   ',bs([1,2,3,4,5],2))