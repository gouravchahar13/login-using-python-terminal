
class login():
    def new_user(self):
        
        global login_info
        global userid
        global ps
        login_info={}
        userid=[]    
        ps=[]
        
        print("welcome to the login system",)
        user_name=input("enter enter the user name:\t")
        while user_name in userid:
                print("the user name has been taken please ernter a new user name\t")
                user_name=input("enter enter the user name:\t")
        password=input("enter the password:\t")
        while len(password)<8:
                print("the paswword is less than 8 digits ")
                password=input("enter the password agin:\t")
        confirm_password=input("Retype the password:")
        while password!=confirm_password:
                print("the password entered and current password do not match")
                confirm_password=input("Retype the password:")
        email=input("enter the email of the user")
            
        userid.append(user_name)
        ps.append(password)
            
        login_info=dict(zip(userid,ps))
        print(userid)
        print(ps)
        print(login_info)
        print("thank you for signing up You can proceed to login")
    def old_user(self):
        print("please proceed toward login by entering the user name and password")
        user_name=input("enter enter the user name:\t")
        password=input("enter the password:\t")
        if user_name in list(login_info.keys()):
                z=login_info[user_name]
                if z==password:
                    print("the user name and password are correct")
                    print("we will be redirecting you to the login page")
                    print("thank you")
                else:
                    print("INVALID PASSWORD")
        else:
                print("INVALID USER_NAME")
if __name__=="__main__":
      li=login()
      entry=input("Are you a new user (Y/N)")
      while not entry.lower()=="y"  or entry.lower()=="n":
        print('INVALID OPTION TRY AGAIN')
        entry=input("Are you a new user (Y/N)")
        if entry.lower()=="y":
                li.new_user()
                li.old_user()
                quit()
        elif entry.lower()=="n":
                li.old_user()
                quit()
        

          