import time
print(input("Welcome, To DBJinfoMedia company, press Enter"))
print(input("Enter your details below and Register Yourself as Employee, press Enter"))

try:
    name = str(input("enter your name: "))
    age = int(input("enter your age: "))
    
    if age > 70:
        print("you can't get a job")
    else:
     address = str(input("Enter your adress: "))
     workas = str(input("Specialized in: "))
     data = name , age , address , workas
     data = str(data)

    print("Sending email to the authority..")
    time.sleep(5)
    print("Wait for your approvement..")
    time.sleep(6)
    print("Application Approved !")
    time.sleep(4)
    print("welcome To our Team")
except ValueError:
    print("How will we give you a job , by looking at your FACE !!!")
