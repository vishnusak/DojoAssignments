# Book Index
#
# Martin is writing his opus: a book of algorithm challenges, set as lyrics to a suite of baroque fugues. He knows that some of those fugueing challenges will be less popular than others, so he needs a book index. Given a sorted array of pages, produce a book index string. Consecutive pages should form ranges separated by a dash. For  [1,3,4,5,7,8,10] , return the string  "1, 3-5, 7-8, 10" .

# steps:
# ---- ignoring a whole lot of that statement because my english vocabulary doesn't stretch that far. But the main problem statement is clear and I think I can handle that. so here goes...
def index(arr):
    pages = ''
    start = arr[0]
    end = arr[0]

    for i in range(1, len(arr)):
        if (arr[i] == arr[i - 1] + 1):
            end = arr[i]
        else:
            if (start == end):
                pages += "{}, ".format(start)
            else:
                pages += "{}-{}, ".format(start, end)

            start = arr[i]
            end = arr[i]
    else:
        if (start == end):
            pages += "{}".format(start)
        else:
            pages += "{}-{}".format(start, end)

        return pages

myArr = [1,2,3,4,5,7,8,10,13,14,15,17,18,19,20]
print("The array of pages is {}").format(myArr)

myStr = index(myArr)
print("The index string is '{}'").format(myStr)
