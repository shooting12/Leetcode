#--------------------------------------------------
# One edit in a string then become another string:
#   pale, ple -> true
#   pales, pale -> true
#   pale, bale -> true
#   pale, bake -> false
#--------------------------------------------------
'''
Todo:
  -1. Think more other faster ways -
  2. Refer to Textbook in the future if needed
     >> separate replace/insert/delete then merge in 1 run

Hint:
  1. How to examine 3 check in 1 run

Note:

'''
def isOneAway_1st(str1, str2):
    ''' Use extra list to store chars, remove common chars, check left: O(n^2)/O(n) '''

    # If length difference is larger than 1 then must not one edit
    l1 = len(str1)
    l2 = len(str2)
    if abs(l1-l2) > 1:
        return False

    # Remove same character in both lists
    list1 = list(str1)
    list2 = list(str2)
    list1_dup = list1.copy()
    
    for c in list1:        
        if c in list2:
            list1_dup.remove(c)
            list2.remove(c)

    # If length difference is larger than 1 then must not one edit
    l1 = len(list1_dup)
    l2 = len(list2)

    # Check if one edit can handle the only 1 character difference
    if abs(l1-l2) > 1 or l1 > 1:
        return False

    return True


def main():
    strList1 = ['pale', 'pales', 'pale', 'pale', 'abc', 'abcdef', 'abd', 'abcd']
    strList2 = ['ple', 'pale', 'bale', 'bake', 'abb', 'abdef', 'abcd', 'ab']
 
    funcList = [isOneAway_1st]

    for func in funcList:
        print(func)
        for s1, s2 in zip(strList1, strList2):
            ret = func(s1, s2)
            print("%10s and %10s are different in one edit: %d" % (s1, s2, ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()