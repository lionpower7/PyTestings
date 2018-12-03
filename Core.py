# Financial Tool called: 'Z-Ten' for Personal use or Entity use.
# Assests vs Liabilities
# For assets we will be looking at the value of all securities and funds.
# For liabilities we will be looking at personal loans, such as credit card balances, unpaid taxes and mortgages.

subject = input("Welcome, write 'personal' for a personal financial analysis or write 'business' for a business financial analysis: ")

if subject.upper() == 'PERSONAL':
    print("You have chosen to analyze a Person's financial health!")
    name = input("Person's First Name: ")
    sec_amount = int(input(f"How Many Securities Or Financial Vehicles Does {name} Have To Make Profit: "))
    for sec in range(sec_amount):
        sec_ = input(f"{sec} Name: ")
        