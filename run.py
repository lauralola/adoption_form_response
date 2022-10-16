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
            # check spreadheet for user name if there:
            print (f'Welcome back {name}')

            # if not add to sheet and print welcome

        break;


    # data_name = input('Enter your name here: ')
    # validate_data(data_name)
    # print(f'Welcome {data_name}')

# def validate_data(name):
#     """
#     Validates that only letters are entered between 2 and 15 letters long, no numbers or special characters
#     """
#     try:
#         if len(name) <2:
#             raise ValueError(
#                 f'Name must be between 2 and 15 letters! {name} too short!'
#             )
#     except ValueError as e:
#         print(f"Invalid data, {e}, please try again")

#         try:
#             if len(name) >15:           
#                 raise ValueError(
#                     f'Name must be between 2 and 15 letters! {name} is too long!'
#                 )
#         except ValueError as e:
#             print(f"Invalid data, {e}, please try again")


get_user()