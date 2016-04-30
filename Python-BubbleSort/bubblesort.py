import time
import random

def bubble(arr):
    done = 0
    length = len(arr) - 1
    num_of_swaps = 0
    while (not done):
        for i in range(length):
            if arr[i] > arr[i+1]:
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                num_of_swaps += 1
        if ((num_of_swaps > 0) or (length == 1)):
            length -= 1
            num_of_swaps = 0
        else:
            done = 1


my_arr = []

for i in range(100):
    my_arr.append(int(round(random.random() * 10000)))

start_time = time.clock()
bubble(my_arr)
end_time = time.clock()

print "Bubble sort took {} secs".format(end_time - start_time)

print "The sorted array is \n {}".format(my_arr)
