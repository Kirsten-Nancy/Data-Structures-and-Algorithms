def IsSubsequence(s,t):
    sub = ''
    location = 0
    found = False
    for i in range(0, len(s)):
        for j in range(location, len(t)):
            if s[i] == t[j]:
                sub += t[j]
                location += 1
                found = True
                print(t[j])
            else:
                print('not')
                found = False
    return found

# s = "axc"
# t = "ahbgdc"
print(IsSubsequence('aaaaaa','bbaaaa'))

