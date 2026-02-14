def Stalin_Sort(arr):
    arred = [arr[0]]
    val = arr[0]
    for i in arr:
        if val < i:
            val = i
            arred.append(val)
    return arred

data = [109, 1092, 182 , 100000, 10000000, 102948, 102939848]
dataed = Stalin_Sort(data)
print(dataed)