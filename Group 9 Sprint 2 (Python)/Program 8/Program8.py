# Description: Summary Report for HAB taxi service
# Authors: Frank Holdbrook, Noah Whiffen, Jonathan Strickland, Jack Williams, Noah Lambe, Group 9 SD12
# Dates: August 10, 2024 - August 11, 2024

# Define program main function.
def main():
    # Define required libraries.
    import csv
    import os
    from datetime import datetime, timedelta
    import datetime
    
    # Define program constants.
    currentDate = datetime.date.today()
    REVENUES_FILE = 'Revenues.dat'
    EXPENSES_FILE = 'Expenses.dat'

    # Define program functions.
    def FDollar2(DollarValue):
        DollarValueStr = "${:,.2f}".format(DollarValue)
        return DollarValueStr

    def load_revenues():
        revenues = []
        with open(REVENUES_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                revenues.append(row)
        return revenues

    def load_expenses():
        expenses = []
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
        return expenses

    # Initialize counters and accumulators
    revenues = load_revenues()
    expenses = load_expenses()
    total_revenue = 0
    total_expense = 0
    driverOneRevenue = 0
    driverTwoRevenue = 0
    driverThreeRevenue = 0
    driverFourRevenue = 0
    driverFiveRevenue = 0
    driverSixRevenue = 0
    totalRides = 0
    
    # Perform Calculations
    for revenue in revenues:
        
        total_revenue += float(revenue[6])
        
        if revenue[1] == " 001":
            driverOneRevenue += float(revenue[6])

        if revenue[1] == " 002":
            driverTwoRevenue += float(revenue[6])

        if revenue[1] == " 003":
            driverThreeRevenue += float(revenue[6])

        if revenue[1] == " 004":
            driverFourRevenue += float(revenue[6])

        if revenue[1] == " 005":
            driverFiveRevenue += float(revenue[6])

        if revenue[1] == " 006":
            driverSixRevenue += float(revenue[6])

        totalRides += 1

    for expense in expenses:
        total_expense += float(expense[9])

    # Format Values
    driverOneRevenueDSP = FDollar2(driverOneRevenue)
    driverTwoRevenueDSP = FDollar2(driverTwoRevenue)
    driverThreeRevenueDSP = FDollar2(driverThreeRevenue)
    driverFourRevenueDSP = FDollar2(driverFourRevenue)
    driverFiveRevenueDSP = FDollar2(driverFiveRevenue)
    driverSixRevenueDSP = FDollar2(driverSixRevenue)

    total_revenueDSP = FDollar2(total_revenue)
    total_expenseDSP = FDollar2(total_expense)
    netProfit = total_revenue - total_expense
    netProfitDSP = FDollar2(netProfit)
        
    # Display summary report
    print()
    print("HAB Taxi Services")
    print(f"Revenue Summary Report as of {currentDate}")
    print()
    print(f"Driver 001:                    Total revenue of   {driverOneRevenueDSP:>10s}")
    print(f"Driver 002:                    Total revenue of   {driverTwoRevenueDSP:>10s}")
    print(f"Driver 003:                    Total revenue of   {driverThreeRevenueDSP:>10s}")
    print(f"Driver 004:                    Total revenue of   {driverFourRevenueDSP:>10s}")
    print(f"Driver 005:                    Total revenue of   {driverFiveRevenueDSP:>10s}")
    print(f"Driver 006:                    Total revenue of   {driverSixRevenueDSP:>10s}")
    print()
    print(f"Total Rides: {totalRides}")
    print("="*60)
    print(f"Total Revenues:                                   {total_revenueDSP:>10s}")
    print(f"Expense Cost:                                     {total_expenseDSP:>10s}")
    print(f"Net Profit:                                       {netProfitDSP:>10s}")

if __name__ == "__main__":
    main()
