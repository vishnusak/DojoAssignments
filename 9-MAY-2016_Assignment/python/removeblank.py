# <!-- Remove blanks
# Create a function that, given a string, returns a string without blanks. Given " play that Funky Music ", returns a string containing "playthatFunkyMusic".
# steps:
# 1. read the string character by character.
# 2. add the character to another string if it is not blanks
# 3. return the second string
def rem_blank(string):
    result = ''
    for char in string:
        if (char != ' '):
            result += char

    return result

my_str = " there's no free lunch - gotta pay yer way. "
print ("The string is '{}'").format(my_str)

my_result = rem_blank(my_str)
print ("The string without spaces is '{}'").format(my_result)
