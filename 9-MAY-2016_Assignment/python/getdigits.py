# Get digits
# Create a JavaScript function that, given a string, returns the integer made from the string's digits. Given  "0s1a3y5w7h9a2t4?6!8?0" , the function should return the number  1,357,924,680
# steps:
# 1. traverse the string char by character
# 2. For each char, Convert it to number and if it is not NaN, add it to second string.
# 3. finally, convert the second string into number and return
def get_digits(string):
    result = ''
    for char in string:
        try:
            num = int(char)
        except:
            num = -1

        if (num != -1):
            result += char 

    return int(result)

my_str = "0s1a3y5w7h9a2t4?6!8?0"
print ("The string is '{}'").format(my_str)

my_result = get_digits(my_str)
print ("The number is {}").format(my_result)
