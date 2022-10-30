from datetime import datetime 
from dateutil.relativedelta import relativedelta
import time
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adoption_form_responses')

logins = SHEET.worksheet('logins')
response= SHEET.worksheet('response')
date_col= response.col_values(1)
kids = response.col_values(4)
dates_list = [datetime.strptime(date, '%m/%d/%Y %H:%M:%S') for date in date_col[1:]]

def get_user():
    """
    Initial prompt to run username input and check that only string between 2 and 15 letters returned
    """
    print(Fore.MAGENTA + 'Enter your name')
    print(Fore.MAGENTA +'Name must be between 2 and 15 letters long, with no numbers or special characters!')
    print(Fore.MAGENTA + 'Example: Laura \n')

    while(True):
        name = input(Fore.CYAN + 'Enter your name here: \n')
        if len(name) > 15:
            print(Back.RED + "Invalid entry! Your name can only be up to 15 letters \n")
            get_user()
        elif len(name) <2:
            print(Back.RED + "Invalid entry! Your name must be more than 2 letters \n")
            get_user()
        elif str.isalpha(name)!= True:
            print(Back.RED + "Invalid entry! Your name must only contain letters\n")
            get_user()
        else:
            logon_check(name)
        break

def logon_check(name):
    """
    Checks user name input against spreadsheet- if already on sheet grants access to edit records. 
    If not asks if user has permission to access these
    If yes- add user to sheet as record 
    If no- brings back to initial page
    """
    # not working correctly! Only checking first value
    data = logins.col_values(1)

    for row in (data):
        if name in data:
            print (Fore.GREEN + f'You have an account. Welcome back {name} \n')
            edit_records()
        elif name not in data:
            permission= input(Fore.YELLOW + 'New user! Do you have permission to access records? y/n: \n')
            if permission== 'y':
                add_user(name)
                edit_records()
            elif permission == 'n':
                print (Back.RED + 'You do not have access \n')
                get_user()
            else:
                print (Back.RED + 'INVALID INPUT!')
                logon_check(name)
        break

def add_user(name):
    """
    Adds username to login spreadsheet
    """
    print('Adding user details...\n')
    logins.append_row([name])
    print('Your details are recorded \n')

def edit_records():
    """
    Allows the user to select what they wish to modify
    """
    print('This page allows you to navigate our record management area \n')
    print(Fore.BLUE +'Select "a" to see how many applications are on the system')
    print(Fore.GREEN +'Select "d" to navigate to entry date management')
    print(Fore.CYAN +'Select "k" to navigate to highlight issues with applications')
    print(Fore.MAGENTA +'Select "f" to end session')

    records = input('Please select a/d/k/f: \n')
    data_remaining= len(dates_list)

    if records == 'a':
        print(f'There are {data_remaining} applications on the system \n')
        edit_records()
    elif records == 'd':
        check_dates()
    elif records == 'k':
        kids_below_6()
    elif records == 'f':
        quit()
    else:
        print (Back.RED + 'INVALID INPUT!')
        edit_records()


def check_dates():
    """
    Use todays date - 6 months and delete records before this time
    """
    today= datetime.today()
    date_less_6_months = today - relativedelta(months=6)

    old_data=[]
    for date in dates_list:
        if date <= date_less_6_months:
            old_data.append(date)
    to_delete = len(old_data)
    delete(to_delete, old_data)

def delete(to_delete, old_data):
    """
    User can use this to find which applications are older than 6 months and delete these
    """

    if to_delete == 0:
        print('You are up to date. All records are under 6 months old')
        edit_records()
    else:
        date_index = [(dates_list.index(i)+2) for i in old_data if i in dates_list]

        print (f'There are {to_delete} files which are over 6 months old and should be deleted.')
        print(f'These are at index {date_index}')
        user_delete= input('Do you wish to delete files:y/n \n')
        if user_delete == 'n':
            edit_records()
        elif user_delete == 'y':
            while True:
                try:
                    print('Please enter row you wish to delete. You may not delete row 1. No letters or characters!')
                    delete_row = input('Which row do you wish to delete?')
                    if delete_row.isdigit():
                        delete_row=int(delete_row)
                    else:   
                        raise ValueError()
                    if 2 <= delete_row <= 400:
                        print ('Deleting..')
                        response.delete_rows(delete_row)
                        data_remaining1= (len(dates_list)-1)
                        print (f'Data up to date. There are {data_remaining1} applications on the system \n')
                        exit()
                    raise ValueError()
                except ValueError:
                    print('\n Please enter an integer between 2 and 400.')
        else:
            print ('INVALID INPUT!')
            delete(to_delete, old_data)
#                 
def kids_below_6():
    """
    function to highlight incorrect applications on sheet
    """

    yes= 'Yes'
    kid_index =[]
    i=0
    length = len(kids)

    while i< length:
        if yes == kids[i]:
            kid_index.append(i+1)
        i +=1
    
    print(f'Applicants have said yes to kids under 6 at index {kid_index}')
    print('These applicants are not suitable for adoptions \n')

    edit_records()

get_user()