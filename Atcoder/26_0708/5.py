#a, b = map(float,input().split())
#print(int(a*b))
a, b = map(str,input().split())
b = float(b)*100
b = int(b)
print(int(a)*int(b)//100)