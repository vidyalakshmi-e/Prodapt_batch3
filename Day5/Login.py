count=0
while(count<3):
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if(username=="vidya"  and password=="Admin@123"):
        print(username ," has login in successfully")
        break
    elif(username !="vidya" and password=="Admin@123"):
        print("Invalid password")
        count+=1
    else:
        print("Invalid username and password")
        count+=1
if count>=3:
    print("Exceeded maximum attempts to login")
