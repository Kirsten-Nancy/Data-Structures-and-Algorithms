from array_implementation import MyArray

arr1 = MyArray()
arr1.push('korir')
arr1.push('Jeff')
print(arr1.length)
print(arr1.data)
print(arr1.get(0))
arr1.pop()
arr1.push('Nancy')
arr1.push('Githeri')
print(arr1.data)
arr1.delete(1)
print(arr1.length)
print(arr1.data)