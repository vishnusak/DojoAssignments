# String.concat
# string1.concat(str2,str3,...,strX)  - add string(s) to end of existing one. Return new string.
# steps:
# ---- concatination in python is also a simple "+". am using it
# the "*args" is how python handles variable number of arguments to a function
def concat(*strings):
    if (len(strings) == 0):
        return "nothing to concatenate"
    else:
        result = ''
        for each in strings:
            result += each
        return result

myStr1 = "this"
myStr2 = "is"
myStr3 = "yet"
myStr4 = "another"
myStr5 = "string"
print("The input strings are:")
print("'{}'").format(myStr1)
print("'{}'").format(myStr2)
print("'{}'").format(myStr3)
print("'{}'").format(myStr4)
print("'{}'").format(myStr5)

myResult = concat(myStr1, myStr2, myStr3, myStr4, myStr5)

print("The concatinated string is '{}'").format(myResult)
