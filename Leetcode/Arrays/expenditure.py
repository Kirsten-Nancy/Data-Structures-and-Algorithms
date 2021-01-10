monthlyExpenses = [
    {
        'January': 2200,
        'February': 2350,
        'March': 2600,
        'April': 2130,
        'May': 2190
    }
]


# 1
# print(monthlyExpenses[0]['February'] - monthlyExpenses[0]['January'])
# 2
expenses = [2200,2350,2600,2130,2190]

sum = 0
for i in range(3):
    sum = expenses[i] + sum

print(sum)

def twoThousand(array):
    for i in range(len(array)):
        if array[i] == 2000:
            return 'Yes i did'
        else:
            return 'For once'

print(twoThousand(expenses))

# 4
expenses.append(1980)
print(expenses)

# 5
expenses[3] = expenses[3] - 200
print(expenses)
