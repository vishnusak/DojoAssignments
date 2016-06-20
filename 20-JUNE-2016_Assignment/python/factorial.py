def rFact(num):
    num = int(num)

    if num > 1:
        return num * rFact(num - 1)
    else:
        return 1

myNum = 6.5
print("rFact({}) is {}").format(myNum, rFact(myNum))
