# Array Remove Duplicates
# Sara is looking to hire an awesome web developer and has received applications from various sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together.

# steps:
# 1 - traverse array
# 2 - compare current element with prev element.
# 3 - if equal, call the removeAt method to remove current element
# 4 - reset index to same value since the array would have changed
# 5 - if not equal, update the prev element with current element value
# we are not sorting because it is already sorted.
# can be done using the built-in method set()
def removeAt(arr, idx):
    val = arr[idx]

    for i in range(idx, (len(arr) - 1)):
        arr[i] = arr[i+1]

    arr.remove(arr[-1])
    return val

def remDups(arr):
    prev = arr[0]
    i    = 1

    while (i < len(arr)):
        if (arr[i] == prev):
            remove_val = removeAt(arr, i)
        else:
            prev = arr[i]
            i += 1

my_array = [0,1,1,1,2,2,3,4,5,5,5,5,6,7,7,8,9,9,9,9,9]

print("\nThe existing array is {}\n").format(my_array)

remDups(my_array)

print("The array after removing duplicates is {}").format(my_array)
