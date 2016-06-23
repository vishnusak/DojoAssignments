def strSubsets(str):
    result = [""]

    if len(str) <= 1:
        result.append(str)
        return result

    str1 = ''
    str2 = ''

    for i in range(len(str)):
        for j in range(i+1,len(str)):
            str1 = str[i:j]
            str2 = str[j:]

            # print("i = {}; j = {}; str1 = {}; str2 = {}").format(i, j, str1, str2)
            for char in str2:
                result.append(str1+char)

    for char in str:
        result.append(char)

    return result

myStr = "string"
myResult = strSubsets(myStr)
print ("String is ''{}''").format(myStr)
print ("Subsets are: {}").format(myResult)
print ("Number of subsets are: {}").format(len(myResult))
