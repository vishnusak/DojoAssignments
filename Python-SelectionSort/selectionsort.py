import time
import random

def selSort(arr):
    done = 0
    start = 0
    num_of_comps = 0
    num_of_swaps = 0

    while (not done):
        min_val = arr[start]
        min_pos = start
        for i in range(start,len(arr)):
            num_of_comps += 1
            if (min_val > arr[i]):
                min_val = arr[i]
                min_pos = i

        if (start < len(arr)-1):
            num_of_swaps += 1
            (arr[start], arr[min_pos]) = (arr[min_pos], arr[start])
            start += 1
        else:
            done = 1

    print "Number of swaps = {}".format(num_of_swaps)
    print "Number of comparisons = {}\n".format(num_of_comps)

def selSort2(arr):
    done = 0
    start = 0
    stop = len(arr) - 1
    num_of_comps = 0
    num_of_swaps = 0

    while (not done):
        min_val = arr[start]
        min_pos = start
        max_val = arr[stop]
        max_pos = stop
        for i in range(start,(stop + 1)):
            num_of_comps += 2
            if (min_val > arr[i]):
                min_val = arr[i]
                min_pos = i
            if (max_val < arr[i]):
                max_val = arr[i]
                max_pos = i

        if (start < stop):
            if (start == max_pos):
                temp = arr[start]
                arr[start] = arr[min_pos]
                arr[min_pos] = arr[stop]
                arr[stop] = temp
                num_of_swaps += 1
            else:
                num_of_swaps += 2
                (arr[start], arr[min_pos]) = (arr[min_pos], arr[start])
                (arr[stop], arr[max_pos]) = (arr[max_pos], arr[stop])

            start += 1
            stop -= 1
        else:
            done = 1

    print "Number of swaps = {}".format(num_of_swaps)
    print "Number of comparisons = {}\n".format(num_of_comps)

my_arr = []
my_arr2 = []

for i in range(100):
    my_arr.append(int(round(random.random() * 10000)))
    my_arr2.append(int(round(random.random() * 10000)))

start_time1 = time.clock()
selSort(my_arr)
end_time1 = time.clock()

start_time2 = time.clock()
selSort2(my_arr2)
end_time2 = time.clock()

print "Selection sort-1 took {} secs".format(end_time1 - start_time1)
print "The 1st sorted array is \n {}".format(my_arr)
print "\n"
print "Selection sort-2 took {} secs".format(end_time2 - start_time2)
print "The 2nd sorted array is \n {}".format(my_arr2)
