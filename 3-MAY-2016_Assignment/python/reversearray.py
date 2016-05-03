# Reverse array
# Given a numerical array, reverse the order of the values. The reversed array should have the same length, with existing elements moved to other indices so that the order of elements is reversed. Don't use a second array - move the  values around within the array that you are given.

# steps:
# 1. find length of the array
# 2. use a loop that iterates for exactly half the length (e.g., if len = 5, the iterator end condition will be < 2)
# 3. for every iteration swap a[i] with a[len-1-i]
# 4. print result
# can be done using the .reverse() built-in method
def rev_arr(arr):
    l_idx = (len(arr) - 1)

    for i in range((len(arr) / 2)):
        arr[i], arr[l_idx - i] = arr[l_idx - i], arr[i]

my_array = [1,2,3,4,5,6,7,8,9,0]
print("\nThe original array is {}\n").format(my_array)

rev_arr(my_array)

print("The reversed array is {}").format(my_array)

# ============================================================================
