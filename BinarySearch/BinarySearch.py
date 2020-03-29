def Binary_search(A,start,end,item):
    if(start <= end ):
        mid = int((start+end)/2)
        if A[mid]==item:
            return mid
        elif A[mid]>item:
            return Binary_search(A,start,mid-1,item)
        else :
            return Binary_search(A,mid+1,end,item)
    return -1                

li = [1,2,14,25,46,67,80,100] 
yes = int(input("Enter item"))
index = Binary_search(li,0,len(li)-1,yes)  
print(index)