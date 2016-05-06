# Array: Rotate
# Implement  rotateArr(arr, shiftBy)  that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), change the array to [3,1,2]. Don't use built-in functions.
# Second: allow negative shiftBy (shift L, not R).
# Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
# Fourth: minimize the touches of each element.

# method-2 for rotateArr:
# this method decreases the number of touches on each element to 1 but doubles the memory requirement becasue we will use a temp array to handle the process

# steps:
# ---since length is a built-in function in python, I am not using it.
# ---since range is a built-in function in python, I am not using it.
# ---list.append is a built-in function in python. But unlike javascript, I couldn't find a way to avoid it. So using it.
# 1. here we simulate the traversal of a linked list.
# 2. when shiftby is to the right, (e.g., shiftBy = n), it means that the last 'n' elements of the array now become the first three elements. Similarly, when the shift is to the left, the first 'n' elements become the last 'n' elements.
# 3. find the index of the 'n'th element
# ------ for right shift, from the end (index = length of array - n)
# ------ for left shift, from the beginning (index = n)
# 4. now use this as the starting point and traverse the array
# 5. when the index reaches the last element, reset it to 0 and traverse the array till index identified in step 3
# 6. as we are doing steps 4 and 5, read each element and push it into a new array
# 7. At the end of the step 5, the new array will have the elements in the order we need. Return the new array

import random

def length(arr):
    done = False
    arr_len = 0
    temp = ''
    while (not done):
        try:
            temp = arr[arr_len]
            arr_len += 1
        except:
            done = True

    return arr_len

def arr_rotate(arr, shiftBy):
    arr_len = length(arr)
    temp    = []

    if ((shiftBy == 0) or (shiftBy == arr_len)):
        return

    if (shiftBy > 0):
        # while (shiftBy > arr_len):
        #     shiftBy = shiftBy - arr_len
        shiftBy = shiftBy % arr_len

        idx = 0
        pos = (arr_len - shiftBy)
        while (idx < arr_len):
            if (pos == arr_len):
                pos = 0
            temp.append(arr[pos])
            pos += 1
            idx += 1
    else:
        shiftBy = (-1 * shiftBy)
        # while (shiftBy > arr_len):
        #     shiftBy = shiftBy - arr_len
        shiftBy = shiftBy % arr_len

        idx = 0
        pos = shiftBy
        while (idx < arr_len):
            if (pos == arr_len):
                pos = 0
            temp.append(arr[pos])
            pos += 1
            idx += 1

    return temp

my_array = []
for i in range(10):
  my_array.append(int(random.random() * 100))

arr_shift = -4

print("The array is {} of length {}").format(my_array, len(my_array))
print("It has to be shifted by {}").format(arr_shift)

my_array = arr_rotate(my_array, arr_shift)

print("After shifting: {} of length {}").format(my_array, len(my_array))
