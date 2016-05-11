# Coin Change with Object
# Given a number of U.S. cents, return the optimal configuration of coins, in an object.
# steps:
# ---- assuming that the valid coins are, 25, 10, 5 and 1
# ---- assuming that the input will be an integer and 1 <= input < 100
# 1. maintain the valid denoms in an array
# 2. initialize the result object
# 3. divide the input consecutively by the valid denoms, starting from the highest and going down.
# 4. for every valid denom, use the current as the key in the result object and the quotient from the division as its value
# 5. the dividend of every division op is the mod value from the previous op.
def makeChange(num):
    coins = {
               25: 0,
               10: 0,
                5: 0,
                1: 0
            }

    denom = [25, 10, 5, 1]

    temp = num

    for e in denom:
        coins[e] = temp / e
        temp = temp % e

    return coins

myCents = 63;
print("\nThe input is {} cents").format(myCents)

myResult = makeChange(myCents)
print("\nThe optimal number of coins for {} cents is {}\n").format(myCents, myResult)
