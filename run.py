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

data= logins.get_all_values()
print(data)

def get_user():
    """
    Gets user name and checks against login sheet
    """
    print('Enter your name')
    print('Name must be between 2 and 15 letters long, with no numbers or special characters!')
    print('Example: Laura \n')

    data_name = input('Enter your name here: ')
    print(f'Welcome {data_name}')

get_user()