values= [23.5, 35.2, 73.5, 47.6]
sum_num= 0
for i in range(len(values)):
    sum_num += values[i]
ave= sum_num /len(values)
print("合計値:",sum_num,"\n平均値:",ave)