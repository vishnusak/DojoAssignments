def check(arr):
    count = 0
    for val in arr:
        if val < 1:
            count += 1

    return count

def maxWater(arr):
    inp = map((lambda a: a), arr)
    wall = inp[0]
    sum = 0

    diff_arr = map((lambda a: (wall - a)), inp)

    while (len(diff_arr) > 1):
        if check(diff_arr) > 1:
            diff_arr.pop(0)
            inp.pop(0)

            while (diff_arr[0] > 0):
                sum += diff_arr[0]
                diff_arr.pop(0)
                inp.pop(0)

            wall = inp[0]
            diff_arr = map((lambda a: (wall - a)), inp)
        else:
            diff_arr = map((lambda a: (a - 1)), diff_arr)

    return sum

# myTerrace = [3,1,1,4,2]
myTerrace = [4,1,2,3,4,1,3,4]
myResult = maxWater(myTerrace)
print ("Terraces are {}").format(myTerrace)
print ("The maximum water stored is {} units").format(myResult)
