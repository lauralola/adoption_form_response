from datetime import date 
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

def get_user():
    """
    Initial prompt to run username input and check that only string between 2 and 15 letters returned
    """
    print('Enter your name')
    print('Name must be between 2 and 15 letters long, with no numbers or special characters!')
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
            print (f'You have an account. Welcome back {name}')
            # run function to change records
        elif name != data:
            permission= input('New user! Do you have permission to access records? y/n: \n')
            if permission== 'y':
            # run function to change records
                logon_check(name)
            elif permission == 'n':
                print ('You do not have access \n')
                get_user()
            else:
                print ('INVALID INPUT!')
                logon_check(name)
        break;

# function to change records by date- import date info- delete 6 months
# function to highlight incorrect applications on sheet??

get_user()