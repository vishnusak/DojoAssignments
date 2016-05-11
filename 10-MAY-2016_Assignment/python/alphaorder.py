# Is Word Alphabetical
# Nikki, a queen of gentle sarcasm, loves the word facetiously. Lance helpfully points out that it is the only known English word that contains all five vowels in alphabetical order, and it even has a 'y' on the end! Nikki takes a break from debugging to turn and give him an acid stare that could only be described as arsenious. Given a string, return a boolean indicating whether all letters contained in that string are in alphabetical order.

# steps:
# ---- ignoring capitalization.
# 1. start reading the string char by char
# 2. if current char is < previous char, return false. else return true
def order(string):
    newStr = ''
    for char in string:
        if ord(char.lower()) in range(ord('a'), ord('z')+1):
            newStr += char.lower()

    for pos in range(1, len(newStr)):
        if newStr[pos] < newStr[pos - 1]:
            return False
    else:
        return True

myStr = "Abcd efijkl nop st"
# myStr = "facetiously"
print("The string is '{}'").format(myStr)

myResult = order(myStr)

if (myResult):
  print("The alphabet is in order")
else:
  print("The alphabet is not in order")
