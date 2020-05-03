#--------------------------------------------------
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
#--------------------------------------------------
'''
Todo:
  -1. Think more other faster ways --> Hint says using Bit Vector, how?
  2. How to update value dictionary with same key in a faster way?
  3. Space complexity of using hashtable O(c) ?
  4. Bit manipulation

Hint:
  1. Hashtable (already did)
  2. Bit vector
  3. Use 26 array size + calculate each char to 0-25

Note: (Refer to book's solution)
  1. Use foundOdd two times to check whether there are 2 odd (good idea)
  2. Use array with 26 size, and map a-z to them
  3. Check whether only 1 bit is 1 with technique: (x & (x-1)) == 0
'''

DEBUG = 0
def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def  isPalindromePermutation_1st(inStr):
    ''' Use hashtable and if more than 1 odd count then not qualifiied: O(n)/O(?) '''
    strDict = dict()

    # Sum each characters apperance times
    for c in inStr:
        c = c.lower()
        val = strDict.get(c, 0)
        val += 1
        pair = {c : val}
        strDict.update(pair)

    # Count how many key has odd count
    oddCount = 0
    specialChars = [' ']
    for key, value in strDict.items():
        print(key, value)
        if value % 2 != 0:
            if key not in specialChars:
                oddCount += 1

    # More than 1 odd count means not palindrome
    if oddCount > 1:
        return False
    else:
        return True


def isPalindromePermutation_sol1(inStr):
    ''' Similar to my 1st, but use foundOdd flag twice to chekc is good idea: O(n)/O(?) '''
    strDict = dict()

    # Sum each characters apperance times
    for c in inStr:
        c = c.lower()
        val = strDict.get(c, 0)
        val += 1
        pair = {c : val}
        strDict.update(pair)

    # foundOdd: If appear two times then return
    foundOdd = False
    # Count how many key has odd count
    oddCount = 0
    specialChars = [' ']
    for key, value in strDict.items():
        print(key, value)
        if value % 2 != 0:
            if key not in specialChars:
                if foundOdd:
                    return False
                foundOdd = True

    return True


#####################
#  Following are referering to sol3 in textbook
#####################
def calculateCharNumber(c):
    # ord('a') = 97
    c = c.lower()
    return ord(c) - 97


def toggleBitVector(myBitVec, index):
    printd("[toggleBitVector]+ bitVec(%s), index(%d)" % (bin(myBitVec), index))

    mask = 1 << index    
    
    # Reverse the index bit (1 to 0, 0 to 1)
    if (myBitVec & mask) == 0:
        myBitVec |= mask
    else:
        myBitVec &= ~mask

    printd("[toggleBitVector]- bitVec(%s), index(%d)" % (bin(myBitVec), index))

    return myBitVec


def isPalindromePermutation_sol3(inStr):
    myBitVec = 0
    for c in inStr:
        n = calculateCharNumber(c)
        print('{} {}'. format(c, n))
        if n >= 0:
            myBitVec = toggleBitVector(myBitVec, n)

    return (myBitVec & (myBitVec -1)) == 0


def main():
    strList = ['Tact Coa', 'abacb']
 
    funcList = [isPalindromePermutation_1st, isPalindromePermutation_sol1, isPalindromePermutation_sol3]

    for func in funcList:
        print(func)
        for s in strList:
            ret = func(s)
            print("'%s' is Palindrome Permutation: %d" % (s, ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()