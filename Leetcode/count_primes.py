def countPrimes(number):
    count = 0
    if number > 1:
        for i in range(2, number):
            for j in range(2, i):
                if i % j != 0:
                    count += 1
                    break
    return count

print(countPrimes(10))

