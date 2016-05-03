# Array Min to Front
# Given an array of comparable values, move the lowest element to the array's front, shifting backward elements that previously were ahead of it. Change [4,2,1,3,5] to [1,4,2,3,5].

# steps:
# 1. This is a bit similar to insertion sort but only for 1 element
# 2. first traverse the array to find the least element
# this can also be done using the "min(array)" method but it won't give us the position. to find the postion, we should then use array.index() function
# 3. when found, save the index of the least element and the value
# 4. now start loop from beginning of array till the index identified
# 5. for each iteration, move all elements 1 spot to the right
# 6. assign the least element to the first index
def min_to_front(arr):
    min = arr[0]
    minpos = 0
    for i in range(1, len(arr)):
        if (arr[i] < min):
            min = arr[i]
            minpos = i

    for i in range(minpos, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = min

my_array = [1,2,3,4,5,6,7,8,9,0]
print("The original array is {}").format(my_array)

min_to_front(my_array)

print("The array after moving min to front is {}").format(my_array)

# ============================================================================
