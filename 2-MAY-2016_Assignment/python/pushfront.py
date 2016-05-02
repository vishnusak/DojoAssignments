# Push Front
# Given array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

# steps:
# 1 - increase the size of the array by 1
# 2 - move all existing values 1 place to the right.
# 3 - assign the new value to the first element
# can be done using the built-in function insert(index, list)
def pushfront(arr, val):
    arr.append('')                  # increase the size of array by 1
    i = -1

    while (i > (-1 * len(arr))):    # move existing elements 1 spot to the right
        arr[i] = arr[i-1]
        i -= 1

    arr[0] = val                    # assign the new value to the 1st element

array = [1,2,3,4,5,6,7,8,9]
new_val = 0

print("The existing array is {}").format(array)
print("The new value to be pushed in front is {}").format(new_val)

pushfront(array, new_val)

print("The array after pushing in the new value is {}").format(array)
