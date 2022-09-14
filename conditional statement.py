##a,b,c=map(int,input("Enter 3 number: ").split())
##
##if(a>b and a>c):
##    print(a," is greater")
##if(b>a and b>c):
##    print(b," is greater")
##else:
##    print(c," is greater")
    
##tot = 25
##a = int(input("Enter the attendance: "))
##b = (a *100)//25
##
##if(b >=70):
##    print("Eligible for exam")
##else:
##    print("Not Eligible for exam")

service = int(input("Enter the service year: "));
sal = int(input("Enter your salary: "));

if service >= 10:
    print("Bonus = ",sal*0.15)
elif service >= 5:
    print("Bonus = ",sal*0.1)
elif service >= 3:
    print("Bonus = ",sal*0.05)
else:
    print("Not Eligible for bonus")
