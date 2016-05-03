# Skyline Heights
# From lovely Burbank you have a breathtaking view of the Los Angeles skyline.
# Let's say you are given an array with heights of consecutive buildings,
# starting closest to you and extending directly away. Array [-1,7,3] would
# represent three buildings: first is actually out of view below street level,
# behind it is second at 7 stories high, third is 3 stories high (hidden behind
# the 7-story). You are situated at street level. Return array containing
# heights of buildings you can see, in order. Given [1,-1,7,3] return [1,7].

# steps:
# 1. since negative values are below street level, we can ignore them
# 2. start with the first positive value in the array. This is current.
# 3. Next find the next positive value in the array which is greater than current.
# 4. the newly identified value is now current.
# 5. repeat steps 3 and 4 till end of array
def heights(arr):
    visible = []
    for i in range(len(arr)):
        if (arr[i] > 0):
            if ((len(visible) == 0) or (arr[i] >= current)):
                visible.append(arr[i])
                current = arr[i]

    return visible

buildings = [-1,2,-2,4,3,-3,6,5,8,9,7,-7]
print("\nThe building list is {}\n").format(buildings)

my_view = heights(buildings)

print("My view is {}").format(my_view)

# ============================================================================
