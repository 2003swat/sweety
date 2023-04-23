print("enter the marks: ")
marksOne = int(input())
marksTwo = int(input())
marksThree = int(input())
marksFour = int(input())
marksFive = int(input())
tot = marksOne+marksTwo+marksThree+marksFour+marksFive
avg = tot/5 
if avg>=100 and avg<=80:
    print("First class") 
elif avg>=70 and avg<=80:
    print("second class") 
elif avg>=60 and avg<=70:
    print("Average")
elif avg>=40 and avg<=60:
    print("Pass")
elif avg>=40 and avg<=40:
    print("Fail")  
else:
    print("fails")          



