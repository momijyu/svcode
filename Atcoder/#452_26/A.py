sekku = [(1,7), (3, 3), (5, 5), (7, 7), (9, 9)]
m, d = map(int, input().split())
for i in range(len(sekku)):
    if sekku[i][0] == m and sekku[i][1] == d:
        print("Yes")
        exit()
print("No")