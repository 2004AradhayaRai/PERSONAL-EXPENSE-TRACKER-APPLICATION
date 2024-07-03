import csv
import datetime
import calendar
class Expense:

    def __init__(self,name,category,amount):
        self.name=name
        self.category=category
        self.amount=amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, Rs{self.amount:.2f} >"

from expense import Expense  # type: ignore
def main():
    print("Running Expense Tracker!")
    expenses_file_path = "Expenses Tracker.csv"
    budget = 3000
    Account_name=input("Enter Account User Name: ")
    print(Account_name)

    #Get user input for expnse
    expense = get_user_expense()


    #Write their expense to a file
    save_expense_to_file(expense, expenses_file_path)


    #Read file and summarize expense
    summarize_expense(expenses_file_path,budget)

   
def get_user_expense():
    print("Getting your expense")
    expense_name=input("Enter Expene Name:")
    expense_amount=float(input("Enter Expene amount"))
    expense_categories=["Food","Home","Work","Fun","Travel","Saving","Misc","Exit"]

    while True:
        print("Select a Category: ")
        for i, category_name in enumerate(expense_categories): #enumerate provide index as well as value for ecah item
            print(f" {i + 1}. {category_name}")

        value_range = f"[1- {len(expense_categories)}]"

        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category= expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category= selected_category, amount = expense_amount)
            return  new_expense
        else:
            print("Invalid category.Please try again")
        


def save_expense_to_file(expense: Expense, expenses_file_path):
    print(f"Saving Your Expense: {expense} to {expenses_file_path}")
    with open (expenses_file_path,"a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expense(expenses_file_path, budget):
    print("Summarize User expense")
    expenses: list[Expense]=[]
    with open (expenses_file_path,"r") as f:
        lines= f.readlines()
        for line in lines:
            stripped_line=line.strip() #Return a copy of the string with leading and trailing whitespace removed.
            expense_name,expense_category,expense_amount=stripped_line.split(",")
            
            line_expense=Expense(name=expense_name,category=expense_category,amount=float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses By category")
    for key, amount in amount_by_category.items():
        print(f" {key}: Rs{amount:2f}")

    total_expense= sum([expense.amount])  
    print(f"You have spent Rs{sum([expense.amount]):.2f} this month!") 

    remaining_budget=budget-total_expense
    if remaining_budget <=0:
        print("You have gone over budget this month by Rs ",remaining_budget)
    else:
        print(f"Budget Remaining: Rs{remaining_budget:.2f}")

    today = datetime.date.today()
    last_day_of_month = calendar.monthrange(today.year, today.month)[1]
    remaining_days = last_day_of_month - today.day
    print(f"Remaining days in the month: {remaining_days}")
    daily_budget=remaining_budget/remaining_days
    
    if daily_budget>0:
        print(f"Budget per day: Rs{daily_budget}")
    else:
        print("Not enough budget for daily expenses")


if __name__=="__main__":
    main()
