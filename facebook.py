array = [-12, -6, -2, 1, 4, 5, 6, 10]
left, right = 0, len(array)-1
square_array = []
for i in array:

    if abs(array[left]) > abs(array[right]):
        squared = array[left]**2
        left = left + 1
    else:
        squared = array[right]**2
        right = right - 1

    square_array.insert(0, squared)

print(square_array)
