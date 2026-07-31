# finance_helpers.py
# the imported module with functions

def format_currency(amount):
    # turns a number into money looking text like $12.50
    money = "$" + str(round(amount, 2))
    return money
 
 
def get_valid_amount(prompt):
    # keeps asking until they type a real number
    good_input = False
    amount = 0
    while good_input == False:
        user_input = input(prompt)
        try:
            amount = float(user_input)
            if amount < 0:
                print("that has to be a positive number")
            else:
                good_input = True
        except ValueError:
            print("that is not a number, try again")
    return amount
 
