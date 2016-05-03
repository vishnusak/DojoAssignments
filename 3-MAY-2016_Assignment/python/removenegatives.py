# Remove negatives
# Implement removeNegatives() that accepts an array and removes any negative values.

# steps:
# 1. traverse array using loop
# 2. for each iteration, check the current value
# 3. if negative (< 0), remove element at that index and reduce iterator by 1
# 4. repeat step 3 till end of array
# the removal at specific index will be done using the remove() method
def rem_neg(arr):
    done = 0
    i    = 0

    while(not done):
        if (i == len(arr)):
            done = 1
        elif (arr[i] < 0):
            arr.remove(arr[i])
        else:
            i += 1

my_array = [1,-2,-3,-4,5,-6,7,-8,9,-10]
print("\nThe original array is {}\n").format(my_array)

rem_neg(my_array)

print("The array with negatives removed is {}").format(my_array)

# ============================================================================
