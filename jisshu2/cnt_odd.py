numbers= [2, 3, 1, 4, 4, 0, 2, 5, 4, 3]
cntodd= 0
cnteven= 0
for i in range(len(numbers)):
    if numbers[i]%2 == 1:
        cntodd += 1
    else:
        cnteven += 1
print("odd:",cntodd, "\neven:",cnteven)
