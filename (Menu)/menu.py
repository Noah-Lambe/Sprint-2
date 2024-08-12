# Description: Menu for Hab Taxi Services various programs and automations.
# Author: Noah Lambe
# Dates: August 6, 2024 - August 12, 2024

# Import required libraries, modules, and programs.
from Programs import Program3
from Programs import Program6
from Programs import Program8
from Programs import StandFee

# Start main program loop.
while True:
    # Run StandFee program
    StandFee.main()

    # Display menu options.
    print()
    print("       HAB Taxi Services")
    print("    Company Services System")
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Corporate Summary Report.")
    print("9. Quit Program.")
    print()

    # Get user's menu choice and execute corresponding program.
    choice = int(input("    Enter choice (1 - 9): "))
    print()

    if choice == 1:
        continue
    elif choice == 2:
        continue
    elif choice == 3:
        Program3.main()
    elif choice == 4:
        continue
    elif choice == 5:
        continue
    elif choice == 6:
        Program6.main()
    elif choice == 7:
        continue
    elif choice == 8:
        Program8.main()
    elif choice == 9:
        print()
        Continue = input("Would you like to continue? (Y/N): ").upper()

        if Continue == "N":
            break

# Conclude program.
print()
print("Have a great day!")