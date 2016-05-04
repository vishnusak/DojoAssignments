# Array: Filter Range
# Alan is good at breaking secret codes. One tool is to eliminate numbers he knows are outside a certain specific range. Given  array  and values  min  and  max , remove array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.

# steps:
# 1. traverse the array
# 2. for each element check if it is between min and max
# 3. if yes, replace with None
# ----- replacing with None for two reasons:
# ----- 1. this makes sure the other values are in the same spot always
# ----- 2. while processing the array, check we can check for type None and ignore the values.
# Can be done using pop() / remove()

import random

def filter(arr, min, max):
    if (min > max):
        min, max = max, min

    filter_range = range(min, max)

    for idx in range(len(arr)):
        if arr[idx] in filter_range:
            arr[idx] = None


my_array = []
for i in range(10):
  my_array.append(int(random.random() * 100))

range_min = 33
range_max = 45

print("The array is {} of length {}").format(my_array, len(my_array))
print("The range is {} - {}").format(range_min, range_max)

filter(my_array, range_min, range_max)

print("After filtering: {} of length {}").format(my_array, len(my_array))
