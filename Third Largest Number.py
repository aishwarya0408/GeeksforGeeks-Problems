


def thirdLargest(arr, n):
    if(n<3):
        return(-1)
    else:
        arr=sorted(arr)
        return(arr[n-3])
m=int(input("Enter the size of array:"))
print("Enter the array:")
a=list(map(int,input().split()))
thirdLargest(a,m)





