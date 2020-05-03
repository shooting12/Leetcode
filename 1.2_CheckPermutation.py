'''
Todo:
  -1. Think more other faster ways  
  2. What is hint #131 mean?
  3. Space complexity of using hashtable O(c)?
  
Hint:
  1. O(n) way
  2. hashtable
  3. Same sequence

Note:
  1. Remeber to ask lower/upper case are the same or not

'''

def isPermutation_1st(str1, str2):
    ''' Use in-place sorting techniques to check permutation: O(nlogn) / O(?) space depends on sorting algo
         Sort each string, and compare them each character by each character. '''

    l1 = len(str1)
    l2 = len(str2)

    if l1 != l2:
        return False

    sortStr1 = sorted(str1)
    sortStr2 = sorted(str2)

    for char1, char2 in zip(sortStr1, sortStr2):
        if char1 != char2:
            return False

    return True


def isPermutation_hashtable(str1, str2):
    ''' Use hashtable techniques to check permutation: O(n)/O(c) '''

    l1 = len(str1)
    l2 = len(str2)

    if l1 != l2:
        return False

    strDict1 = dict()
    strDict2 = dict()

    # Put string's all characters in dictionary (~hashtable)
    for c in str1:
        c = c.lower()
        count = strDict1.get(c, 0)
        count += 1 
        pair = {c : count}
        strDict1.update(pair)

    for c in str2:
        c = c.lower()
        count = strDict2.get(c, 0)
        count += 1
        pair = {c : count}
        strDict2.update(pair)

    # Compare two dictionary to see if 2 strings are same
    for key, value in strDict1.items():
        if key not in strDict2:
            return False

        if value != strDict2[key]:
            return False

    return True


def isPermutation_hint(str1, str2):
    ''' Use dictionary & Add chars count in 1st string + minus chars count in 2nd string: O(n)/O(c) '''
    l1 = len(str1)
    l2 = len(str2)

    if l1 != l2:
        return False

    strDict = dict()

    # Put 1st string's all characters in dictionary (~hashtable)
    for c in str1:
        c = c.lower()
        count = strDict.get(c, 0)
        count += 1 
        pair = {c : count}
        strDict.update(pair)

    # Minus dictionary by 2nd string's chars
    for c in str2:
        c = c.lower()
        count = strDict.get(c, 0)
        count -= 1
        
        if count < 0:
            return False

        pair = {c : count}
        strDict.update(pair)

    # Check whether all the char count in dictionary is zero (should be)
    for key, value in strDict.items():
        if value != 0:
            return False

    return True


def main():
    strList1 = ['abc', 'abdde', 'abdde']
    strList2 = ['cab', 'cdabe', 'cabe']
 
    funcList = [isPermutation_1st, isPermutation_hashtable, isPermutation_hint]

    for func in funcList:
        print(func)
        for s1, s2 in zip(strList1, strList2):
            ret = func(s1, s2)
            print("%s and %s are each other's permutation: %d" % (s1, s2, ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()