strs = ["flower","flow","flight"]
first = strs[0]


def longestCommonPrefix(mystring):
    result = ""
    for i in range(1, len(mystring)):
        for j in range(len(mystring[i])):
            if first[j] == mystring[i][j]:
                result +=  mystring[i][j]

longestCommonPrefix(strs)