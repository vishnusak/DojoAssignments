# Common Suffix
#
# Lance is writing his opus: a tome of beat poetry. Always looking for a good rhyme, he seeks words ending with the same letters. Write a function that, given a word array, returns the largest common suffix (word-end). For inputs  ["deforestation", "citation", "conviction", "incarceration"] , return  "tion"  (not a very creative starting point). If it is  ["nice", "ice", "baby"] , return  "" .
def suffix(arr):
    result = ''
    lmin = len(arr[0])
    suf  = ''

    for word in arr:
        if (len(word) < lmin):
            lmin = len(word)

    for char in range(1, lmin+1):
        for word in arr:
            if (suf == ''):
                suf = word[len(word) - char:]
            else:
                if (word[len(word) - char:] != suf):
                    return result
        else:
            result = suf
            suf = ''
    else:
        return result

myStr = ["deforestation", "citation", "conviction", "incarceration", "rice"]
# myStr = ["deforestation", "citation", "conviction", "incarceration"]
# myStr = ["bernice", "mice", "caprice", "thrice", "rice"]
# myStr = ["there", "here", "where"]
print("The array of strings is {}").format(myStr)

myResult = suffix(myStr)
print("The common suffix is '{}'").format(myResult)
