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


class Solution:
    def containsDuplicate_dict(self, nums):
        ''' 124ms '''
        numDict = dict()

        for c in nums:
            if c in numDict:
                return True
            else:
                numDict[c] = c

        return False


    def containsDuplicate_dict2(self, nums):
        ''' 124ms '''
        numDict = {}

        for c in nums:
            val = numDict.get(c, 0)
            
            if val:  # != 0
                return True
            else:
                numDict[c] = 1

        return False


    def containsDuplicate_set(self, nums):
        ''' 128ms '''
        if len(nums)==len(set(nums)):
            return False
        else:
            return True


    def containsDuplicate(self, nums):
        return self.containsDuplicate_set(nums)


def main():
    # --- Textbook ---
    strList = ['abc', 'aaaa', 'abcd', 'abac', '1ac23', '0ao01']
 
    funcList = [uniqueStr_1st, uniqueStr_hashtable, uniqueStr_sorting]

    for func in funcList:
        print(func)
        for s in strList:
            ret = func(s)
            print("%s is unique: %d" % (s, ret))

    # --- Leetcode ---
    nums = [1, 2, 3, 1]
    sol = Solution()
    ret = sol.containsDuplicate(nums)
    print("%s is unique: %d" % (str(nums), ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()