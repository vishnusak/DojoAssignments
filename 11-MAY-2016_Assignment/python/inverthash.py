# Invert Hash
# Associative arrays are also called hashes. Build invertHash(assocArr) to convert hash keys to values, and values to keys. Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high": "charm", "dicey": "morals"}.
# steps:
# 1. break the hash into two array and use the zip function from above to put them back together in the order we need
# ---- use the built-in dict.keys() and dict.values() functions to split
# ---- use the zipit module for putting them back into a dict
import zipit as z

def invert(hash):
    return z.zipit(hash.values(), hash.keys())

myHash = {"name": "Zaphod", "charm": "high", "morals": "dicey"}

print("\nThe initial hash is {}\n").format(myHash)

myResult = invert(myHash)

print("The inverted hash is {}\n").format(myResult)
