n1=int(input("enter the encoding range: "))
def sum(a):
    sum=0
    for i in range(1,n1):
      if i%3==0:
         sum+=i
      print(sum)
    sum(n1)     