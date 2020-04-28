def uniqueStr_bruteforce(inStr):
    l = len(inStr)
    for i in range(l):
        for j in range(i+1, l):
            if inStr[i] == inStr[j]:
                return False
    return True


def uniqueStr_hashtable(inStr):   
    strDict = dict()

    for c in inStr:
        # ASCII of a character: ord('a')=97 & chr(97) = 'a'
        index = ord(c)
        if index in strDict:
            return False
        else:
            strDict[index] = c

    return True


def main():
    strList = ['abc', 'aaaa', 'abcd', 'abac']
 
    funcList = [uniqueStr_bruteforce, uniqueStr_hashtable]

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