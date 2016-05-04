# Array: Concat
# Replicate JavaScript's  concat() . Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.:  arrConcat( ['a','b'], [1,2] )  should return new array  ['a','b',1,2] .

# steps:
# 1. find the combined length (len(arr1) + len(arr2)). This will be the length of the new array
# 2. set up a loop from 0 to combined length - 1
# 3. inside the loop, read the first array and push the elements in to the result array (loop counter is the index for result array only.)
# 4. once the first array is done, read the second array and continue pushing into the result array
# 5. at the end of the loop, return the result array
import random

def arr_concat(arr1, arr2):
    arr_len = len(arr1) + len(arr2)
    result = []

    for resIdx in range(arr_len):
        if (resIdx < len(arr1)):
            result.append(arr1[resIdx])
        else:
            result.append(arr2[resIdx - len(arr1)])

    return result

my_array1 = []
for i in range(10):
  my_array1.append(int(random.random() * 24))

my_array2 = []
for i in range(13):
  my_array2.append(int(random.random() * 83))

print("The array1 is {} of length {}").format(my_array1, len(my_array1))
print("The array2 is {} of length {}").format(my_array2, len(my_array2))

my_array = arr_concat(my_array1, my_array2)

print("After concatenating: {} of length {}").format(my_array, len(my_array))
