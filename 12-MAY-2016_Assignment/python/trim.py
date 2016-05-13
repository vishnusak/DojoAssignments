# String.trim
# string.trim()  - remove whitespace (spaces, tabs, newlines) from both sides, and return a new string.
# Example:  "\n hellogoodbye\t ".trim()  should return  "hellogoodbye" .
# steps:
# 1.find the position of first non-white space char and the last non-white space char.
# 2. then slice the string between these indices.
# 3. return the slice.
def trim(string):
    start = None
    end = None

    for idx in range(len(string)):
        if ord(string[idx]) in range(33, 133):
            start = idx
            break

    for idx in range(len(string) - 1, -1, -1):
        if ord(string[idx]) in range(33, 133):
            end = idx
            break

    return string[start:end+1]

myStr = "     \n hello good bye  \t      "
print("The string is '{}'").format(myStr)

myResult = trim(myStr)
print("The trimmed string is '{}'").format(myResult)
