"Customer Management System"
#BLL:Business Logic Layer
id_list=[]          #id_list=[10,20,30]
name_list=[]        #name_list=["vikas","Anil","Amit"]
age_list=[]         #age_list=[39,41,45]
mob_list=[]         #mob_list=[1234,2345,3456]
def addCustomer(id,name,age,mob):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mob_list.append(mob)
    return
def searchCustomer(id):     #id=20
    index=id_list.index(id) #index=1
    return index
def deleteCustomer(id):     #id=20
    i=id_list.index(id)     #i=1
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mob_list.pop(i)
def modifyCustomer(id,name,age,mob):    #30,"Prashant",55,9999
    i=id_list.index(id)     #i=2
    name_list[i]=name
    age_list[i]=age
    mob_list[i]=mob

#PL: Presentation Layer
def showCustomer(i):        #i=1
    print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i],"Cust Mob:",mob_list[i])

print("Welcome to Akshat's Management System")
while(1):
    choice=input("Enter Choice:\n1.for Add Cust\n2.Search\n3.Delete\n4.Modify\n5.Display all\n6.for Exit:")
    if(choice=="1"):    #Add New Customer
        id=input("Enter Cust ID:")          #10
        name = input("Enter Cust Name:")    #"Vikas"
        age = input("Enter Cust Age:")      #39
        mob = input("Enter Cust Mob:")      #1234
        addCustomer(id,name,age,mob)
        print("Customer Added Successfully")
    elif(choice=="2"):  #Search Customer
        id=input("Enter Cust Id to Search:")    #id=20
        i=searchCustomer(id)            #i=1
        showCustomer(i)
    elif(choice=="3"):  #Delete Customer
        id=input("Enter Cust Id to Delete:")
        deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(choice=="4"):  #Modify Customer
        id=input("Enter Customer Id to Modify:")   #id=30
        name=input("Enter Cust updated name:")  #"Prashant"
        age = input("Enter Cust updated age:")  #55
        mob = input("Enter Cust updated mob:")  #9999
        modifyCustomer(id,name,age,mob)
        print("Customer Modified Successfully")
    elif(choice=="5"):  #Display all Customers
        for i in range(len(id_list)):   #i=0,1,2
            showCustomer(i)
    elif(choice=="6"):  #Exit
        print("Thanks for using Akshat's CRM")
        break
    else:
        print("Incorrect Choice")



