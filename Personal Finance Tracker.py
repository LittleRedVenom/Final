#Personal Finance Tracker
 
import finance_helpers
  
# CLASSES
 
class BudgetItem:
    # this is the parent class, income and expense both come from this
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
 
    def display(self):
        return self.name + " " + str(self.amount)
 
 
class Income(BudgetItem):
    # sub class of BudgetItem for money coming in
    def __init__(self, name, amount, category, source):
        self.name = name
        self.amount = amount
        self.category = category
        self.source = source
 
    def display(self):
        text = "[INCOME] " + self.name + " from " + self.source + ": " + finance_helpers.format_currency(self.amount)
        return text
 
 
class Expense(BudgetItem):
    # sub class of BudgetItem for money going out
    def __init__(self, name, amount, category, is_recurring):
        self.name = name
        self.amount = amount
        self.category = category
        self.is_recurring = is_recurring
 
    def display(self):
        if self.is_recurring == True:
            r = "recurring"
        else:
            r = "one-time"
        text = "[EXPENSE] " + self.name + ", " + self.category + " (" + r + "): " + finance_helpers.format_currency(self.amount)
        return text
 
 
class Budget:
    # this class holds all the income and expenses together
    def __init__(self, period):
        self.period = period
        self.income_list = []
        self.expense_list = []
        self.savings_goal = 0
 
    def add_income(self, income_obj):
        self.income_list.append(income_obj)
 
    def add_expense(self, expense_obj):
        self.expense_list.append(expense_obj)
 
    def total_income(self):
        total = 0
        for i in range(len(self.income_list)):
            total = total + self.income_list[i].amount
        return total
 
    def total_expenses(self):
        total = 0
        for i in range(len(self.expense_list)):
            total = total + self.expense_list[i].amount
        return total
 
    def save_summary_to_file(self, filename="budget_summary.txt"):
        # writes out everything to a txt file
        try:
            file = open(filename, "w")
            file.write("=== PERSONAL BUDGET SUMMARY ===\n")
            file.write("Period: " + self.period + "\n\n")
 
            file.write("--- Income ---\n")
            for i in range(len(self.income_list)):
                file.write(self.income_list[i].display() + "\n")
            total_in = self.total_income()
            file.write("Total Income: " + finance_helpers.format_currency(total_in) + "\n\n")
 
            file.write("--- Expenses ---\n")
            for i in range(len(self.expense_list)):
                file.write(self.expense_list[i].display() + "\n")
            total_out = self.total_expenses()
            file.write("Total Expenses: " + finance_helpers.format_currency(total_out) + "\n\n")
 
            balance = total_in - total_out
            file.write("Remaining Balance: " + finance_helpers.format_currency(balance) + "\n")
            file.write("Savings Goal: " + finance_helpers.format_currency(self.savings_goal) + "\n")
 
            if balance >= self.savings_goal:
                file.write("Status: you are on track for your savings goal\n")
            else:
                file.write("Status: you are not meeting your savings goal yet\n")
 
            file.close()
            print("saved to " + filename)
        except:
            #Ecption
            print("something went wrong saving the file")
 
 #functions
 
def add_income_menu(budget):
    name = input("Enter income name (ex. Paycheck): ")
    source = input("Enter income source (ex. Job, Gift): ")
    amount = finance_helpers.get_valid_amount("Enter income amount: $")
    new_income = Income(name, amount, "Income", source)
    budget.add_income(new_income)
    print("Income added!")
    print("")
 
 
def add_expense_menu(budget):
    name = input("Enter expense name (ex. Rent): ")
    category = input("Enter expense category (ex. Housing, Food): ")
    amount = finance_helpers.get_valid_amount("Enter expense amount: $")
    recurring_input = input("Is this recurring? (y/n): ")
    if recurring_input == "y" or recurring_input == "Y":
        is_recurring = True
    else:
        is_recurring = False
    new_expense = Expense(name, amount, category, is_recurring)
    budget.add_expense(new_expense)
    print("Expense added!")
    print("")
 
def view_budget(budget):
    print("")
    print("--- Income ---")
    if len(budget.income_list) == 0:
        print("no income yet")
    for item in budget.income_list:
        print(item.display())
 
    print("--- Expenses ---")
    if len(budget.expense_list) == 0:
        print("no expenses yet")
    for item in budget.expense_list:
        print(item.display())
 
    total_in = budget.total_income()
    total_out = budget.total_expenses()
    print("")
    print("Total Income: " + finance_helpers.format_currency(total_in))
    print("Total Expenses: " + finance_helpers.format_currency(total_out))
    print("Remaining Balance: " + finance_helpers.format_currency(total_in - total_out))
    print("Savings Goal: " + finance_helpers.format_currency(budget.savings_goal))
    print("")
 
def main():
    print("=== Welcome to the Personal Finance Tracker ===")
    print("")
 
    period = input("Are you budgeting monthly or weekly? ")
    my_budget = Budget(period)
 
    goal = finance_helpers.get_valid_amount("Enter your savings goal: $")
    my_budget.savings_goal = goal
 
    running = True
    while running == True:
        print("What would you like to do?")
        print("1. Add income")
        print("2. Add expense")
        print("3. View budget summary")
        print("4. Update savings goal")
        print("5. Save summary to file and quit")
        choice = input("Enter your choice (1-5): ")
 
        if choice == "1":
            add_income_menu(my_budget)
        elif choice == "2":
            add_expense_menu(my_budget)
        elif choice == "3":
            view_budget(my_budget)
        elif choice == "4":
            new_goal = finance_helpers.get_valid_amount("Enter new savings goal: $")
            my_budget.savings_goal = new_goal
            print("Savings goal updated!")
        elif choice == "5":
            my_budget.save_summary_to_file()
            running = False
        else:
            print("that is not a choice, try again")
 
    print("Thanks for using the Personal Finance Tracker. Goodbye!")
 
main()
 
