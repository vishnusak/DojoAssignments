# Insert At
# Given array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. You can think of  PushFront(arr,val)  as equivalent to  InsertAt(arr,0,val) .

# steps:
# 1 - increase the size of the array by 1
# 2 - move all existing values from the index mentioned 1 place to the right.
# 3 - assign the new value to the index mentioned
# can be done using built-in function insert(index, list)
def insertAt(arr, idx, val):
    arr.append('')
    for i in range((len(arr) - 1), (idx - 1), -1):
        arr[i] = arr[i - 1]

    arr[idx] = val

my_array = [1,2,3,4,5,6,7,8,9]
new_val  = 0
index    = 4

print("\nThe existing array is {}").format(my_array)
print("The new value to be inserted is {}").format(new_val)
print("The index at which insertion should happen is {}\n").format(index)

insertAt(my_array, index, new_val)

print("The array after inserting the new value is {}").format(my_array)
