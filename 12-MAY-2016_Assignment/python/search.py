# String.search
# string.search(val)  - search string for val (another string). Return index position of first match ( -1  if not found).
# ---- Bonus: Implement regular expression support
def search(string, val):
    val = str(val)  #convert the to-be-searched string into a string type

    if (len(val) == 0): #if the to-be-searched is an empty string, return 0
        return 0
    elif (len(val) == 1): #the to-be-searched is a single char.
        for char_idx in range(len(string)):
            if (string[char_idx] == val):
                return char_idx
        else:
            return -1
    else:  #the to-be-searched is a string on length > 1
        for char_idx in range(len(string) - len(val) + 1):
            if (string[char_idx:len(val)+1] == val):
                return char_idx
        else:
            return -1

myStr = "this is yet a34n 2other     !str1ng"
mySearchStr = 1

print("\nThe string is '{}'").format(myStr)
print("The search string is '{}'\n").format(mySearchStr)

myResult = search(myStr, mySearchStr)

if (myResult == -1):
  print("The '{}' is not found in '{}'\n").format(mySearchStr, myStr)
else:
  print("The string '{}' is found at index {}\n").format(mySearchStr, myResult)
