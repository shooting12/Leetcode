'''
Todo: 
  1. Bit vector implementaiton
  2. Sorting algorithm by myself 
  3. Figure out difference between ASCII and Unicode

Tips:
  1. String len larger than alphabet count -> not unique
  2. Use array

'''

def uniqueStr_1st(inStr):
    ''' Compare all chars after the index char: O(n^2)/O(1) '''
    l = len(inStr)
    for i in range(l):
        for j in range(i+1, l):
            if inStr[i] == inStr[j]:
                return False
    return True


def uniqueStr_hashtable(inStr):
    ''' Use hashtable to see if all the char is unique: O(n)/O(c) '''

    strDict = dict()

    for c in inStr:
        # ASCII of a character: ord('a')=97 & chr(97) = 'a'
        index = ord(c)
        if index in strDict:
            return False
        else:
            strDict[index] = c

    return True


def uniqueStr_sorting(inStr):
    ''' Use sorting and then compare next char: O(nlogn)/O(?) space depends on sorting algo '''
    
    sortStr = sorted(inStr)
    l = len(sortStr)

    for i in range(l-1):
        if sortStr[i] == sortStr[i+1]:
            return False

    return True


def main():
    strList = ['abc', 'aaaa', 'abcd', 'abac', '1ac23', '0ao01']
 
    funcList = [uniqueStr_1st, uniqueStr_hashtable, uniqueStr_sorting]

    for func in funcList:
        print(func)
        for s in strList:
            ret = func(s)
            print("%s is unique: %d" % (s, ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()