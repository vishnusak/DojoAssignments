# Is Palindrome
# Strings like "Able was I, ere I saw Elba" or "Madam, I'm Adam" could be considered palindromes, because (if we ignore spaces, punctuation and capitalization) the letters are the same from back to front. Create a function that returns a boolean indicating whether the string is a strict palindrome. For  "a x a"  or  "racecar" , return  true . Do not ignore spaces, punctuation and capitalization: if given  "Dud"  or  "oho!" , return  false .
# ---- Next, ignore white space (spaces, tabs, returns), capitalization and punctuation.
# steps:
# 1. start reading the string char by char from both ends
# 2. compare the chars. If they are equal, palindrome, otherwise not-palindrome
def palin(string):
    rev_pos = len(string) - 1
    for pos in range(len(string) / 2):
        if (string[pos] != string[rev_pos - pos]):
            return False
    else:
        return True

# steps:
# ---- same steps as above. But before that we strip every non-alphabet from it
# 'a' = 97, 'z' = 122
# 1. start reading the string char by char from both ends
# 2. compare the chars. If they are equal, palindrome, otherwise not-palindrome

def palin2(string):
    newStr = ''
    for char in string:
        if ord(char.lower()) in range(ord('a'), ord('z')+1):
            newStr += char.lower()

    return palin(newStr)

# myStr = "Able was I, ere I saw Elba"
# myStr = "Madam, I'm Adam"
myStr = "racecar"
print("The string is '{}'").format(myStr)

myResult = palin(myStr)
output1 = "According to first method: "

myResult2 = palin2(myStr)
output2 = "According to second method: "

if (myResult):
  output1 += "It's a Palindrome"
else:
  output1 += "It's not a Palindrome"

if (myResult2):
    output2 += "It's a Palindrome"
else:
    output2 += "It's not a Palindrome"

print("{}").format(output1)
print("{}").format(output2)
