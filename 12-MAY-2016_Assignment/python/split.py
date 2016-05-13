# String.split
# string.split(separator,limit)  - split string into array of substrings, returning the new array. Separator specifies where to divide substrings and is not included in any substring. If  ""  is specified, split string on every character. Limit is optional and indicates number of splits; additional post-limit items should be discarded.
# Note: existing string is unaffected.

# steps:
# ---- This is javascript behaviour. The python split doesn't discard the post limit items. Instead in python, the rest of the string is returned as a single element in the result array!!!!!!!

# 1. read the string char by char
# 2. if seperator is empty, then push each char into the output array and return output array
# 3. if seperator is not empty, match each char with the seperator.
# 4. whenever the char matches the seperator, store the previously read substring into the result array and continue reading from next char
# 5. repeat 3 and 4 till end of string
def split(string, sep, limit=0):
    result = []
    push_count = 0

    if (limit <= 0):
        limit = len(string)

    if (len(sep) == 0):
        # seperator string is empty. so split full string, char by char
        for char in string:
            result.append(char)
            push_count += 1
            if (push_count == limit):
                break
    elif (len(sep) == 1):
        # seperator is a single character
        start = 0
        for idx in range(len(string)):
            if (string[idx] == sep):
                result.append(string[start:idx])
                start = idx + 1
                push_count += 1
                if (push_count == limit):
                    break
        else:
            if (start < len(string)):
                result.append(string[start:])
    else:
        # seperator is a string with length > 1
        start = 0
        for idx in range(len(string) - len(sep) + 1):
            if (string[idx:idx + len(sep)] == sep):
                result.append(string[start:idx])
                start = idx + len(sep)
                push_count += 1
                if (push_count == limit):
                    break
        else:
            if (start < len(string) - len(sep) + 1):
                result.append(string[start:])

    return result

myStr = "this is yet an other     string"
print("\nThe string is '{}'\n").format(myStr)

myResult = split(myStr, ' ', 3)

print("The split result is {}\n").format(myResult)
