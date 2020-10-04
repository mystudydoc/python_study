print("Welcome xyz.org.")

# Initialize a List of users and passwords
# Using two lists for quick prototyping.
# We can improve it by just maintaining a a single list with user:password combinatio.
usersList = []
usersList.append("Ayush")
usersList.append("Srushti")

# List of users and apsswords.
usersAndPasswordsList = []
usersAndPasswordsList.append("Ayush:ayush@1")
usersAndPasswordsList.append("Srushti:srushti@1")

existingAccount=input('Do you have an existing account?')
if existingAccount=="yes":
    username=input('Please type your username:')
    if username in usersList:
         password=input('Please type your password:')
         if username+":"+password in usersAndPasswordsList:
             print("You have sucessfully logged in")
         else:
             print("Incorrect Password")
    else:
        print('Username is wrong')
else:
    print('Lets create an account')
    username=input('Please type your username:')
    
    # Age is a numeric value, so need s to be typecasted to numbers.
    age=int(input('Please enter your age:'))

    if (age >=7):
        password=input('Please type your password:')
        usersList.append(username)
        usersAndPasswordsList.append(username+":"+password)
        print("Updated users list")
        print (usersList)
        print("Updated users and passwords list")
        print(usersAndPasswordsList)
        print('You have seccessfully created an account')
    else:
        print('You are not eligible to make an account')
        print("Updated users list")
        print (usersList)
    
input ("Press any key to exit...")
