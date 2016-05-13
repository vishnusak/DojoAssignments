# String.slice
# string.slice(start,end)  - extract part of a string and return in a new one. Start and end are indices into the string, with the first character at index 0. End param is optional and, if present, refers to one beyond the last character to include.
# --Bonus: include support for negative indices, representing offsets from string-end. Example:  string.slice(-1)  returns the string's last character.
# steps:
# 1. read the string character by char using the index
# 2. when the index = start index, start copying it into new string.
# 3. do this till index = stop index or end of string
# ---- assuming that if the start is negative, then the end is also negative
# ---- validations are not in place. so the below code will easily break (e.g., try using (4,0) as the range)
def slice(string, *idx):
    result = ''
    if (len(idx) == 0):
        result = string
    elif (len(idx) == 1):
        if (idx[0] >= 0):
            for i in range(idx[0], len(string)):
                result += string[i]
        else:
            for i in range(len(string) + idx[0], len(string)):
                result += string[i]
    else:
        if (idx[0] >= 0):
            for i in range(idx[0], idx[1]):
                result += string[i]
        else:
            for i in range(len(string) + idx[0], len(string) + idx[1]):
                result += string[i]

    return result

myStr = "thisisyetanotherstring"
print("The string is '{}'").format(myStr)
myStart = 8
myEnd   = 0

myResult = slice(myStr, myStart)

print("The sliced string ({}, {}) is {}").format(myStart, myEnd, myResult)
