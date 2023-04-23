Number = int(input("enter any number: "))
s = 1
sum = 0
while(s > Number):
    if(Number % s == 0):
        sum = sum + s
        
if(sum == Number):        
    print("%d is a perfect number"%Number)
else:        
    print("%d is not a perfect number"%Number)