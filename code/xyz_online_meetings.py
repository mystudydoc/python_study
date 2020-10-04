print("Welcome xyz.org.")
existing_account=input('Do you have an existing account?')
if existing_account=="yes":
    username=input('Please type your username:')
    if username==('Ayush' or 'Srushti'):
         password=input('Please type your password:')
         if password==('Ayush' or 'Srushti'):
             print("You have sucessfully logged in")
         else:
             print("Incorrect Password")
    else:
        print('Username is wrong')
else:
    print('Lets create an account')
    username=input('Please type your username:')
    
    list = []
    list.append("Ayush")
    list.append("Srushti")
    
    age=input('Please enter your age:')
    if (age >=str(7)):
        list.append(username)
        print (list)
        password=input('Please type your password:')
        print('You have seccessfully created an account')
    else:
        print('You are not eligible to make an account')
        print (list)
    
