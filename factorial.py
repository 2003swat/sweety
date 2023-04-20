num=int(input("enter a number to find factorial: "))
factorial=1;
if num<0:
    print("factorial does not defined for negative integer");
elif(num==0):
    print("the factorial of 0 is 1");
else:

   while(num>0):
         factorial=factorial*num
         num=num-1
         print("factorial of the given number is: ")
         print(factorial)
