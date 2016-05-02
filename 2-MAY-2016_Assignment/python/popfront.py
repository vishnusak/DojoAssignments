# Pop Front
# Given array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except  pop() .

# steps:
# 1 - assign value of first element to the return variable
# 2 - move all elements from 2nd to last 1 spot to the left
# 3 - remove the last element of the array
# can be done using the built-in function pop() / remove()
def popFront(arr):
    val = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i+1]

    arr.remove(arr[-1])
    return val

my_array = [1,2,3,4,5,6,7,8,9]

print("\nThe existing array is {}").format(my_array)
print("The length of existing array is {}\n").format(len(my_array))

popped_val = popFront(my_array)

print("The popped value is {}\n").format(popped_val)
print("The array after popping the first value is {}").format(my_array)
print("The length of array now is {}\n").format(len(my_array))
