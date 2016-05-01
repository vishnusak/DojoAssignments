import time
import random

"""
Insertion Sort
-compare consecutive pairs of elements. start with 1 & 2
-if they are in order, move to the next pair - 2 & 3 - and so on
-at any point, if the pair is not in order (in pair (i,i+1) i+1 is less than i) then start comparing it down the order (with i-1, i-2 etc until 1) to find its correct spot.
-once the spot is found (e.g., correct position should be i-5) move everything from (i-5) till (i) one place to the right and insert (i+1) into i-5
-now continue from new i+1 (the pair will be (i+1,i+2))
-Repeat till (n-1,n)
"""

"""
this can be done using the list methods like list.insert() and list.remove() instead of doing the element swaps
"""

def insSort(arr):
    done = 0
    length = len(arr) - 1
    num_of_swaps = 0
    i = 0

    while (not done):
        if (arr[i] > arr[i+1]):
            cur = i+1
            prev = i
            while ((arr[cur] < arr[prev]) and (prev >= 0)):
                arr[cur], arr[prev] = arr[prev], arr[cur]
                cur -= 1
                prev -= 1
                num_of_swaps += 1
        if (i == length - 1):
            done = 1
        else:
            i += 1

my_arr = []

for i in range(100):
    my_arr.append(int(round(random.random() * 10000)))

start_time = time.clock()
insSort(my_arr)
end_time = time.clock()

print "Insertion sort took {} secs".format(end_time - start_time)

print "The sorted array is \n {}".format(my_arr)
