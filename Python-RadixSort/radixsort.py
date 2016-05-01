# radix sort works on integers only
# It is non-comparative (no comparisons between elements of the list are done) and NOT in-place
# It works if range of integers in the list is known upfront. Otherwise it will go into an infinite loop

# Radix sort: (assume list has numbers from 0 to 10000 only. so max = 10000)
# 1 - start by creating a bucket (bkt) to hold the numbers. This will be an array of length 10 and will be empty at the beginning. each element of this bucket will also be an array.
# 2 - set divisor to 10. read the list of numbers to the sorted (arr) and get the MOD value for each number being read (arr[i] % 10)
# 3 - for the mod value from step-2, find the most significant digit (MSD). This will usually be available by dividing it by appropriate multiple of 10 and taking the quotient (e.g., for single digit numbers, divide by 1; for 2 digit numbers divide by 10; for three digit numbers divide by 100...)
# 4 - use this MSD as the index on the bucket and add the number to that bucket (bkt[MSD][x] = arr[i])
# 5 - after all the numbers are processed this way, replace the original list with the elements from the bucket in the order they are stored there.
# 6 - repeat steps 2 thru 6, each time multiplying the divisor by 10. The loop will end when the divisor becomes greater than to the range of numbers being sorted (e.g., for 5 digit numbers, range will be 100000)

import time
import random

def radix(arr,sort_range):
    bkt = [[], [], [], [], [], [], [], [], [], []]
    div_m = 10
    div_q = 1
    done = 0

    while (not done):
        for num in arr:
            digit = (num % div_m) / div_q
            bkt[digit].append(num)
        if (div_m > sort_range):
            done = 1
        else:
            # print bkt
            del arr[:]
            for i in bkt:
                for j in i:
                    arr.append(j)
            for i in bkt:
                del i[:]
            # print arr
            div_m *= 10
            div_q *= 10

my_arr = []

for i in range(100):
    my_arr.append(int(round(random.random() * 10000)))

start_time = time.clock()
radix(my_arr,10000)
end_time = time.clock()

print "Radix sort took {} secs\n".format(end_time - start_time)

print "The sorted array is \n {}".format(my_arr)
