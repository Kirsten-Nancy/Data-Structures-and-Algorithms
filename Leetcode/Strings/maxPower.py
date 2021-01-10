def maxPower(string):
    maxCount = 0
    currentCount = 0
    previous = ' '

    for i in (range(len(string))):
        if string[i] == previous:
            currentCount += 1
        else:
            currentCount = 1
            previous = string[i]
        
        maxCount = max(maxCount, currentCount)
    return maxCount

print(maxPower('leetcode'))