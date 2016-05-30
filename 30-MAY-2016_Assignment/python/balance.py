# Array balance point
# Write a function that returns whether the given array has a balance point between indices, where one side's sum is equal to the other's. Example:  [1,2,3,4,10]  ->  true  (between indices 3 & 4), but  [1,2,4,2,1]  ->  false

def balance(arr):
    sum_arr = reduce((lambda x,y: x+y), arr)
    balanced = False
    sum = None
    for idx in range(len(arr)):
        sum = (sum + arr[idx] if (sum) else arr[idx])
        if ((sum * 2) == sum_arr):
            balanced = 'The array is balanced between indices {} and {}'.format(idx, idx+1)
            break
    return balanced

# myArr = [1,2,3,4,5,6,9]
# print("The array is {}").format(myArr)
# print("Checking it for balance")
# print("{}").format(balance(myArr))

# Balance Index
#
# Here, a balance point is on an index, not between indices. Return the balance index where sums are equal on either side (exclude its own value). Return  -1  if none exist. Ex.:  [- 2,5,7,0,3]  ->  2 , but  [9,9] -> -1 .

def balIdx(arr):
    sum_arr = reduce((lambda x,y: x+y), arr)
    balanced = -1
    sum = arr[0]

    for idx in range(1, len(arr)):
        if ((sum * 2) == (sum_arr - arr[idx])):
            balanced = idx
            break
        else:
            sum += arr[idx]
    return balanced

myArr = [20,4,5,6,9]
print("The array is {}").format(myArr)
print("Checking it for balance")
print("Balanced on index {}").format(balIdx(myArr))
