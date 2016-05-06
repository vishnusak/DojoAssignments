# Intermediate Sums
# You will be given an array of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the array does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums. Given the array  [1,2,1,2,1,2,1,2,1,2,1,2,1,2] , change it to  [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6]

# steps:
# 1. traverse array
# 2. keep adding all the elements being read
# 3. maintain a counter to identify 10 elements. when counter = 10, insert the sum into array at the index+1 position. reset sum, reset counter and increment the traversal loop counter (this is to avoid the newly inserted sum from being processed in the next iteration)
# 4. continue steps 2 and 3 till end of array.
# 5. whatever is the value of sum at this point, insert it into arr (arr.push(sum))
def intersum(arr):
    elem_sum = 0
    counter = 0
    idx = 0
    done = False

    while (not done):
        elem_sum += arr[idx]
        idx += 1
        counter += 1
        if (counter == 10):
            arr.insert(idx, elem_sum)
            idx += 1
            elem_sum = 0
            counter = 0
        if (idx == len(arr)):
            done = True

    if (elem_sum > 0):
        arr.append(elem_sum)

myArray = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]

print("The input array is {}").format(myArray)

intersum(myArray)

print("The modified array is {}").format(myArray)
