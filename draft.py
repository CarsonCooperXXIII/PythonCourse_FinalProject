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
from datetime import datetime

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

# Function to parse date string into datetime object
def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

# Function to view transactions for a specific user
def view_transactions(username):
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = list(csvreader)
        user_transactions = []
        transaction_count = 0
        total_gain = 0
        total_loss = 0

        for transaction in transactions:
            if transaction[8] == username:
                transaction_date = parse_date(transaction[5])
                transaction_amount = float(transaction[5])

                user_transactions.append({
                    "date": transaction_date,
                    "amount": transaction_amount
                })

                transaction_count += 1
                if transaction_amount > 0:
                    total_gain += transaction_amount
                else:
                    total_loss += transaction_amount

        # Include the monthly charge of $10 in the total loss
        total_loss -= 10

        return user_transactions, transaction_count, total_gain, total_loss
# Function to calculate monthly spending
def calculate_monthly_spending(username, month, year):
    transactions, _, _, _ = view_transactions(username)
    total_spending = 0
    
    for transaction in transactions:
        transaction_date = parse_date(transaction['date'])
        if transaction_date.month == month and transaction_date.year == year:
            transaction_amount = transaction['amount']
            if transaction_amount < 0:
                total_spending += abs(transaction_amount)
                return total_spending
            
            
# Function to calculate quarterly income report
def calculate_quarterly_income_report(username):
    transactions, _, total_gain, total_loss = view_transactions(username)
    quarterly_report = {}

    for transaction in transactions:
        transaction_date = transaction['date']
        quarter = f"Q{transaction_date.quarter}-{transaction_date.year}"

        if quarter in quarterly_report:
            quarterly_report[quarter] += transaction['amount']
        else:
            quarterly_report[quarter] = transaction['amount']

    return quarterly_report

# Function to get the account summary for a user
def get_account_summary(username):
    transactions, transaction_count, total_gain, total_loss = view_transactions(username)

    print(f"Account Summary for {username}:")
    print(f"Total transactions: {transaction_count}")
    print(f"Total gain: {total_gain}")
    print(f"Total loss: {total_loss}")

    return transactions
# Function to get the account summary for a user
def get_account_summary(username):
    transactions, transaction_count, total_gain, total_loss = view_transactions(username)

    print(f"Account Summary for {username}:")
    print(f"Total transactions: {transaction_count}")
    print(f"Total gain: {total_gain}")
    print(f"Total loss: {total_loss}")

    return transactions

# Function to get quarter information
def get_quarter(date):
    quarter = (date.month - 1) // 3 + 1
    year = date.year
    return f"Q{quarter}-{year}"

def generate_income_report():
    income_per_quarter = {}

    with open('profiles.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader:
            date = datetime.strptime(row[0], '%Y %m %d')

            amount = float(row[1])
            quarter = get_quarter(date)

            if quarter in income_per_quarter:
                income_per_quarter[quarter] += amount
            else:
                income_per_quarter[quarter] = amount

    return income_per_quarter

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
                        user_input_settings = input(
                            'Pick one from the following settings options and press ENTER: 1) View profile | 2) Change username | 3) Change password | 4) Change PIN | 5) Deactivate account | 6) View Statements- [1/2/3/4/5/6] ? ')

                        if user_input_settings == '1':
                            print('You picked View profile')
                            with open('profiles.csv', 'r') as csvfile:
                                csvreader = csv.reader(csvfile, delimiter='|')
                                for row in csvreader:
                                    if row[8] == username and row[9] == user_password and row[10] == user_pin:
                                        print(row)
                            break
                        
                        elif user_input_settings == '2':
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

                          
                        elif user_input_settings == '3':
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
                        elif user_input_settings == '4':
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
                        elif user_input_settings == '5':
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
                        
                        elif user_input_settings == '6':
                            print('You picked View Statements.\n')
                            print('Please choose one of the following options and press ENTER: 1) View All Transactions | 2) View Gains and Losses | 3) Compare Monthly Spending | 4) Get Quarterly Income Report ')
                            user_input_settings = input()
    
                        if user_input_settings == '1':
                            print('You picked View All Transactions')
                            username = "example_user"
                            account_transactions = get_account_summary(username)
                            for transaction in account_transactions:
                                print(f"Date: {transaction['date']}, Amount: {transaction['amount']}")
            
                        elif user_input_settings == '2':
                            print('You picked View Gains and Losses')
                            username = "example_user"
                            account_transactions = get_account_summary(username)
                            total_gain = sum(transaction['amount'] for transaction in account_transactions if transaction['amount'] > 0)
                            total_loss = sum(transaction['amount'] for transaction in account_transactions if transaction['amount'] < 0)
                            print(f"Total gain: {total_gain}")
                            print(f"Total loss: {total_loss}")
        
                        elif user_input_settings == '3':
                            print('You picked Compare Monthly Spending')
                            username = "example_user"
                            month = int(input("Enter the month (1-12): "))
                            year = int(input("Enter the year: "))
                            monthly_spending = calculate_monthly_spending(username, month, year)
                            print(f"Monthly spending for {month}/{year}: {monthly_spending}")
        
                        elif user_input_settings == '4':
                            print('You picked Get Quarterly Income Report')
                            # Generate the income report
                            income_report = generate_income_report()

    
                            print("Quarterly Income Report:")
                            for quarter, income in income_report.items():
                                print(f"{quarter}: {income}")
                           
                           # this part does not work
                        
                            break
                    else:
                        print("User not authorized.\n")
                        true = 0        

read_profile()

