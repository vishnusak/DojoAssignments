# Double Trouble
# Create a function that changes a given array to list each existing element twice, retaining original order. Convert  [4,"Ulysses",42,false]  to  [4,4,"Ulysses","Ulysses",42,42,false,false] .
# steps:
# 1. slice the array from index 1 and store the slice.
# 2. remove all elements from array except first
# 3. append the same element into array
# 4. for every element in the slice, append it to array twice.
def double(arr):
    slc = arr[1:]
    del arr[1:]
    arr.append(arr[0])

    for element in slc:
        arr.append(element)
        arr.append(element)

myArray = [4,"Ulysses",42,False]

print("The array is {}").format(myArray)

double(myArray)

print("The doubled array is {}").format(myArray)
