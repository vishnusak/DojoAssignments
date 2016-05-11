# Integer to Roman Numerals
# Given a positive integer that is less than 4000, return a string containing that value in Roman numeral representation. In this representation:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000.
# Remember that 4 is IV, 349 is CCCXLIX and 444 is CDXLIV. -->

# steps:
# 0. store the above conversion (regular numbers <==> roman numbers) as an object. call this object S0.
# 1. seperate the numbers in individual digits and store them in an array.
# ---- The (index+1) will denote the position of the digit in the original number starting from the right
# 2. Now start processing from the last element of the above digit array
# 3. Each digit will be converted as follows-(digit * 10 ^(index+1)). This is X.
# ---- (e.g., for 349, the array will be [9,4,3]. for 483, the array will be[3,8,4]
# ---- in first array, 3 is at index 2 - will be processed as (3)*10^(3) = 300; X = 300
# ---- in 2nd array, 4 is at index 2 - will be processed as (4)* 10^(3) = 400; X = 400
# 4. for every X in step 3, identify where it falls between the numbers in S0. Let these numbers be A(greater than X) and B(less than X)
# ---- e.g.,in 349, for 300, we see it is between 500 and 100. So A = 500; B=100
# ---- e.g.,in 483, for 400, we see it is between 500 and 100. So A = 500; B=100
# 5. if (A - X) is also available in S0, then it will be C. Now step-7
# ---- if X = 400, then A - X will be 500 - 400 = 100. 100 is in S0, so C = 100.
# 6. if not step-5, then C will be the power of 10 used in step-3. We will go to step-8.
# ---- if X = 300, A - X is 500 - 300 = 200 which is not in S0. so C = 100
# 7. represent X as S0[C]+S0[A] in the result string
# ---- for X = 400, S0[100] + S0[500] => 'C'+'D'. so 400 = 'CD'
# 8. Find how many time X is divisible by C. Then represent X by that many Cs
# ---- X = 300; C = 100. So X is divisble by C 3 times. we know from S0 that 100 = 'C'. so 300 = 'CCC'.
# 9. repeat steps 3 thru 8 for every digit in the original number. return the result string.
def get_roman(num, idx):
    if (num == 0):
        return -1

    result = ''

    roman = {
    1000: 'M',
     500: 'D',
     100: 'C',
      50: 'L',
      10: 'X',
       5: 'V',
       1: 'I'
    }

    r_keys = sorted(roman.keys(), reverse=True)

    done = False
    for cur in range(len(r_keys)):
        if ((cur == 0) and (num > r_keys[cur])):
            for loop in range(num / r_keys[cur]):
                result += roman[r_keys[cur]]
            done = True
        elif (num == r_keys[cur]):
            result += roman[r_keys[cur]]
            done = True
        elif (num > r_keys[cur]):
            diff1 = r_keys[cur - 1] - num
            if (diff1 in r_keys):
                result += roman[diff1]
                result += roman[r_keys[cur-1]]
                done = True
            else:
                diff2 = num - r_keys[cur]
                div = 10**idx
                result += roman[r_keys[cur]]
                for loop in range(diff2 / div):
                    result += roman[div]
                done = True

        if (done):
            break

    return result

def roman(num):
    result = ''

    temp = num
    d_arr = []
    while (temp != 0):
        d_arr.append(temp % 10)
        temp = temp / 10

    for idx, digit in enumerate(d_arr):
        r_num = get_roman((digit * (10**idx)), idx)
        if (r_num != -1):
            result = r_num + result

    return result

my_num = 3450
print ("The number is {}").format(my_num)

my_result = roman(my_num)
print ("The roman number is {}").format(my_result)
