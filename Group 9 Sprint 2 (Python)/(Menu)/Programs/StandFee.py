# Title:       Python Final Sprint - Stand Fee
# Description: A program to calculate the 
#              stand fee for HAB Taxi Services
# Author:      Noah Whiffen, Jonathan Strickland, Noah Lambe - SD12 - Robot Group 9
# Date:        August 6th, 2024 - August 12th, 2024

def main():
    # Define program libraries
    import datetime
    import csv

    # Define program constants.
    with open("Defaults.dat", "r") as file:
        f = file.readlines()
        nextTransNum = f[0].strip()
        nextTransNum = int(nextTransNum)
        nextDriverNum = f[1].strip()
        standFee = f[2].strip()
        standFee = float(standFee)
        dailyRentFee = f[3].strip()
        dailyRentFee = float(dailyRentFee)
        weekRentFee = f[4].strip()
        weekRentFee = float(weekRentFee)
        HSTRate =  f[5].strip()
        HSTRate = float(HSTRate)

    today = datetime.datetime.today()

    # Define program constants
    def load_employees():
        employees = []
        with open('Employees.dat', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                employees.append(row)
        return employees

    # Perform Calculations
    standFeeHST = standFee * HSTRate
    standFeeTotal = standFeeHST + standFee
    employees = load_employees()
    
    # Update Revenues.dat with monthly stand fees
    for employee in employees:
        if today.day == 1:
            if employee[8] == " Yes":
                driverNum = employee[0]
                with open("Revenues.dat", "a") as f:
                    f.write(f"{nextTransNum}, {driverNum}, {today}, Monthly Stand Fees, {standFee}, {standFeeHST}, {standFeeTotal}\n")
                    nextTransNum += 1

if __name__ == "__main__":
    main()