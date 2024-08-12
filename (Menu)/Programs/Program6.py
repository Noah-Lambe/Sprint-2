# Zackery Strickland
# Date: Fri, Aug, 9
# Python Sprint Profit Listing

def main():
    # Imports
    import datetime
    import os

    # Functions
    def ValidateDate(DateStr):
        try:
            datetime.datetime.strptime(DateStr, "%Y-%m-%d")
            return True 
        except ValueError:
            return False 

    # Constants
    Today = datetime.datetime.now()

    # Input
    while True:
        StartDateStr = input("Please enter the start date (YYYY-MM-DD): ")
        if ValidateDate(StartDateStr):
            StartDate = datetime.datetime.strptime(StartDateStr, "%Y-%m-%d")
            print("Date is valid and in the correct format.")
            break
        else:
            print("Date is invalid or not in the correct format. Please try again.") 

    while True:
        EndDateStr = input("Please enter the end date (YYYY-MM-DD): ")
        if ValidateDate(EndDateStr):
            EndDate = datetime.datetime.strptime(EndDateStr, "%Y-%m-%d")
            print("Date is valid and in the correct format.")
            break
        else:
            print("Date is invalid or not in the correct format. Please try again.") 

    # Processing
    RevenueData = []
    with open('Revenues.dat', mode='r') as file:
        Lines = file.readlines()
        for Line in Lines[1:]:
            Row = Line.strip().split(', ')
            Date = datetime.datetime.strptime(Row[2], '%Y-%m-%d')
            if StartDate <= Date <= EndDate:
                RevenueData.append(Row)

    TotalRevenue = sum(float(Row[6].replace('$', '').replace(',', '')) for Row in RevenueData)

    ExpenseData = []
    with open('Expenses.dat', mode='r') as file:
        Lines = file.readlines()
        for Line in Lines[1:]:
            Row = Line.strip().split(', ')
            Date = datetime.datetime.strptime(Row[1], '%Y-%m-%d')
            if StartDate <= Date <= EndDate:
                ExpenseData.append(Row)

    TotalExpense = sum(float(Row[10].replace('$', '').replace(',', '')) for Row in ExpenseData)

    TotalNetIncome = TotalRevenue - TotalExpense

    # Displaying Totals
    TotalRevenueDSP = "${:,.2f}".format(TotalRevenue)
    TotalExpenseDSP = "${:,.2f}".format(TotalExpense)
    TotalNetIncomeDSP = "${:,.2f}".format(TotalNetIncome)

    # Output
    print(f"HAB Taxi Services") 
    print()
    print(f"Profit Listing Report as of YYYY-MM-DD") 
    print()
    print(f"Start Date To End Date") 
    print(f"{StartDateStr:>10s}")
    print(f":") 
    print(f"{EndDateStr:>10s}") 
    print()
    print()
    print(f"Revenue") 
    print() 
    print(f"{'Transaction':<15}{'Driver':<15}{'Date':<15}{'Description':<25}{'Amount':<10}{'HST':<10}{'Total':<10}")
    print(f"{'ID’s':<15}{'Number’s':<15}{'Transaction’s':<15}{'Transaction’s':<25}{'Amount’s':<10}{'HST’s':<10}{'Revenues':<10}")
    print(f"{'='*98}") 
    for row in RevenueData:
        print(f"{row[0]:<15}{row[1]:<15}{row[2]:<15}{row[3]:<25}{row[4]:<10}{row[5]:<10}{row[6]:<10}")
    print(f"{'='*98}") 
    print(f"Total Revenue") 
    print()
    print(f"{TotalRevenueDSP}")																					 
    print()
    print(f"{'-'*142}") 
    print()
    print(f"Expenses") 
    print()
    print()
    print()
    print(f"{'Invoice':<15}{'Invoice':<15}{'Driver':<15}{'Item':<15}{'Item':<25}{'Item':<10}{'Item':<10}{'Item':<10}{'':<10}{'':<10}{'Total':<10}") 
    print(f"{'Number':<15}{'Date':<15}{'Number':<15}{'Number':<15}{'Description':<25}{'Cost':<10}{'Quantity':<10}{'Total':<10}{'Subtotal':<10}{'HST':<10}{'Expense':<10}") 
    print(f"{'='*142}") 
    for row in ExpenseData:
        print(f"{row[0]:<15}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:<25}{row[5]:<10}{row[6]:<10}{row[7]:<10}{row[8]:<10}{row[9]:<10}{row[10]:<10}")
    print(f"{'='*142}") 
    print(f"Total Expenses") 
    print()
    print(f"{TotalExpenseDSP}")
    print()
    print(f"{'-'*142}") 
    print()
    print(f"Total Net Income = Monthly Revenue – Monthly Expense")  
    print()
    print()
    print()
    print(f"{TotalNetIncomeDSP}") 
    print()

if __name__ == "__main__":
    main()
