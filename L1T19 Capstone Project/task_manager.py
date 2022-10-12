#=====importing libraries===========
import datetime

#====Login Section====

inputed_credentials = False # Declaring variable inputed_credentials which will be used as a control variable in while loop
# Initializing while loop to validate user name and password. 
while inputed_credentials == False:  

    # Request user input(username and password). 
    username = input("Please enter your username:\t")
    password = input("Please enter your password:\t")

    # Below line creates file object named users which will be used to read and verify inputed data from user.
    users = open("user.txt","r+")

    # Reading in credentials from user.txt
    for line in users:

        # Declaring a temporary list which will be used to store username and password from each line.
        credentials_list = line.split(',')

        # Checking if credentials match
        if credentials_list[0].strip() == username and credentials_list[1].strip() == password:

            # Update Control Variable
            inputed_credentials = True

            # Displaying welcome text
            print("\n\n\t\t\t***** Welcome *****\n\n\n")

            # If user has been match. Break out of loop.
            break
    
    #Closing file object
    users.close()
#=====================================================================================================================



while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username != "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    ds - Display statistics
    e - Exit
    : ''').lower()
    if menu == 'r':
        pass
        # Checking if user has username of 'admin'
        if(username == 'admin'):

            # Requesting user input.
            new_user_username = input("Please enter username for new user:\t")
            new_user_password = input("Please enter password for new user:\t")
            new_user_confirm_password = input("Please confirm password for new user:\t")

            # Checking if passwords match
            if new_user_password == new_user_confirm_password :
                
                # Below line creates file object named login_credentials which will be used to add new users.
                login_credentials = open("user.txt","a")

                # Writing new user credentials to user.txt
                login_credentials.write(f"\n{new_user_username}, {new_user_password}")

                #Closing file object
                login_credentials.close()

                # Displaying Success Message
                print("Credentials have been saved")

            else:

                # Displaying Relevant Message
                print("Passwords do not match. Please try again")
        
        else:
            print("Only admin can add users")

    elif menu == 'a':
        pass
        # Requesting user input.
        task_username = input("Please enter username of the person whom the task is assigned to:\t")
        task_title = input("Please enter title of task:\t")
        task_description = input("Please enter description of task:\t")
        task_current_date = datetime.date.today().strftime('%d %b %Y')
        task_due_date = input("Please enter task due date:\t")
        task_completed = input("Has task been completed? Please enter yes or no:\t").lower()
    
        if task_completed != "yes":

            # Update variable task_completed
            task_completed = "No"
            
        else:

            # Update variable task_completed
            task_completed = "Yes"

        # Creating file object named new_tasks which will be used to write data to the tasks.txt
        new_tasks = open('tasks.txt','a')
        
        # Writing data to tasks.txt
        new_tasks.write(f"\n{task_username}, {task_title}, {task_description}, {task_current_date}, {task_due_date}, {task_completed}")

        # Clsoing the file object
        new_tasks.close()

        # Displaying Success Message
        print("Task has been saved")

    elif menu == 'va':
        pass
        # Creating file object where data will be read from
        tasks = open('tasks.txt','r')

        # Displaying Contents
        for line in tasks:

            # Creating list which will store details of each task
            task_list = line.split(',')

            # Displaying Contents
            print(f"Task:\t\t\t{task_list[1].strip()}")
            print(f"Assigned to:\t\t{task_list[0].strip()}")
            print(f"Date assigned:\t\t{task_list[3].strip()}")
            print(f"Due date:\t\t{task_list[4].strip()}")
            print(f"Task Complete:\t\t{task_list[-1].strip()}")
            print(f"Task description:\n {task_list[2]}\n")

        # Closing the object
        tasks.close()
    elif menu == 'vm':
        pass
        # Creating file object where data will be read from
        tasks = open('tasks.txt','r')

         # Displaying Contents
        for line in tasks:

            # Creating list which will store details of each task
            task_list = line.split(',')

            # Checking if tasked assigned to username matches logged in user.
            if username == task_list[0].strip():

                # Displaying Contents
                print(f"Task:\t\t\t{task_list[1].strip()}")
                print(f"Assigned to:\t\t{task_list[0].strip()}")
                print(f"Date assigned:\t\t{task_list[3].strip()}")
                print(f"Due date:\t\t{task_list[4].strip()}")
                print(f"Task Complete:\t\t{task_list[-1].strip()}")
                print(f"Task description:\n {task_list[2]}\n")
        
        tasks.close()
    elif menu == 'ds':

        # Creating file object to read from to get the total number of users
        count_users = open('user.txt','r')

        # Creating variable which will be used to display the total number of users
        number_of_users = 0

        # Initializing for loop to get the number of users.
        for line in count_users:
            
            # Updating number_of_tasks
            number_of_users +=1

        # Creating file object to read from to get the total number of tasks
        count_tasks = open('tasks.txt','r')

        # Creating variable which will be used to display the total number of tasks
        number_of_tasks = 0

        # Initializing for loop to get the number of tasks.
        for line in count_tasks:

            # Updating number_of_tasks
            number_of_tasks += 1
        
        # Displaying Results to user
        print(f"The total number of tasks is:\t{number_of_tasks}")
        print(f"The total number of users is:\t{number_of_users}")
        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

