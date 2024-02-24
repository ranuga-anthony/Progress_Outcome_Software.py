# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953811
# Date: 13/12/2022

print("Progress outcome software")
print()
progress = 0
trailer = 0
retriever = 0
exclude = 0
dict1 = {}


def prompt_username():
    """ Prompt the user to enter username.
    Last modified 13/12/2022 """
    global username #https://www.geeksforgeeks.org/global-local-variables-python/
    
    while True:
        username = input("Please enter your username:")
        if len(username)==8 and username[0] == 'w': #validate the username assuming that the username is westminster username
            pass
        else:
            print("Invalid Username...Please try again.")
            continue
        if username in dict1: #validate the username by checking whether the username already exists
            print('Username already existing...Please enter a different username')
            continue
        else:
            break

def prompt_user_inputs():
    """ Prompt the user to input pass,defer,fail credits.
    Last modified 13/12/2022 """
    global pass_credits,defer_credits,fail_credits #https://www.geeksforgeeks.org/global-local-variables-python/
    while True:
        try:
            pass_credits = int(input("Enter your total PASS credits:")) 
            if pass_credits >= 0 and pass_credits <=120 and pass_credits % 20 ==0:
                break
            else:                                       #validating the input data
                print("Out of range.")
                continue
        except ValueError: 
            print('Integer required.')
            continue
        

    while True:
        try:
            defer_credits = int(input("Enter your total DEFER credits:"))
            if defer_credits >= 0 and defer_credits <=120 and defer_credits % 20 ==0:
                break
            else:                                       #validating the input data
                print("Out of range.")
                continue
        except ValueError:
             print('Integer required.')
             continue

    while True:
        try:
            fail_credits = int(input("Enter your total FAIL credits:"))
            if fail_credits >= 0 and fail_credits <=120 and fail_credits % 20 ==0:
                break
            else:                                       #validating the input data
                print("Out of range.")
                continue
        except ValueError:
            print('Integer required.')
            continue 


    
while True:
    tlist = [] #initialise tlist as an empty list
    prompt_username() #calling the username prompt function
    prompt_user_inputs() #calling the user input prompt function  
    
    total_credits = pass_credits + defer_credits + fail_credits
    
    tlist = [str(pass_credits) +',',str(defer_credits) + ',',str(fail_credits)] #include input progression data to tlist
    
    if total_credits != 120: # to prevent credits leading to incorrect totals from proceeding forward
        print("Total incorrect")
        continue
    else:
        if pass_credits == 120:
            print()
            print("Progress")
            progress = progress + 1
            
            # include Progression outcome into a list
            tlist.insert(0,'Progress =')

            #include the list into a dictionary
            dict1[username] = tlist

            
        
        elif pass_credits == 100:
            print("Progress(Module Trailer)")
            trailer = trailer + 1
            # include progression outcome into tlist
            tlist.insert(0,'Progress (module trailer) =')
            dict1[username] = tlist
            
            
        elif fail_credits == 80 or fail_credits == 100 or fail_credits == 120:
            print("Exclude")
            exclude = exclude + 1
            #include progression outcome into tlist
            tlist.insert(0,str("Exclude ="))
            dict1[username] = tlist
            
            
        else:
            print("Module retriever")
            retriever = retriever + 1
            #include input progression data into tlist 
            tlist.insert(0,str("Module retriever ="))
            dict1[username] = tlist
            
            
    while True:   # Prompt user to input whether to continue
        print()
        print("Would you like to enter another set of data?")
        user_reply = input("Enter 'y' for yes or 'q' to quit and view result:")
        print()
        if user_reply.lower() == "y" or user_reply == "q" :
            break
        else:
            print('Invalid Input.Please Try again.')
            continue

    if user_reply.lower() == "y":
        continue
    else:
        break

# Print the histogram
print()
print("-------------------------------------------------------------------------------------")
print("Histogram")
print()
print('Progress',progress,'\t:','*' * progress)
print('Trailer',trailer,'\t:','*' * trailer)
print('Retriever',retriever,'\t:','*' * retriever)
print('Exclude',exclude,'\t:','*' * exclude)
outcomes = progress + trailer + retriever + exclude
print(outcomes," outcomes in total.")
print("------------------------------------------------------------------------------------")
print()
    
print("Part 4")
for key, value in dict1.items():
    print(key,':',end = "") #Print the keys in the dictionary
    print(*value) #https://realpython.com/python-print/ #Print the values in the dictionary




