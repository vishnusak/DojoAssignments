# Nth largest
# Given  arr  and  N , return the Nth-largest element, where (N-1) elements are larger. Return  null  if needed

# steps:
# -----This involves sorting. We can either use the in built array sort function to do it or write our own sort routine to do it (radix sort is already part of our curriculum!!!)
# -----I am using the built-in sorts for this.
# -----I am assuming all values are going to be unique (without repetitions). If this assumption is not valid, array traversal will be required to get the correct answer
# 1. if length of array less than N, return null. otherwise do the below
# 2. sort the array
# 2.a. use the reverse=True inside the sort to get it in descending order
# 3. if the order is ascending, return arr[-N]
# 3.a. if order is descending, return arr[N-1]
def nth_large(arr, pos):
    i = len(arr) - pos
    if (i < 0):
        return None
    else:
        # using the sorted(arr) function instead of the arr.sort() method since the former doesn't change the original array
        # unlike javascript, negative indices are supported here which helps us in traversing the array from right to left

        # ascending order, regular sort
        return sorted(arr)[pos * -1]

        # descending order, using lambda
        # return sorted(arr, key = lambda x: x * -1)[pos - 1]

        #descending order, using reverse=True
        # return sorted(arr, reverse = True)[pos - 1]

myArray = [1,2,45,65,85,43,98,76,32,12];
nth = 4;
print("The original array is {}").format(myArray)

nthLargeVal = nth_large(myArray, nth)

print("The {}th largest value in {} is {}").format(nth, myArray, nthLargeVal)
