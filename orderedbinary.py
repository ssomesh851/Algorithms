#ordered binary search

def ordersearch(olist,n):
    if len(olist) == 0:
        print('False')
    else:
        mid = len(olist)//2
        if olist[mid] == n:
            return Binarysearch(olist[:mid],n)

        else:
            return Binarysearch(olist[mid+1:],n)
        
        
                            
def Binarysearch(list,n):
    l = 0
    u = len(list)-1
    found = False
    while l<u and not found:
        mid = (l+u)//2
        if list[mid] == n:
            return True
        else:
            if list[mid]<n:
                l = mid-1
            else:
                u = mid+1
    return found
olist = [0,1,3,4,5,69,36,45]
n = 69
print(ordersearch([0,1,3,8,14,18,19,34,52], 3))

      

