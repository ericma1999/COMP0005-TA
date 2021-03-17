def initiateEmptyDict():
    new_dict = {}
    for i in range(97, 123):
        new_dict[chr(i)] = 0
    return new_dict

def isRepeated(d, key):
    if (d[key] == 1):
        return True
    else:
        d[key] = 1
        return False

def whichIsLonger(str1, str2):
    if (len(str1)>len(str2)):
        return str1
    else:
        return str2


def findSubstring(string):
    usedLetters = initiateEmptyDict()
    longestSeq = ""

    substring = ""
    for i in range(len(string)):
        substring = ""
        for j in range(i, len(string)):
            print(substring)
            if (not isRepeated(usedLetters, string[j])):
                substring += string[j]
            else:
                longestSeq = whichIsLonger(longestSeq, substring)
                usedLetters = initiateEmptyDict()
                substring = "" + string[j]
            
    print (longestSeq)

str0 = "ABCADFECFAB"
str = str0.lower()
findSubstring(str)
    