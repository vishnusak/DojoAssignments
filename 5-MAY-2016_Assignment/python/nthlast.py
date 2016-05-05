# Nth-to-last
# Return the element that is N-from-array's-end. Given  ([5,2,3,6,4,9,7],3) , return  4 . If the array is too short, return  null .
# steps:
# 1. if length < N, return null
# 2. if length = N return the first element in the array
# 3. if length > N, return the length - N element
def nthLast(arr, pos):
    i = len(arr) - pos
    if (i == 0):
        return arr[0]
    elif (i < 0):
        return null
    else:
        return arr[i]

myArray = [1,2,45,65,85,43,98,76,32,12];
nth = 4;
print("The original array is {}").format(myArray)

nthLastVal = nthLast(myArray, nth)

print("The value of the {}th last element in {} is {}").format(nth, myArray, nthLastVal)
