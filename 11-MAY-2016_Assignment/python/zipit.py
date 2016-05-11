# Zip Arrays into Map
# Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.
# steps:
# 1. read both arrays in the same loop.
# 2. for every iteration, combine the two elements and add to the hash
# ---- can be done using the built-in "zip" and "dict" functions
def zipit(arr1, arr2):
    return dict(zip(arr1, arr2))

if __name__ == "__main__":
    myArr1 = ["abc", 3, "yo"]
    myArr2 = [42, "wassup", True]
    print("The arrays are {} and {}").format(myArr1, myArr2)

    myResult = zipit(myArr1, myArr2)

    print("The zipped result is {}").format(myResult)
