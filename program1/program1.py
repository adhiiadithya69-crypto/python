c=int(input("Enter the current year:"))
f=int(input("Enter the final year:"))
print("Future leap years are:")
for x in range(c,f+1):
    if(x%4==0 and x%100!=0) or (x%400==0):
        print(x)