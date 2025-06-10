arr = [2,3,4,5,6,7,10]

target = 11

left = 0

right = len(arr)-1

while (left<right):
    heap = arr[left] + arr[right]

    if heap == target:
        print( "Index : " , left , right)
        print ("Value : " ,arr[left] ,"+" ,arr[right] , "="  , arr[left] + arr[right])
        break
    elif heap < target:
        left = left +1
    else:
        right = right -1