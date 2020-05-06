#--------------------------------------------------
# Assumeyou have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
#--------------------------------------------------
'''
Todo:
  -1. Think more other faster ways

Hint:
  1. Refer to sol

Note:

'''
DEBUG = 1
def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def isSubString(s1, s2):
    ''' Check if s2 is s1's substring '''
    if s1.find(s2) >= 0:
        return True
    else:
        return False


def isStringRotation_1st(str1, str2):
    if len(str1) != len(str2):
        return False

    if str1 == '':
        return True

    index = str2.find(str1[0])
    if index < 0:
        return False

    printd(index)
    printd(str2[index:])
    printd(str2[:index])

    newStr = str2[index:] + str2[:index]

    if not isSubString(str1, newStr):
        return False

    return True


def isStringRotation_sol(str1, str2):
    ''' execution time depends on isSubString's time, if isSubString is O(A+B), then O(N) '''
    if len(str1) != len(str2):
        return False

    # s1(waterbottle) & s2(erbottlewat)
    # x = wat, y=erbottle
    # s1 = xy, s2 = yx, yx(s2) must be xyxy's substring
    newStr = str1 + str1

    if isSubString(newStr, str2):
        return True
    else:
        return False


def main():
    strList1 = ['waterbottle', 'abcde', 'aa', 'xyz', "bbbacddceeb", ""]
    strList2 = ['erbottlewat', 'abced', 'a', 'xyz', "ceebbbbacdd", ""]
 
    funcList = [isStringRotation_1st, isStringRotation_sol]

    for func in funcList:
        print(func)
        for s1, s2 in zip(strList1, strList2):
            ret = func(s1, s2)
            print("%15s is %15s's rotation string: %d" % (s2, s1, ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()