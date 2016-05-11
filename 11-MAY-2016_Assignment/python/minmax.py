# Max/Min/Average with Object
# Given an array, return an object containing the array's max, min and average values.
def obj(arr):
    return {"avg": reduce(lambda x,y: x+y, arr)/len(arr),
            "max": max(arr),
            "min": min(arr)}

myArr = [1,2,3,4,5,6,7,8,9]
print("\nThe array is {}\n").format(myArr)

myResult = obj(myArr)

print("The object returned is {}\n").format(myResult)
