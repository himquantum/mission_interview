def get_subarray(arr, start, length, subarray = []):
    for i in range(start, start+length):
        subarray.append(arr[i])
    return subarray

print(get_subarray([1,3,5,-6,-4,7], 2, 4))


print([x for x in range(1,7)])