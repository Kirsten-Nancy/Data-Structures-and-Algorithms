myList = []


def fizzBuzz(n):
    for i in range(1, n + 1):
        # if i % 3 == 0 and i % 5 == 0:
        if i % 15 == 0:
            myList.append('FizzBuzz')
        elif i % 3 == 0:
            myList.append('Fizz')
        elif i % 5 == 0:
            myList.append('Buzz')
        else:
            myList.append(str(i))

    return myList

print(fizzBuzz(100))
