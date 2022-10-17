from datetime import datetime 
from dateutil.relativedelta import relativedelta
import time
import gspread
from google.oauth2.service_account import Credentials

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

def get_user():
    """
    Initial prompt to run username input and check that only string between 2 and 15 letters returned
    """
    print('Enter your name \n')
    print('Name must be between 2 and 15 letters long, with no numbers or special characters! \n')
    print('Example: Laura \n')

    while(True):
        name = input('Enter your name here: ')
        if len(name) > 15:
            print("Invalid entry! Your name can only be up to 15 letters \n")
            get_user()
        elif len(name) <2:
            print("Invalid entry! Your name must be more than 2 letters \n")
            get_user()
        elif str.isalpha(name)!= True:
            print("Invalid entry! Your name must only contain letters\n")
            get_user()
        else:
            logon_check(name)
        break;

def logon_check(name):
    """
    Checks user name input against spreadsheet- if already on sheet grants access to edit records. 
    If not asks if user has permission to access these
    If yes- add user to sheet as record 
    If no- brings back to initial page
    """
    data= logins.col_values(1)

    for data in (data):
        if name == data:
            print (f'You have an account. Welcome back {name} \n')
            edit_records()
        elif name != data:
            permission= input('New user! Do you have permission to access records? y/n: \n')
            if permission== 'y':
                add_user(name)
                edit_records()
            elif permission == 'n':
                print ('You do not have access \n')
                get_user()
            else:
                print ('INVALID INPUT!')
                logon_check(name)
        break;

def add_user(name):
    """
    Adds username to login spreadsheet- API error!!!!
    """
    print('Adding user details...\n')
    SHEET.worksheet('logins').append_row(name)
    print('Your details are recorded \n')

def edit_records():
    """
    Allows the user to select what they wish to modify
    """
    print('This page allows you to navigate our record management area \n')
    print('Select "d" to navigate to entry date management')
    print('Select "k" to navigate to highlight issues with applications')
    print('Select "f" to end session')

    records = input('Please select d/k: \n')
    if records == 'd':
        check_dates()
    elif records == 'k':
        kids_below_6()
    elif records == 'f':
        get_user()
    else:
        print ('INVALID INPUT!')
        edit_records()


def check_dates():
    """
    Use todays date - 6 months and delete records before this time
    """
    print(date_col)

    dates_list = [datetime.strptime(date, '%d/%m/%Y %H:%M:%S') for date in date_col[1:]]

    today= datetime.today()
    print(today)

    data_less_6_months = today - relativedelta(months=6)
    print(data_less_6_months)

    for dates in dates_list:
        if dates <= data_less_6_months:
            print(dates)
        else:
            edit_records()
    

def kids_below_6():
    # function to highlight incorrect applications on sheet??
    for kid in (kids):
        if kid == 'Yes':
            response.delete_row(index)
            return kid
        else:
            edit_records()

get_user()