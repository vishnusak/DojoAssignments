# Shuffle
# Recreate the  shuffle(arr)  function built into JavaScript, to efficiently shuffle a given array's values. Work in-place, of course. Do you need to return anything from your function?
#
# steps:
# ---- make use of the random number generator
# ---- genrate random numbers less than array length
# ---- python has a shuffle() function to do this
# 1. traverse the array in the regular way
# 2. for each stop in the iteration, generate a random number less than array length.
# 3. use the random number from step 2 as target index.
# 4. swap values of current index with target index
# 5. steps 2 thru 4 happe in place, so no need to return anything. The input array will be shuffled
import random as rd

def shufflearr(arr):
    for idx in range(len(arr)):
        newidx = int(round(rd.random() * len(arr)))
        arr[idx], arr[newidx] = arr[newidx], arr[idx]

myArray = []
for i in range(10):
  myArray.append(int(round(rd.random() * 1000)))

print("The input array is {}").format(myArray)

shufflearr(myArray)

print("The shuffled array is {}").format(myArray)
