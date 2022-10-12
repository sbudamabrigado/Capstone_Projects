# Creating Classes

class Shoes:
    def __init__(self,country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # Defining the required methods
    def get_cost(self):
        #Return cost of Shoe
        return self.cost
    
    def get_quantity(self):
        #Return quantity of Shoe
        return self.quantity
    
    def __str__(self):
        # Return string representation of class
        return f'''
        Country = {self.country}
        Code = {self.code}
        Product = {self.product}
        Cost = {self.cost}
        Quantity = {self.quantity}'''

# Declare empty list to store shoe objects
shoes_list = [] 

# Defining relevant functions outside of class Shoes

def read_shoes_data():
    # Create file object to read from.
    inventory_txt = open('inventory.txt','r')
    
    # Using the try except in this function for error handling.
    try:
        # Declare for loop to loop through the file and create shoe objects
        # When shoe objects are created they will be appended to the shoes_list
        for count,line in enumerate(inventory_txt,start = 0):
            # Check if count is 0.
            if count == 0:
                # Skip current iteration. First Line represents data to create one object of shoes
                continue
            
            # Create a list of object attributes from the line
            object_details = line.split(',')
            
            #Create Shoe object
            shoe = Shoes(object_details[0].strip(),object_details[1].strip(),object_details[2].strip(),object_details[3].strip(),object_details[4].strip())
            
            # Append to shoe list
            shoes_list.append(shoe)
        # Close the file object
        inventory_txt.close()

        # Display success message
        print("\nData has been read successfully\n")

    except Exception as exception:
        print("Unfortunately an error has occured! Please see below for more details:\n\n")
        print(exception)
       
def capture_shoes():
    # Request input from user
    country = input("Please input shoe country:\t")
    code = input("Please input shoe code:\t")
    product = input("Please enter shoe name:\t")
    cost = input("Please enter cost of shoe:\t")
    quantity = input("Please enter shoe quantity:\t")

    # Create shoe object
    shoe = Shoes(country, code, product, cost,quantity)

     # Clear list and reload to get latest information
    shoes_list.clear()
    read_shoes_data()

    # Append to list
    shoes_list.append(shoe)

    # Update inventory.txt
    # Create file object to write to.
    inventory_txt = open('inventory.txt','w')
    
    # Write first line which represents data to create one object of shoes
    inventory_txt.write(f"Country,Code,Product,Cost,Quantity\n")

    # Declare for loop to loop through the shoe list and update inventory.txt
    for shoe in shoes_list:
        # Write to invntory.txt
        inventory_txt.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    
    # Close the file object
    inventory_txt.close()

    # Display success message
    print("\nShoe was successfully captured\n")
    
def view_all():
    # Declare for loop to iterate over all the shoes list and print the details of the shoes
    for shoe in shoes_list:
        print()
        print(shoe.__str__())
    print()

def re_stock():
    # Clear list and reload to get latest information
    shoes_list.clear()
    read_shoes_data()
    # for index_position, shoe in enumerate(shoes_list, start = 0):
    # Declare variable quantity which will be used to find the lowest quantity
    quantity = int(shoes_list[0].quantity)

    # Declare variable position which will get the postion(index) f object with lowest quantity
    index_position = 0
    # Declare for loop to loop through the list and find the shoe with lowest quantity
    for index, shoe in enumerate(shoes_list, start = 0):
        # Check if quantity of object is more than variable quantity
        if int(shoe.quantity) <= quantity:
            # Update variable quantity
            quantity = int(shoe.quantity)
            index_position = index
    
    # Display the Product with lowest quantity
    print(f"{shoes_list[index_position].product} has got a quantity of  {shoes_list[index_position].quantity} which is the lowest quantity")
    
    # Ask user if they would like to update stock ?
    user_input = input("Would you like to update the quantity? Type yes or no:\t").lower()
    if user_input == "yes":
        # Request user input
        updated_quantity = input("Please enter the value of the updated quantity:\t")
        
        # Check user entered valid input
        if updated_quantity.isdigit():
            #Update the quantity
            shoes_list[index_position].quantity = updated_quantity

            # Update inventory.txt
            # Create file object to write to.
            inventory_txt = open('inventory.txt','w')
            
            # Write first line which represents data to create one object of shoes
            inventory_txt.write(f"Country,Code,Product,Cost,Quantity\n")

            # Declare for loop to loop through the shoe list and update inventory.txt
            for shoe in shoes_list:
                # Write to invntory.txt
                inventory_txt.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            
            # Close the file object
            inventory_txt.close()

            # Display Success message
            print("\nShoe updated successfully\n")
        else:
            # Display relevant message
            print("Invalid Input")

            # Break out of function
            return
    elif user_input == "no":
        # Display relevant message
        print("GoodBye!!")

        # Break out of function
        return
    else:
        # Display relevant message
        print("Invalid Input")

        # Break out of function
        return

def search_shoe(shoe_code):
    # Declare for loop to loop through the shoe list and search for the shoe using code

    # Variable to check if shoe not found
    shoe_not_found = True
    for shoe in shoes_list:
        if shoe.code.strip() == shoe_code:
            # Display the shoe details
            print(f"{shoe.__str__()}\n")

            # Update variable 
            shoe_not_found = False

    # Check if shoe was found
    if shoe_not_found:
        # Display relevant message
        print("\nNo matches found for shoe code\n")


def value_per_item():
    # Declare for loop to loop through the shoe list and search for the shoe using code
    for shoe in shoes_list:
        # Calculate value for each object
        value = float(shoe.get_cost()) * int(shoe.get_quantity())
        # Display details
        print(f"\n{shoe.__str__()}")
        print(f"\tValue = {value}\n")
    
def highest_qty():
    # Declare variable quantity which will be used to find the highest quantity
    quantity = 0

    # Declare variable product which will be used to store the product with the highest quantity
    product = ""

    # Declare varaible cost which will store the cost of the product with the highest quantity
    cost = 0
    # Declare for loop to loop through the shoe list and find the highest quantity
    for shoe in shoes_list:
        if int(shoe.get_quantity())>= quantity:
            # Update Variables
            quantity = int(shoe.get_quantity())
            product = shoe.product
            cost = shoe.cost

    # Display shoe as being for sale
    print(f"\t\t\t*** Sale Sale Sale ***\n\n A pair of {product} only cost {cost}\n Get it while stocks last\n\n")

try:
    while True:
        # Presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following Options below:
        rs - Read data into shoe list
        as - Add a Shoe
        vs - View all shoes
        us - Update shoe with low quantity
        ss - Search for shoe
        sv - Get values for shoes
        hs - Get shoe with highest quantity and put up for sale
        e  - Exit
        : ''').lower()
        
        # Based on input call relevant function
        if menu == 'rs':
            read_shoes_data()

        elif menu == 'as':
            capture_shoes()

        elif menu == 'vs':
            view_all()

        elif menu == 'us':
            re_stock()

        elif menu == 'ss':
            # Request user input
            shoe_code = input("Please enter shoe code:\t")

            search_shoe(shoe_code)
            
        elif menu == 'sv' :
            value_per_item()

        elif menu == 'hs':
            highest_qty()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
            
except Exception as exception:
    print("Oops unfortunately an error. Please see below for error details.\n")
    print("************************************************************************************************************************************************")
    print(exception)
    print("************************************************************************************************************************************************")


