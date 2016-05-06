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

# radix2 is the way where we don't need to input the range. the function figures it out on its own.
# what I claimed earlier - that it will go into an infinite loop if there is no range specified, is obviously wrong

# Radix sort: (assume list has integers >= 0)
# 1 - start by creating a bucket (bkt) to hold the numbers. This will be an array of length 10 and will be empty at the beginning. each element of this bucket will also be an array.
# 2 - start with a divisor of 10. read the list of numbers to be sorted (arr) and get the MOD value for each number being read (arr[i] % 10)
# 3 - for the mod value from step-2, find the most significant digit (MSD). This will usually be available by dividing it by appropriate multiple of 10 and taking the quotient (e.g., for single digit numbers, divide by 1; for 2 digit numbers divide by 10; for three digit numbers divide by 100...)
# 4 - use this MSD as the index on the bucket and add the number to that bucket (bkt[MSD][x] = arr[i])
# 5 - store the quotient from step-2 in an array.
# 6 - after all the numbers are processed this way, replace the original list with the elements from the bucket in the order they are stored there.
# 7 - repeat steps 2 thru 7, each time multiplying the divisor by 10. The loop will end when the quotient array from step-5 contains 0 in all elements

def radix2(arr):
    # the bucket list for storing values based on MSD
    bkt   = [[], [], [], [], [], [], [], [], [], []]

    # the quotient bucket for checking end of sort
    q_bkt = []

    # divisor to get the mod values from the input list elements
    div_m = 10

    # divisor to get the MSD of the mod value
    div_q = 1

    # flag to indicate end of the sort.
    # can be avoided but I find it more readable to see done / not done
    done  = False

    # start the iterations. continue till quotient list is all zeroes
    while (not done):

        # iterate over the input list. 'num' has the numbers from input list
        for num in arr:
            # for every 'num' the below will give us the individual digits starting from the right and moving left
            # to begin with div_m = 10 and div_q = 1. so we get the digit in the unit's place or one's place
            # in the next iteration of the WHILE loop, div_m = 100, div_q = 10 and we get the digit in the 10's place and so on till we get all the digits in subsequent while loops.
            digit = (num % div_m) / div_q

            # using the above digit as the index, add the number from input list into the appropriate buckect in the bucket list
            bkt[digit].append(num)

            # this will save the quotient of the division and store it in the quotient list. (e.g., if num = 123 and div_m = 100, num / div_m = 1; in the next iteration, div_m will be 1000 and num/div_m = 0. Similarly when quotient becomes 0 for all 'num', the sorting will stop)
            q_bkt.append(num / div_m)

        # after the for loop, empty the current list so that the bucket list can be copied into it
        del arr[:]

        # copy the elements from the bucket list to the current list
        # nested for loop here because bucket list is an array of arrays
        for i in bkt:
            for j in i:
                arr.append(j)

        # empty the bucket and get it ready for the next iteration
        for i in bkt:
            del i[:]

        # check if the quotient bucket has any non-zero values. the 'any' built-in function checks for any True value in a list and returns True if found. Since 0 is a falsey value in python, any(q_bkt) will be False when all values are 0 otherwise it will be True
        if (any(q_bkt)):
        # if atleast one value in quotient bucket is non-zero, it means sort has to continue. so reset the quotient bucket and increment the divisors.
            # empty the quotient bucket
            del q_bkt[:]

            # increment the divisors - multiply by 10
            div_m *= 10
            div_q *= 10
        else:
        # if all values in quotient bucket are zeros, sort is finished. stop the process
            done = True

my_arr = []

for i in range(2500):
    my_arr.append(int(round(random.random() * 10000)))

# test data
# my_arr = [5667, 3948, 2737, 6575, 9290, 6864, 9421, 75, 9182, 611, 7772, 9217, 3683, 9131, 8551, 9553, 6908, 3725, 6535, 3197, 3275, 3142, 5603, 5131, 5353]

print "\nThe unsorted array - 1 is \n{}".format(my_arr)

start_time = time.clock()
radix(my_arr,10000)
end_time = time.clock()

print "\nRadix sort - 1 took {} secs\n".format(end_time - start_time)

print "The sorted array is \n {}".format(my_arr)

my_arr2 = []

for i in range(2500):
    my_arr2.append(int(round(random.random() * 10000)))

# test data
# my_arr2 = [5667, 3948, 2737, 6575, 9290, 6864, 9421, 75, 9182, 611, 7772, 9217, 3683, 9131, 8551, 9553, 6908, 3725, 6535, 3197, 3275, 3142, 5603, 5131, 5353]

print "\nThe unsorted array - 2 is \n{}".format(my_arr2)

start_time2 = time.clock()
radix2(my_arr2)
end_time2 = time.clock()

print "\nRadix sort - 2 took {} secs\n".format(end_time2 - start_time2)

print "The sorted array is \n {}".format(my_arr2)
