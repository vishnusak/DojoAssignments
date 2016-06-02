def find_missing(arr):
    missing = None

    # find the max value
    max = reduce((lambda a,b: (a if a > b else b)), arr)
    # find the min value
    min = reduce((lambda a,b: (a if a < b else b)), arr)

    # generate range of numbers between min and max and check which of them is missing in the array
    for i in range(min+1, max):
        if i not in arr:
            missing = i
            break

    return missing

myArr = [2,-4,0,-3,-2,1]
myArr = [5,2,7,8,4,9,3]
myArr = [3,0,1,2]
myArr = [3,0,1]
# myArr = [3,2,1]

myResult = find_missing(myArr)

print ("The array is {}").format(myArr)
if myResult == None:
    print ("There are no values missing in the array")
else:
    print("The missing value is {}").format(myResult)
