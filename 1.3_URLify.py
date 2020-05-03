#--------------------------------------------------
# Replace space with %20:
#   Input: "Mr John Smith ", 13
#   Output: "Mr%20John%20Smith"
#--------------------------------------------------
'''
Todo:
  1. How to implement different ways in python? (Refer to hint)
  2. What is trueLength in hint answer?
 
Hint:
  1. Handle string backwards
  2. Need to know number of space

Note:
  1. Add escape % to show % in string. e.g. %%20
'''

def urlify_1st(inStr):
    return inStr.replace(' ', '%20')


def main():
    strList = ['a b c', 'a  b   d de', 'ab  dd  e']
 
    funcList = [urlify_1st]

    for func in funcList:
        print(func)
        for s in strList:
            ret = func(s)
            print("%s become %s after replacing space to %%20." % (s, ret))


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()