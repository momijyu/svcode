values= [23.5, 35.2, 73.5, 47.6]
max_num= 0
min_num= 100
for i in values:
    if max_num <= i:
        max_num = i
    if min_num >= i:
        min_num = i
print("最大値:",max_num,"\n最小値:",min_num)