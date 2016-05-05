# The Luhn formula is sometimes used to validate credit card numbers. Create the function  isCreditCardValid(digitArr)  that accepts an array of digits on the card (13-19 depending on the card), and returns a boolean whether the card digits satisfy the Luhn formula, as follows:
# 1. Set aside the last digit and do not include it in these calculations (until step 5);
# 2. Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
# 3. If any results are larger than 9, subtract 9 from them;
# 4. Add all numbers (not just our odds) together;
# 5. Now add the last digit back in - the sum should be a multiple of 10.
# For example, given digit array  [5,2,2,8,2] , it would become 1)  [5,2,2,8] , then 2)  [5,4,2,16] , then 3)  [5,4,2,7] , then 4)  18 , then 5)  20 , so we would return  true . If the final digit were any other value, we would return  false .

from random import random

def isCreditCardValid(arr):
    card_sum = 0

    for idx in range(-2, (-1*(len(arr)+1)), -2):
        if ((arr[idx] * 2) > 9):
            card_sum += (arr[idx] * 2) - 9
        else:
            card_sum += (arr[idx] * 2)

        if ((idx - 1) >= (-1 * len(arr))):
            card_sum += arr[idx - 1]

    if (((card_sum + arr[-1]) % 10) == 0):
        return 'VALID'
    else:
        return 'INVALID'

myCard = []
for i in range(16):
  myCard.append(int(round(random() * 9)))
# myCard = [2,6,9,5,8,8,1,5,2,3,6,4,3,6,2,4] - this is a valid card
# myCard = [2,6,0,6,8,7,5,4,3,6,0,4,3,7,7,1] - This is a calid card

print("The card number {} is {}").format(('').join(str(e) for e in myCard), isCreditCardValid(myCard))
