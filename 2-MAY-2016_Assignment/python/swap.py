# Swap Array Pairs
# Swap positions of successive pairs of values of given array. If length is odd, do not change final element. For  [1,2,3,4] , return  [2,1,4,3] . For  [false,true,42] , return  [true,false,42] .

# steps:
# 1 - traverse array in for loop
# 2 - increment counter by 2 each time instead of one
# 3 - for every run of the loop, swap a[i] and a[i+1]
# 4 - run loop till counter is less than length-1
# I couldn't find any built-in function to swap variable values in python
def arrSwap(arr):
    for i in range(0, (len(arr) - 1), 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

my_array = [1,2,3,4,5,6,7,8,9]

print("\nThe existing array is {}\n").format(my_array)

arrSwap(my_array)

print("The array after swapping is {}").format(my_array)
