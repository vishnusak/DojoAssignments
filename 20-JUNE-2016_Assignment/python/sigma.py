def rSigma(num):
    num = int(num)

    if num > 1:
        return num + rSigma(num - 1)
    else:
        return 1

myNum = 10
print("rSigma({}) is {}").format(myNum, rSigma(myNum))
