# Acronyms
# Create a function that, given a string, returns the string's acronym (first letters only, capitalized). Given  " there's no free lunch - gotta pay yer way. " , return  "TNFL-GPYW" . Given  "Live from New York, it's Saturday Night!" , return  "LFNYISN" .
# steps:
# 1. strip blanks (as done above)
# 2. while stripping blanks store every char that comes immediately after a space into second string
# 3. use the .toUpperCase() on the second string and return
def acronym(string):
    result = ''
    for pos in range(len(string) - 1):
        if ((pos == 0) and (string[pos] != ' ')):
            result += string[pos]
        if ((string[pos] == ' ') and (string[pos + 1] != ' ')):
            result += string[pos + 1]

    return result.upper()

my_str = " there's no free lunch - gotta pay yer way. "
print ("The string is '{}'").format(my_str)

my_result = acronym(my_str)
print ("The acronym is {}").format(my_result)
