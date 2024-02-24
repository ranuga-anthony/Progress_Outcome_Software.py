# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953811
# Date: 13/12/2022


print("Progress Outcome Software..............")
print()

progress = 0
trailer = 0
retriever = 0
exclude = 0
flist = []



f = open('input_data.txt','w') #open the text file for writing
f.write('Part 3:\n')


def filewrite():
    """ Write the file using the input progression data.
    Last modified 13/12/2022 """
    f.write(outcome)
    f.write(' = ')
    f.write(str([pass_credits,defer_credits,fail_credits])[1:-1]) #write the list of progression data for each outcome in the text file
    f.write('\n')

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
    tlist = []#initialise tlist as an empty list
    prompt_user_inputs()#calling the user input prompt function
    
        
    total_credits = pass_credits + defer_credits + fail_credits
    
    if total_credits != 120: # to prevent credits leading to incorrect totals from proceeding forward
        print("Total incorrect")
        continue
    else:
        tlist = [str(pass_credits)+',',str(defer_credits)+',',str(fail_credits)] #include input progression data into tlist
        if pass_credits == 120:
            outcome = 'Progress'
            print(outcome)
            progress = progress + 1
            
            # include progresssion outcome into tlist
            tlist.insert(0,'Progress =')
            flist.append(tlist) #appending the tlist to another list called flist

            
            
            # calling on the file write function
            filewrite()
            
            
        elif pass_credits == 100:
            outcome = "Progress (Module trailer)"
            print(outcome)
            trailer = trailer + 1
            
            # include progression outcome into tlist
            tlist.insert(0,'Progress (module trailer) =')
            flist.append(tlist)
            
            # calling on the file write function
            filewrite()
            
        elif fail_credits == 80 or fail_credits == 100 or fail_credits == 120:
            outcome = "Exclude"
            print(outcome)
            exclude = exclude + 1

            # include progresssion outcome into tlist
            tlist.insert(0,'Exclude =')
            flist.append(tlist)
            
            # calling on the file write function
            filewrite()

        else:
            outcome = "Module retriever"
            print(outcome)
            retriever = retriever + 1

            # include progresssion outcome into tlist
            tlist.insert(0,'Module retriever =')
            flist.append(tlist)
            
            # calling on the file write function
            filewrite()
            
            

    
    # Prompt user to input whether to continue

    while True:
        print()
        print("Would you like to enter another set of data?")
        user_reply = input("Enter 'y' for yes or 'q' to quit and view result:")
        print()
        if user_reply.lower() == "y" or user_reply.lower() == "q":
            break
        else:
            continue

    if user_reply.lower() == 'y':
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
print('Excluded',exclude,'\t:','*' * exclude)
outcomes = progress + trailer + retriever + exclude
print()
print(outcomes," outcomes in total.")
print("------------------------------------------------------------------------------------")
print()

print("Part 2:")
for i in range(len(flist)):
    print(*flist[i]) #https://realpython.com/python-print/


f = open('Input_data.txt','r') # open the text file for reading

print()    
print(f.read()) #read the text file
f.close()


    
    
    


