name = address = dob = age = phone = salary = dept = None

while(name == None or address == None or dob == None or age == None or phone == None or salary == None or dept == None):
    if name == None:
        name = input("Enter Name:")
        if len(name) == 0:
            name = None
            print("Please enter the value")
            continue
        try:
            var = int(name)
            name = None
            print("Name should not be number ")
            continue
        except:
            continue
        
    if address == None:
        address = input("Enter address: ")
        if len(address) == 0:
            address = None
            print("Please enter the value")
            continue
        
        
    if dob == None:
        dob = input("Enter dob: ")
        if len(dob) == 0:
            dob = None
            print("Please enter the value")
            continue
        
    if age == None:
        age = input("Enter Age: ")
        if len(age) == 0:
            print("Please enter the value")
            age = None
            continue
        try:
            age = int(age)
            if(age <= 0):
                age =None
                print("Age should be greater than 0 ")
                continue
        except:
            print("Enter number")
            age = None
            continue

    
        
    if phone == None:
         phone = input("Enter Phone number: ")
         if len(phone) < 0:
            print("Please enter the value")
            phone = None
            continue
         try:
             if(len(phone)<10):
                phone =None
                print("Please give 10 digit number")
                continue
             phone = int(phone)
            
         except:
            print("Enter number")
            phone = None
            continue

        
    if dept == None:
        dept = input("Enter Department: ")
        if len(dept) == 0:
            dept = None
            print("Please enter the value")
            continue

    if salary == None:
        salary = input("Enter Salary: ")
        if len(salary) == 0:
            print("Please enter the value")
            salary = None
            continue
        try:
            salary = int(salary)
            if(salary <= 0):
                salary =None
                salary("Salary should be greater than 0 ")
                continue
        except:
            print("Enter number")
            salary = None
            continue

print("********************")
print("Name: ",name)
print("Address: ",address)
print("Date of birth: ",dob)
print("Age: ",age)
print("phone: ",phone)
print("Department: ",dept)
print("Salary: ",salary)
    
