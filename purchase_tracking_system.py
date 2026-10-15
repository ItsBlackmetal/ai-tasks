# The first part of the task

# Displaying the system name and greeting
print('YOURGOODS PURCHASE TRACKING SYSTEM')
print('Hello, dear user. We hope you enjoy using our purchase tracking system')

# Declaring lists to store product names and their prices
product_names = []
prices = []

# Creating a variable that will store the user's budget
budget = input('Specify the capital available for purchases: ')

# The second part of the task
while True:
    print('PURCHASE ACCOUNTING MENU\n\n1. Add an item\n2. Show all items\n3. Calculate total cost\n4. Check budget\n5. Find the most expensive and cheapest items\n6. Remove an item\n7. Show statistics\n8. Exit the program\n')
    operation_number = input('Enter your choice: ')

# Part three of the task
    if operation_number == '1':
# A part of the program that enables the first operation from the aforementioned list. It allows the user to enter a product name and price, converts the price into a number, verifies that the name is not empty and that the price is greater than zero but less than $10,000, and adds these values to the corresponding lists — while displaying messages for other scenarios
    user_product_name = input('Product name: ')
    if user_product_name == True:
        product_names.append(user_product_name)
    else:
        print('Please, enter a product name')
    user_product_cost = int(input('Cost of the product: '))
    if user_product_cost > 0 and user_product_cost == 10000:
        prices.append(user_product_cost)
    else:
        print('Enter the price of the item, which must be greater than zero and less than $10.000')

    elif operation_number == '2':
    elif operation_number == '3':
    elif operation_number == '4':
    elif operation_number == '5':
    elif operation_number == '6':
    elif operation_number == '7':
    elif operation_number == '8':
    else:
         print('Enter one of the suggested operations')