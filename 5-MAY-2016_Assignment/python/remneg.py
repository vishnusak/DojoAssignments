# Remove negatives
# Implement  removeNegatives()  that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives' order. As always, do not use built-in array functions.
# Additional: Don't use nested loops
# steps:
# 1. traverse the array
# 2. for every element, check if it is negative.
# 3. if negative, replace with None
def remNeg(arr):
    for idx in range(len(arr)):
        if (arr[idx] < 0):
            arr[idx] = None

myArray = [1,-22,-45,-65,85,43,-98,76,-32,12];
print("The original array is {}").format(myArray)

remNeg(myArray)

print("The array with negatives removed is {}").format(myArray)
