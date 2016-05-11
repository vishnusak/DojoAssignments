# Parens Valid
# Create a function that, given an input string  str , returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For  "Y(3(p)p(3)r)s" , return  true . Given  "N(0(p)3" , return  false : not every parenthesis is closed. Given  "N(0)t )0(k" , return  false .
# steps:
# 0. for every closed parenthesis, there has to be an open parenthesis. Which means that at any given point, the number of open parens we are tracking will be greater than or equal to the number of closed parens. We will use this.
# 1. traverse the string. if the char is an open parens, push it into an array - openparens
# 2. if the char we read is a closed parens, check the openparens array. If it is empty, then return false. If it is not empty, step-3
# 3. pop from the openparens array. This means that one pair of open and close are accounted for.
# 4. continue steps 2 and 3 till end of string.
# 5. at the end of the loop, if the openparens array still has elements, return false, otherwise return true
def parens(str):
    openPrens = []
    for char in str:
        if (char == '('):
            openPrens.append(char)
        elif (char == ')'):
            if (len(openPrens) == 0):
                return False
            else:
                openPrens.pop()
    else:
        if (len(openPrens) == 0):
            return True
        else:
            return False

myStr = "Y(3(p)p(3)r)s"
# myStr = "N(0(p)3"
# myStr = "N(0)t )0(k"
print("The string is {}").format(myStr)

myResult = parens(myStr)

if (myResult):
  print("{} - all parenthesis are matched").format(myResult)
else:
  print("{} - all parenthesis are not matched").format(myResult)
