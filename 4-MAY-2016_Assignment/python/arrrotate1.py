# Array: Rotate
# Implement  rotateArr(arr, shiftBy)  that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), change the array to [3,1,2]. Don't use built-in functions.
# Second: allow negative shiftBy (shift L, not R).
# Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
# Fourth: minimize the touches of each element.

# steps:
# 1. the shiftby will be the number of times the core logic will return
# 2. core logic handles shifting items by 1, either to right or left
# ---length is a built-in function in python, so not using it
# ---range is a built-in function in python, so not using it
# 3. for shifting:
# 4. save the value of the left or right most element (depending on a left or right shift)
# 5. using a for loop move the elements to the right or left by 1.
# 6. repeat steps 4 & 5 as many times as indicated by shiftBy

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
    temp    = ''

    if ((shiftBy == 0) or (shiftBy == arr_len)):
        return

    if (shiftBy > 0):
        # while (shiftBy > arr_len):
        #     shiftBy = shiftBy - arr_len
        shiftBy = shiftBy % arr_len

        loop = 1
        while (loop <= shiftBy):
            temp = arr[arr_len - 1]
            idx = arr_len - 1
            while (idx > 0):
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[0] = temp
            loop += 1
    else:
        shiftBy = (-1 * shiftBy)
        # while (shiftBy > arr_len):
        #     shiftBy = shiftBy - arr_len
        shiftBy = shiftBy % arr_len

        loop = 1
        while (loop <= shiftBy):
            temp = arr[0]
            idx = 0
            while (idx < (arr_len - 1)):
                arr[idx] = arr[idx + 1]
                idx += 1

            arr[arr_len - 1] = temp
            loop += 1

my_array = []
for i in range(10):
  my_array.append(int(random.random() * 100))

arr_shift = 4

print("The array is {} of length {}").format(my_array, len(my_array))
print("It has to be shifted by {}").format(arr_shift)

arr_rotate(my_array, arr_shift)

print("After shifting: {} of length {}").format(my_array, len(my_array))
