from datetime import datetime
import string
import random
import csv
print("==================================================")
print("              ***** Final Project ****")
print("==================================================\n")

print("--------------------------------------------------")
print("      Book Keeping System - GEO Investments")
print("--------------------------------------------------\n")

print("1) New users? Sign Up -> Create an account")
print("2) Current users? Log In -> Open your account")

print("--------------------------------------------------\n")


user_option = str(input("Enter a number option and press ENTER: "))
print("\n")

# ------------------------ Account Creation: Create a Profile------------------------------------------#

if user_option == '1':

    # Function to generate an account number
    def generate_account_number(business_name):
        account_number = ''.join(random.choices(string.digits, k=8))
        account_number += '-' + business_name[:2].upper()
        return account_number

    # Function to create a new profile
    def create_profile():
        full_name = input('Enter your full name: ')
        address = input('Enter your address: ')
        date_of_birth = input('Enter your date of birth: ')
        business_name = input('Enter the name of your business: ')
        date_of_incorporation = input('Enter the date of incorporation: ')
        stakeholders_equity = input(
            'Enter the list of stakeholders and equity: ')

        print('Choose the type of account:')
        print('1) Small Business Class')
        print('2) Medium Business Class')
        print('3) Large Business Class')
        print('4) Enterprise Business')
        account_type = input('Enter the account type (1/2/3/4): ')

        account_number = generate_account_number(business_name)

        username = input('Enter a username: ')
        password = input('Enter a password: ')
        pin = input('Enter a 4-digit PIN number: ')

        profile = {
            'Full Name': full_name,
            'Address': address,
            'Date of Birth': date_of_birth,
            'Business Name': business_name,
            'Date of Incorporation': date_of_incorporation,
            'Stakeholders & Equity': stakeholders_equity,
            'Account Type': account_type,
            'Account Number': account_number,
            'Username': username,
            'Password': password,
            'PIN': pin
        }

        with open('profiles.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerow(profile.values())

        print('Profile created successfully.')

    create_profile()

# #-------------------------------------Current Users -  Login -----------------------------------------------------#
elif user_option == '2':

    def read_profile():
        # input username
        username = input('Enter your username and press ENTER: ')
        # input password
        user_password = input('Enter your password and press ENTER: ')
        # input PIN
        user_pin = input('Enter your PIN and press ENTER: ')
        login_user(username, user_password, user_pin)

        #  Settings------------Statements-------------------#
        while True:
            user_input_settings = input(
                'Pick one from the following settings options and press ENTER: 1) View profile | 2) Change username | 3) Change password | 4) Change PIN | 5) Deactivate account | 6) View Statements - [1/2/3/4/5/6] ? '
            )

            if user_input_settings == '1':
                print('You picked View profile')
                profile = view_profile(username)
                print('Current Profile:')
                for key, value in profile.items():
                    print(f'{key}: {value}')

                break

            elif user_input_settings == '2':
                print('You picked Change username')
                new_username = input("Enter new username: ")
                change_username(username, new_username)

                break

            elif user_input_settings == '3':
                print('You picked Change password')
                new_password = input("Enter new password: ")
                change_password(username, new_password)

                break

            elif user_input_settings == '4':
                print('You picked Change PIN')
                new_pin = input("Enter new PIN: ")
                change_pin(username, new_pin)

                break

            elif user_input_settings == '5':
                print('You picked Deactivate account')
                deactivate_account(username)

                break

            if user_input_settings == '6':
                print('You picked View Statements.\n')
                print('Please choose one of the following options and press ENTER: 1) View All Statements | 2) View Monthly statements | 3) View Insights ')
                user_input_statements = input()

                if user_input_statements == '1':
                    print('You picked View All Statements')
                    view_statements(username)

                elif user_input_settings == '2':
                    print('View Monthly statements')
                    user_input_month = input(
                        'Please input the month you want to see the statements and press ENTER: ')
                    user_input_year = input(
                        'Please input the year and press ENTER: ')
                    view_monthly_statements(
                        username, user_input_month, user_input_year)

                elif user_input_settings == '3':
                    print(' View Insights')
                    user_input_insights = input(
                        'Pick one from the following settings options and press ENTER: 1) Compare Monthly Spending | 2) Quarterly Income Report '
                    )

                    if user_input_insights == '1':
                        print('Compare Monthly Spending')
                        user_input_compare_month1 = input(
                            'Please input the month you want to compare with and press ENTER: '
                        )
                    user_input_compare_month2 = input(
                        'Please input the month to which you want to compare with and press ENTER: '
                    )
                    user_input_compare_year = input(
                        'Please input the year in which the months fall and press ENTER: '
                    )
                    compare_monthly_spending(username, user_input_compare_month1,
                                             user_input_compare_year,
                                             user_input_compare_month2,
                                             user_input_compare_year)

                    user_answer_monthly_fees = input(
                        'Do you want to see your monthly fees, type YES or NO and press ENTER: '
                    )
                    if user_answer_monthly_fees == 'YES':
                        charge_monthly_fee(username)
                    else:
                        print('You choose NO')

                elif user_input_settings == '2':
                    print('Quarterly Income Report')
                    generate_quarterly_income_report(username)
            break

    # Usage examples
    # login_successful = login_user('john_doe', 'password123', '1234')
    # if login_successful:
    #     profile = view_profile('john_doe')
    #     print('Current Profile:')
    #     for key, value in profile.items():
    #         print(f'{key}: {value}')

    #     change_username('john_doe', 'jdoe')
    #     change_password('jdoe', 'newpassword')
    #     change_pin('jdoe', '4321')

    #     deactivate_account('jdoe')
    # else:
    #     print('Invalid login credentials.')


def login_user(username, password, pin):

    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            if row[8] == username and row[9] == password and row[10] == pin:
                print("User is Authorized\n")
                return True

            else:
                print("User not authorized.\n")

                return False


def view_profile(username):
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            if row[8] == username:
                profile = {
                    'Full Name': row[0],
                    'Address': row[1],
                    'Date of Birth': row[2],
                    'Business Name': row[3],
                    'Date of Incorporation': row[4],
                    'Stakeholders & Equity': row[5],
                    'Account Type': row[6],
                    'Account Number': row[7],
                    'Username': row[8],
                    'Password': row[9],
                    'PIN': row[10]
                }
                return profile


def change_username(username, new_username):
    profiles = []
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            if row[8] == username:
                row[8] = new_username
            profiles.append(row)

    with open('profiles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(profiles)
        print("New username is added to your profile\n ")


def change_password(username, new_password):
    profiles = []
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            if row[8] == username:
                row[9] = new_password
            profiles.append(row)

    with open('profiles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(profiles)
        print("New password is added to your profile\n ")


def change_pin(username, new_pin):
    profiles = []
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            if row[8] == username:
                row[10] = new_pin
            profiles.append(row)

    with open('profiles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(profiles)
        print("New PIN is added to your profile\n ")


def deactivate_account(username):
    profiles = []
    with open('profiles.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            if row[8] == username:
                continue
            profiles.append(row)

    with open('profiles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(profiles)

    # Delete all transactions associated with the deactivated account
    with open('transactions.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = []
        for row in csvreader:
            if row[0] != username:
                transactions.append(row)

    with open('transactions.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(transactions)

    print('Account deactivated and all associated information deleted.')

# ---------------------------------------------Statements functions ----------------------------------#


def get_account_transactions(username):
    with open('transactions.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = []
        for row in csvreader:
            if row[0] == username:
                transaction = {
                    'Date': row[1],
                    'Amount': float(row[2]),
                    'Description': row[3]
                }
                transactions.append(transaction)
        return transactions


def calculate_total_transactions_and_gain_loss(username):
    transactions = get_account_transactions(username)
    total_transactions = len(transactions)
    total_gain = sum(transaction['Amount'] for transaction in transactions
                     if transaction['Amount'] > 0)
    total_loss = sum(transaction['Amount'] for transaction in transactions
                     if transaction['Amount'] < 0)
    return total_transactions, total_gain, total_loss


def get_monthly_transactions(username, month, year):
    with open('transactions.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        transactions = []
        for row in csvreader:
            if row[0] == username:
                transaction_date = datetime.strptime(row[1], '%Y-%m-%d')
                if transaction_date.month == month and transaction_date.year == year:
                    transaction = {
                        'Date': row[1],
                        'Amount': float(row[2]),
                        'Description': row[3]
                    }
                    transactions.append(transaction)
        return transactions


def calculate_monthly_gain_loss(username, month, year):
    transactions = get_monthly_transactions(username, month, year)
    total_transactions = len(transactions)
    total_gain = sum(transaction['Amount'] for transaction in transactions
                     if transaction['Amount'] > 0)
    total_loss = sum(transaction['Amount'] for transaction in transactions
                     if transaction['Amount'] < 0)
    return total_transactions, total_gain, total_loss


def compare_monthly_spending(username, month1, year1, month2, year2):
    transactions1 = get_monthly_transactions(username, month1, year1)
    transactions2 = get_monthly_transactions(username, month2, year2)
    total_spending1 = sum(transaction['Amount'] for transaction in transactions1
                          if transaction['Amount'] < 0)
    total_spending2 = sum(transaction['Amount'] for transaction in transactions2
                          if transaction['Amount'] < 0)
    return total_spending1, total_spending2


def generate_quarterly_income_report(username):
    current_year = datetime.now().year
    quarters = [(1, current_year), (2, current_year), (3, current_year),
                (4, current_year - 1)]
    quarterly_reports = []
    for quarter in quarters:
        transactions = get_monthly_transactions(username, (quarter[0] - 1) * 3 + 1,
                                                quarter[1])
        total_gain = sum(transaction['Amount'] for transaction in transactions
                         if transaction['Amount'] > 0)
        total_loss = sum(transaction['Amount'] for transaction in transactions
                         if transaction['Amount'] < 0)
        quarterly_report = {
            'Quarter': quarter,
            'Gain': total_gain,
            'Loss': total_loss
        }
        quarterly_reports.append(quarterly_report)
    return quarterly_reports


def charge_monthly_fee(username):
    with open('transactions.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        transaction = [
            username,
            datetime.now().strftime('%Y-%m-%d'), -10, 'Monthly fee'
        ]
        writer.writerow(transaction)


def view_statements(username):
    transactions = get_account_transactions(username)
    total_transactions, total_gain, total_loss = calculate_total_transactions_and_gain_loss(
        username)
    print('All transactions:')
    for transaction in transactions:
        print(
            f"Date: {transaction['Date']}, Amount: {transaction['Amount']}, Description: {transaction['Description']}"
        )
    print(f'Total number of transactions: {total_transactions}')
    print(f'Total gain: {total_gain}')
    print(f'Total loss: {total_loss}')


def view_monthly_statements(username, month, year):
    transactions = get_monthly_transactions(username, month, year)
    total_transactions, total_gain, total_loss = calculate_monthly_gain_loss(
        username, month, year)
    print(f'Monthly statements for {month}/{year}:')
    for transaction in transactions:
        print(
            f"Date: {transaction['Date']}, Amount: {transaction['Amount']}, Description: {transaction['Description']}"
        )
    print(f'Total number of transactions: {total_transactions}')
    print(f'Total gain: {total_gain}')
    print(f'Total loss: {total_loss}')


read_profile()
