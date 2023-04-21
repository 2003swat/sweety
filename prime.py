a = int(input("Enter the number:-"))
def swati(n):
    i=2
    c=0
    while i<n:
        if (n % i)==0:
            c=1
            break
        i+=1
    if a==2:
        print(a, "is a prime number:")
    elif c==1:
        print(a, "is not prime number:")

    else:
        print(a,"is prime number:")   
    


swati(a)
