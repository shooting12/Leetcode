#--------------------------------------------------
# String compression:
#   string aabcccccaaa would become a2blc5a3
#--------------------------------------------------
'''
Todo:
  -1. Think more other faster ways
  -2. Don't undersatnd hint
     >> Refer to Textbook sol2

Hint:
  1. compress string and compare length
  2. Be careful of duplicate concatenate string

Note:

'''
DEBUG = 0
def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def doStrigCompression_1st(inStr):
    currChar = inStr[0]
    outStr = ''
    count = 1

    l = len(inStr) - 1
    for i in range(l):
        printd("%d currChar %s, count %d, outStr %s" % (i, currChar, count, outStr))
        j = i + 1
        if  inStr[i] == inStr[j]:
                count += 1
                continue
        else:
            outStr += currChar
            outStr += str(count)
            count = 1
            currChar = inStr[j]

    # For last character
    outStr += currChar
    outStr += str(count)

    if len(outStr) < len(inStr):
        return outStr
    else:
        return inStr


def doStrigCompression_sol1(inStr):
    outStr = ''
    count = 0

    l = len(inStr)
    for i in range(l):
        count += 1

        if (i+1 >= l) or inStr[i] != inStr[i+1]:
            outStr += inStr[i] + str(count)
            count = 0

    return outStr if len(outStr) < len(inStr) else inStr


def main():
    strList = ['aabcccccaaa', 'abacb']
 
    funcList = [doStrigCompression_1st, doStrigCompression_sol1]

    for func in funcList:
        print(func)
        for s in strList:
            ret = func(s)
            print("%s become %s" % (s, ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()