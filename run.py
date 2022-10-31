from datetime import datetime 
from dateutil.relativedelta import relativedelta
import time
import gspread
from google.oauth2.service_account import Credentials
import os
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

def get_user():
    """
    Initial prompt to run username input and check that only input is a string between 2 and 15 letters
    """
    print(Fore.MAGENTA + 'Enter your name')
    print(Fore.MAGENTA +'Name must be between 2 and 15 letters long, with no numbers or special characters!')
    print(Fore.MAGENTA + 'Example: Laura \n')

    while(True):
        name = input(Fore.CYAN + 'Enter your name here: \n').lower()
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
    Adds new usernames to login spreadsheet
    """
    print('Adding user details...\n')
    logins.append_row([name])
    print('Your details are recorded \n')

def clear_screen():
    if os.name == 'posix':
        _= os.system('clear')
    else:
        _=os.system('cls')

def edit_records():
    """
    Allows the user to select what they wish to modify. Input is limited to 4 letters
    These 4 letters bring the user to different functions
    If anything else is inputted an error is thrown back to user
    """
    print('This page allows you to navigate our record management area \n')
    print(Fore.BLUE +'Select "a" to see how many applications are on the system')
    print(Fore.GREEN +'Select "d" to navigate to entry date management')
    print(Fore.CYAN +'Select "k" to navigate to highlight issues with applications')
    print(Fore.MAGENTA +'Select "f" to end session')

    records = input('Please select a/d/k/f: \n')
    if records == 'a':
        applications()
    elif records == 'd':
        check_dates()
    elif records == 'k':
        kids_below_6()
    elif records == 'f':
        clear_screen()
        get_user()
    else:
        print (Back.RED + 'INVALID INPUT! Please only enter a/d/k/f')
        edit_records()

def menu():
    """
    Allow user to navigate to menu or to end session. 
    Must only enter m or f
    """
    print(Fore.CYAN +'Press "m" to return to menu')
    print(Fore.MAGENTA +'Select "f" to end session')

    home = input('Please select m/f: \n')
    if home == 'm':
        edit_records()
    elif home == 'f':
        clear_screen()
        get_user()
    else:
        print (Back.RED + 'INVALID INPUT! Please only enter m/f')
        menu()

def applications():
    """
    Function to return the total number of applications on sheet
    Length of column -1 to allow for title of sheet
    """
    date_col= response.col_values(1)
    data_remaining= len(date_col)-1
    print(f'There are {data_remaining} applications on the system \n')
    menu()

def check_dates():
    """
    Use todays date - 6 months to return list of data older than this and their row number in sheet
    This is then used in the delete function
    """
    date_col= response.col_values(1)
    dates_list = [datetime.strptime(date, '%m/%d/%Y %H:%M:%S') for date in date_col[1:]]
    today= datetime.today()
    date_less_6_months = today - relativedelta(months=6)

    old_data=[]
    for date in dates_list:
        if date <= date_less_6_months:
            old_data.append(date)
    to_delete = len(old_data)
    delete(to_delete, old_data, dates_list)

def delete(to_delete, old_data, dates_list):
    """
    User can use this to find which applications are older than 6 months and delete these
    If no applications older than 6 months the user is informed of this and returned to menu
    If older applications present the row number of these is returned and the user is asked if they wish to delete
    If no- they are returned to menu
    If yes a new function is called row_delete
    """
    data_remaining= len(dates_list)

    if to_delete == 0:
        print('You are up to date. All records are under 6 months old')
        menu()
    else:
        date_index = [(dates_list.index(i)+2) for i in old_data if i in dates_list]

        print(f'There are {data_remaining} applications on the system \n')
        print (f'There are {to_delete} files which are over 6 months old and should be deleted.')
        print(f'These are at index {date_index}')
        user_delete= input('Do you wish to delete files:y/n \n')
        if user_delete == 'n':
            menu()
        elif user_delete == 'y':
            row_delete(old_data, dates_list)
        else:
            print (Back.RED + 'INVALID INPUT! Please only enter y/n')
            delete(to_delete, old_data, dates_list)

def row_delete(old_data, dates_list):
    """
    This allows user to delete rows. 
    They must enter just one integer between 2 and 70 otherwise error will occur.
    They cannot delete row 1 as this is the headings of the sheet
    They cannot delete over 65 at the moment as the sheet is not full.
    This can be increased as data increases.
    """
    while True:
        try:
            print('Please enter row you wish to delete. You may not delete row 1. No letters or characters!')
            delete_row = input('Which row do you wish to delete?')
            if delete_row.isdigit():
                delete_row=int(delete_row)
            else:   
                raise ValueError()
            if 2 <= delete_row <= 65:
                print ('Deleting..')
                response.delete_rows(delete_row)
                check_dates()
                data_remaining1= [(dates_list.index(i)+2) for i in old_data if i in dates_list]
                print (f'Data up to date. There are {data_remaining1} applications on the system \n')
                delete(to_delete, old_data, dates_list)
            raise ValueError()
        except ValueError:
            print(Back.RED + '\n Please enter an integer between 2 and 65.')
               
def kids_below_6():
    """
    Function to highlight applications on sheet that have kids under 6 years of age
    It will return the row number of these applications which in further development could be highlighted or moved 
    """
    kids = response.col_values(4)
    yes= 'Yes'
    kid_index =[]
    i=0
    length = len(kids)

    while i< length:
        if yes == kids[i]:
            kid_index.append(i+1)
        i +=1

    if len(kid_index)== 0:
        print('There are no unsuitable applications on the system')
    else:
        print(f'Applicants have said yes to kids under 6 at index {kid_index}')
        print('These applicants are not suitable for adoptions \n')
    menu()

get_user()