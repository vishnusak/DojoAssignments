# Create an algorithm that will output the fewest coins needed given an input value.
# For example:
# makeChange(.26) should output 1 quarter, 1 penny
# makeChange(.43) should output 1 quarter, 1 dime, 1 nickel, 3 pennies

# as seen in javascript, the same inconsistencies are present while doing subtraction on floats in python
# example: when we do (0.09 - 0.05), we expect 0.04. However, the system returns 0.039999999999999994. You can check this in the python console as well as in the browser console
# so providing the solution assuming that the maximum number of digits after the decimal in the input will be 2. (e.g., max value will be 0.99)
# lists make life a lot more easier here compared to dicts since the ordering of the key/value pairs internally is not maintained. But I am using dicts because I want to
def make_change(num):
    inp   = num * 100
    coins = {25:0, 10:0, 5:0, 1:0}
    denom = [25, 10, 5, 1]

    done  = 0
    idx   = 0

    while(not done):
        diff = inp - denom[idx]
        if (diff > 0):
            coins[denom[idx]] += 1
            inp = diff
        elif (diff == 0):
            coins[denom[idx]] += 1
            done = 1
        else:
            idx += 1

    return coins

# ==========================================================================

coin_names = {
              25:['quarter', 'quarters'],
              10:['dime', 'dimes'],
              5:['nickel', 'nickels'],
              1:['penny', 'pennies']
             }

my_val = 0.97

my_change = make_change(my_val)

key = my_change.keys()

output = ''

for i in range(len(key)):
    if (my_change[key[i]]):
        if (my_change[key[i]] > 1):
            output += "{} {} ".format(my_change[key[i]], coin_names[key[i]][1])
        else:
            output += "{} {} ".format(my_change[key[i]], coin_names[key[i]][0])

print "\nThe change for {} is {}".format(my_val, output)
