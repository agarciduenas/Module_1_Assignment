# coding: utf-8
import csv
from pathlib import Path

# Part 1 Automate the Calculations.   
loan_costs = [500, 600, 200, 1000, 450]

#  How many loans are in the list?  The list has 5 loans
print(f"The total number of loans is: ", (len(loan_costs)))
total_loan_list=len(loan_costs)

# What is the total of all loans?  The sum of all loans is $2750
print(f"The total all loans is: $", (sum(loan_costs)))
loan_totals=sum(loan_costs)

# What is the average loan amount from the list?  The avg loan amount is $550
loan_average=(loan_totals/total_loan_list) 
print(f"The avrage loan amount is: $", (loan_average))

# Part 2 Analyze Loan Data

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


#Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

future_value= loan.get("future_value", 1000)
print(future_value)

remaining_months= loan.get("remaining", 9)
print(remaining_months)



# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

discount_rate= .2
present_value= future_value/ (1+ discount_rate/12)** remaining_months
print(round(present_value, 2))


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    
if present_value >= future_value:
    print("The loan is worth at least the cost to buy it")
elif present_value == future_value:
    print("The loan is eqaul to the future value")    
else:
    print("The loan is too expensive and not the worth the price")


# Part 3: Perform Financial Calculations

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

def preset_value(future_value, remaining_months, discount_rate):
    present_value= (future_value)/(1+discount_rate/12)**remaining_months

    future_value= new_loan.get("future_value", 1000)
    print(future_value)

    remaining_months= new_loan.get("remaining", 12)
    print(remaining_months)


    present_value= future_value/ (1+ discount_rate/12)** remaining_months
    print(round(present_value, 2))

    return present_value

# @Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

print(f"The present value of the loan is: {present_value: .2f}") #discount rate never changed .2 = 20%

# Part 4: Conditionally filter lists of loans
#In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

#1. Create a new, empty list called `inexpensive_loans`.
#2. Use a for loop to select each loan from a list of loans.
#    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
#    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
#3. Print the list of inexpensive_loans.

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    }
]

# @Create an empty list called `inexpensive_loans`
inexpensive_loans=[]

# @Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
#inexpensive_loans=  [price for price in loans if price["loan_price"]<=500]  THIS SETUP IS GOOD BUT THE OUTPUT GENERATES TWO ENTRIES FOR THE 500 LOAN
for price in loans:
    if price["loan_price"]== 500:
        inexpensive_loans.append(price)
    elif price["loan_price"]<500:
         inexpensive_loans.append(price)
# only two loans are =< 500
# @ Print the `inexpensive_loans` list  
print(inexpensive_loans)


#Part 5: Save the results.

#Output this list of inexpensive loans to a csv file
#    1. Use `with open` to open a new CSV file.
        #a. Create a `csvwriter` using the `csv` library.
        #b. Use the new csvwriter to write the header variable as the first row.
        #c. Use a for loop to iterate through each loan in `inexpensive_loans`.
        #    i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    #Hint: Refer to the official documentation for the csv library.
    #https://docs.python.org/3/library/csv.html#writer-objects


# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")
print("Writing the data to a CSV file...")
# @Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.


with open(output_path,'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for row in inexpensive_loans:
            csvwriter.writerow(row.values())