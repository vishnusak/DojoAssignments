# Remove array
# Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array). Given  ([20,30,40,50,60,70],2,4) , change to  [20,30,70]  and return it.

# simply going to use built in functions
# I guess I am running out of patience
def remArr(arr, start, end):
    del arr[start:end+1]

myArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

range_start = 3
range_end = 6

print("The array is {}").format(myArray)
print("The range is {} - {}").format(range_start, range_end)

remArr(myArray, range_start, range_end)

print("The modified array is {}").format(myArray)
