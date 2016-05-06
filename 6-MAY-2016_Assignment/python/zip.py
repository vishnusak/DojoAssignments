# Zip it
# Create a standalone function that accepts two arrays and combines their values sequentially into the first array, at alternating indices starting with the first array. Extra values from either array should be included afterward. Given  [1,2]  and  [10,20,30,40] , change first array to  [1,10,2,20,30,40] .
#
# steps:
# 1. slice the first array after the first element and save it
# 2. starting with the second array, alternatively push a single element of second array and sliced array into array 1.
# 3. When one of the arrays is empty (slice or second array), push the remaining elements of the remaining array into array 1
# can be done using the splice function.
def zip(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    if (len1 <= len2):
        length = len1 - 1
    else:
        length = len2

    slc = arr1[1:]
    del arr1[1:]

    index = 0
    for idx in range(length):
        arr1.append(arr2[idx])
        arr1.append(slc[idx])
        index += 1

    if (len1 <= len2):
        for idx in range(index, len(arr2)):
            arr1.append(arr2[idx])
    else:
        for idx in range(index, len(slc)):
            arr1.append(slc[idx])

myArray1 = [1,2,3,4,5]
myArray2 = [10,20,30]

print("The first array is {}").format(myArray1)
print("The second array is {}").format(myArray2)

zip(myArray1, myArray2)

print("The zipped array is {}").format(myArray1)
