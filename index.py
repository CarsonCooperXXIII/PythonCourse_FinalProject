print("==================================================")
print("              ***** Final Project ****")
print("==================================================\n")

print("--------------------------------------------------")
print("      Book Keeping System - GEO Investments")
print("--------------------------------------------------\n")

print("1) New users? Sign Up -> Create an account")
print("2) Current users? Log In -> Open your account")

print("--------------------------------------------------\n")


import os.path
import csv
import string
import random


user_option = str(input("Enter a number option and press ENTER: "))
print("\n")


#------------------------ Account Creation: Create a Profile------------------------------------------#
class Profile:
    def __init__(self, full_name, address, date_of_birth, business_name, date_of_incorporation, stakeholders,
                 account_type):
        self.full_name = full_name
        self.address = address
        self.date_of_birth = date_of_birth
        self.business_name = business_name
        self.date_of_incorporation = date_of_incorporation
        self.stakeholders = stakeholders
        self.account_type = account_type
        self.account_number = self.generate_account_number()  # Create an account number
        self.username = self.generate_username()  # Generate a username
        self.password = self.generate_password()  # Generate a password
        self.pin = self.generate_pin()  # Generate a pin

    # Create an account number
    def generate_account_number(self):
        random_digits = ''.join(random.choices(string.digits, k=8))
        business_name_initials = self.business_name[:2].upper()
        account_number = f"{random_digits}-{business_name_initials}"
        return account_number

    # Generate a Username
    def generate_username(self):
        first_initial = self.full_name[0].lower()
        last_name = self.full_name.split()[-1].lower()
        username = f"{first_initial}{last_name}"
        return username

    # Generate a Password
    def generate_password(self):
        password_length = random.randint(8, 12)
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters)
                           for _ in range(password_length))
        return password

    # Generate a PIN Number
    def generate_pin(self):
        pin = ''.join(random.choices(string.digits, k=4))
        return pin

    def display_profile(self):
        print("Full Name:", self.full_name)
        print("Address:", self.address)
        print("Date of Birth:", self.date_of_birth)
        print("Business Name:", self.business_name)
        print("Date of Incorporation:", self.date_of_incorporation)
        print("Stakeholders & Equity:", self.stakeholders)
        print("Account Type:", self.account_type)
        print("Account Number:", self.account_number)
        print("Username:", self.username)
        print("Password:", self.password)
        print("PIN:", self.pin)


# Save Profile
def save_profile(profile):
    with open('profiles.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_ALL)
        writer.writerow([profile.full_name, profile.address, profile.date_of_birth, profile.business_name,
                         profile.date_of_incorporation, profile.stakeholders, profile.account_type,
                         profile.account_number, profile.username, profile.password, profile.pin])


# Function to view transactions for a specific user
def view_transactions(username, month=None, year=None):
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = list(csvreader)
        transaction_count = 0
        total_gain = 0
        total_loss = 0

        for transaction in transactions:
            if transaction[8] == username:
                transaction_date = transaction[1]
                transaction_amount = float(transaction[2])
                transaction_month, transaction_year = map(int, transaction_date.split('-'))

                # Check if the transaction falls within the specified month and year
                if month is not None and year is not None:
                    if transaction_month != int(month) or transaction_year != int(year):
                        continue

                # Check if the transaction amount is in the expected format
                if not transaction_amount.isdigit():
                    print(f"Invalid transaction amount: {transaction_amount}")
                    continue

                transaction_amount = float(transaction_amount)

                transaction_count += 1
                if transaction_amount > 0:
                    total_gain += transaction_amount
                else:
                    total_loss += transaction_amount

                print(f"Date: {transaction_date} | Amount: {transaction_amount}")

        # Include the monthly charge of $10 in the total loss
        total_loss -= 10

        print(f"Total transactions: {transaction_count}")
        print(f"Total gain: {total_gain}")
        print(f"Total loss: {total_loss}")

# Function to compare monthly spending
def compare_monthly_spending(username):
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = list(csvreader)
        monthly_spending = {}

        for transaction in transactions:
            if transaction[0] == username:
                transaction_date = transaction[1]
                transaction_amount = float(transaction[2])
                transaction_month, transaction_year = map(int, transaction_date.split('-'))

                if transaction_month in monthly_spending:
                    monthly_spending[transaction_month] += transaction_amount
                else:
                    monthly_spending[transaction_month] = transaction_amount

        print("Monthly Spending Comparison:")
        for month, spending in monthly_spending.items():
            print(f"Month: {month} | Spending: {spending}")

# Function to get quarterly income report
def get_quarterly_income_report(username):
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = list(csvreader)
        quarterly_income = {}

        for transaction in transactions:
            if transaction[0] == username:
                transaction_date = transaction[1]
                transaction_amount = float(transaction[2])
                transaction_month, transaction_year = map(int, transaction_date.split('-'))
                quarter = (transaction_month - 1) // 3 + 1

                if quarter in quarterly_income:
                    quarterly_income[quarter] += transaction_amount
                else:
                    quarterly_income[quarter] = transaction_amount

        print("Quarterly Income Report:")
        for quarter, income in quarterly_income.items():
            print(f"Quarter: {quarter} | Income: {income}")
            
# Function to compare monthly spending
def compare_monthly_spending(username):
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = list(csvreader)
        monthly_spending = {}

        for transaction in transactions:
            if transaction[8] == username:
                transaction_date = transaction[1]
                transaction_amount = float(transaction[2])
                transaction_month, transaction_year = map(int, transaction_date.split('-'))

                if transaction_month in monthly_spending:
                    monthly_spending[transaction_month] += transaction_amount
                else:
                    monthly_spending[transaction_month] = transaction_amount

        print("Monthly Spending Comparison:")
        for month, spending in monthly_spending.items():
            print(f"Month: {month} | Spending: {spending}")

# Function to read user profile and perform actions
def read_profile():
    username = input("Enter your username: ")

    view_transactions(username)
    compare_monthly_spending(username)
    get_quarterly_income_report(username)

# Account creation - create a profile, account number, username, password, PIN number and store profile
if user_option == '1':
    def create_profile():
        full_name = input("Enter full name: ")
        address = input("Enter address: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        business_name = input("Enter business name: ")
        date_of_incorporation = input(
            "Enter date of incorporation (YYYY-MM-DD): ")
        stakeholders = input("Enter stakeholders & equity (comma-separated): ")
        account_type = input(
            "Enter account type (Small/Medium/Large/Enterprise): ")

        profile = Profile(full_name, address, date_of_birth, business_name,
                          date_of_incorporation, stakeholders, account_type)
        return profile

    profile = create_profile()
    profile.display_profile()
    save_profile(profile)
    print("File created.")

#-------------------------------------Current Users -  Login -----------------------------------------------------#
elif user_option == '2':

    def read_profile():
        # input username
        username = input('Enter your username and press ENTER: ')
        # input password
        user_password = input('Enter your password and press ENTER: ')
        # input PIN
        user_pin = input('Enter your PIN and press ENTER: ')
        
        
        with open('profiles.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter='|')
            for row in csvreader:
             
                if row[8] == username and row[9] == user_password and row[10] == user_pin:
                    print("User is Authorized\n")
                    true = 1
    
                    # Settings
                    while true:
                        user_input = input(
                            'Pick one from the following settings options and press ENTER: 1) View profile | 2) Change username | 3) Change password | 4) Change PIN | 5) Deactivate account | 6) View Statements- [1/2/3/4/5/6] ? ')

                        if user_input == '1':
                            print('You picked View profile')
                            with open('profiles.csv', 'r') as csvfile:
                                csvreader = csv.reader(csvfile, delimiter='|')
                                for row in csvreader:
                                    if row[8] == username and row[9] == user_password and row[10] == user_pin:
                                        print(row)
                            break
                        
                        elif user_input == '2':
                            print('You picked Change username')
                            new_username = input("Enter new username: ")

                            # reading the CSV file
                            text = open("profiles.csv", "r")

                            # join() method combines all contents of csvfile.csv and formed as a string
                            text = ''.join([i for i in text])

                            # search and replace the contents
                            text = text.replace(username, new_username)

                            # profiles.csv opened in write mode
                            x = open("profiles.csv", "w")

                            # all the replaced text is written in the profiles.csv file
                            x.writelines(text)
                            x.close()

                            print("New username is added to your profile\n ")

                          
                        elif user_input == '3':
                            print('You picked Change password')
                            new_password = input("Enter new password: ")

                            # reading the CSV file
                            text = open("profiles.csv", "r")

                            # join() method combines all contents of csvfile.csv and formed as a string
                            text = ''.join([i for i in text])

                            # search and replace the contents
                            text = text.replace(user_password, new_password)

                            # profiles.csv opened in write mode
                            x = open("profiles.csv", "w")

                            # all the replaced text is written in the profiles.csv file
                            x.writelines(text)
                            x.close()

                            print("New password is added to your profile\n ")

                            break
                        elif user_input == '4':
                            print('You picked Change PIN')
                            new_pin = input("Enter new PIN: ")

                            # reading the CSV file
                            text = open("profiles.csv", "r")

                            # join() method combines all contents of csvfile.csv and formed as a string
                            text = ''.join([i for i in text])

                            # search and replace the contents
                            text = text.replace(user_pin, new_pin)

                            # profiles.csv opened in write mode
                            x = open("profiles.csv", "w")

                            # all the replaced text is written in the profiles.csv file
                            x.writelines(text)
                            x.close()

                            print("New PIN is added to your profile\n ")

                            break
                        elif user_input == '5':
                            print('You picked Deactivate account')

                            # reading the CSV file
                            with open('profiles.csv', 'r') as csvfile:
                                csvreader = csv.reader(csvfile, delimiter='|')
                                profiles = list(csvreader)
                                profile_exists = False

                                for profile in profiles:
                                    if profile[8] == username:
                                        profile_exists = True
                                        profiles.remove(profile)
                                        break

                            if profile_exists:
                                with open('profiles.csv', 'w', newline='') as csvfile:
                                    csvwriter = csv.writer(
                                        csvfile, delimiter='|', quoting=csv.QUOTE_ALL)
                                    for profile in profiles:
                                        csvwriter.writerow(profile)

                                user_file = f"users/{username}.txt"
                                if os.path.exists(user_file):
                                    os.remove(user_file)

                                print(
                                    f"Account for {username} has been deactivated and information deleted.")
                            else:
                                print(
                                    f"Account for {username} does not exist.")
                                break
                            break
                        
                        elif user_input == '6':
                            print('You picked View Statements.\n')
                            print('')
                            print('Please choose one of the following options and press ENTER: 1) View All Statements | 2) View Monthly Statements | 3) View Insights | 4) Get Quarterly Income Report ')
                            
                            user_input = input()
                            if user_input == '1':
                                print('You picked View All Statements.')
                                view_transactions(username)
                            
                            elif user_input =='2':
                                print('You picked View Monthly Statements.')
                                print('Please enter the month and year for which you want to view transactions (YYYY-MM):')
                                month_year = input()
                                month, year = month_year.split('-')
                                view_transactions(username, month, year)
                            
                            elif user_input == '3':
                                print('You picked View Insights')
                                print('')
                                print('Please choose one of the following options and press ENTER: 1) Compare Monthly Spending | 2) Get Quarterly Income Report')
                                insights_option = input()
                                print(insights_option)
                            
                            elif user_input == '4':
                                print('You picked Get Quarterly Income Report')

                            break
                    else:
                        print("User not authorized.\n")
                        true = 0        
                        
    read_profile()

