# Remove At
# Given array and an index into array, remove and return the array value at that index. Do this without using built-in array methods except  pop() . Think of  PopFront(arr)  as equivalent to  RemoveAt(arr,0) .

# steps:
# 1 - assign value of required index to the return variable
# 2 - move all elements from that index to last 1 spot to the left
# 3 - remove the last element of the array
# can be done using the built-in function remove(element)
def removeAt(arr, idx):
    val = arr[idx]

    for i in range(idx, (len(arr) - 1)):
        arr[i] = arr[i+1]

    arr.remove(arr[-1])
    return val

my_array = [1,2,3,4,5,6,7,8,9]
index    = 4

print("\nThe existing array is {}").format(my_array)
print("The length of existing array is {}").format(len(my_array))
print("The index at which value should be removed is {}\n").format(index)

removed_val = removeAt(my_array, index)

print("The removed value is {}").format(removed_val)
print("The array after removing the value is {}").format(my_array)
print("The length of array now is {}").format(len(my_array))
