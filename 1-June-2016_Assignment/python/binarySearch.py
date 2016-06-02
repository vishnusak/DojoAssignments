# binary search

def binarySearch(arr, val):
    start = 0
    end = len(arr) - 1
    found = False
    pos = None

    if arr[start] == val:
        pos = start
    elif arr[end] == val:
        pos = end
    else:
        while ((end - start > 1) and (not found)):
            print ("start is {}").format(start)
            print ("end is {}").format(end)
            mid = start + (end - start)/2
            print ("mid is {}").format(mid)
            print ("mid value is {}").format(arr[mid])
            if (arr[mid] > val):
                print("mid greater than val")
                end = mid
            elif (arr[mid] < val):
                print("mid less than val")
                start = mid
            else:
                print("got it")
                found = True

        if found:
            pos = mid

    return pos

myArr = [1,2,4,5,6,7,8,9,13,15,23,34,41,58,65,72,83,96,99,100]
myVal = 73
myResult = binarySearch(myArr, myVal)

print("The array is {}").format(myArr)
print("The value searched is {}").format(myVal)
if myResult != None:
    print("{} is at index {}").format(myVal, myResult)
else:
    print("{} is not in the array").format(myVal)
