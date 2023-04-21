s=int(input("enter the number: "))
a=s
b=0
while(s>0):
    c=s%10
    b=b*10+c
    s=s//10
if(a==b):
    print("the number is palindrome!")
else:
    print("the number is not palindrome!")
