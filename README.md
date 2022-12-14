# **Adoption Form Manipulation**

The purpose of this project is to provide a simple, easy way for users to interact with a spreadsheet containing data from a google form. I currently volunteer with an animal rescue using this method for our rehoming but currently all data is manually changed in the spreadsheet. With GDPR records must be deleted after 6 months and certain applicants are unsuitable for homing. The aim of this project was to trial a method of allowing users to perform these tasks with less effort. 

[View the live project here](https://adoption-form.herokuapp.com/) 

## [Contents](#contents) 

* **[Design](#design)**
* **[Project Objectives](#project-objectives)**
* **[User Experience](#user-experience)**
* **[Features](#features)**
   * Initial welcome screen and user-name input
   * New user or already user
   * Menu
   * Applications on system
   * Date management
   * Applicants with young kids
   * End session
* **[Future Features](#future-features)**
* **[Technologies Used](#technologies-used)**
* **[Testing](#testing)**
* **[Bugs](#bugs)**
* **[Validator Testing](#validator-testing)**
* **[Deployment](#deployment)**
* **[Credits](#credits)**

## Design

The google form is designed to collect basic data from potential adopters and collate this into a google sheet. The google form is [available here](https://forms.gle/c2WoRFhvzqWEH8nC6).

The program is designed to manipulate the data from the sheet collected from this form to make rehoming of dogs more streamline. Upon running the program, the user is prompted for a username. This is to ensure security of the program and all new users are recorded.

The colour scheme was chosen to make the text more easy to discern particularly in the menu which is text heavy and to highlight issues with a strong red background to the text. 

[Back to top](#contents)

## Project Objectives

* User can enter valid username which is stored to google sheet
* Return users are recognised
* New users are added to the sheet
* Menu provides options for managing data
* Data from the sheet provides the total number of applications 
* Data from the sheet provides number of applications over 6 month old and their row numbers
* Users may delete rows 
* Data from the sheet provides the number and position of applications on the sheet that do not meet requirements with regards to children under 6
* When user finishes session the data is cleared from the console and login page is presented

[Back to top](#contents)

## User Experience

#### First Time Users
 The goal for first time users is for the program to be easily understood. The user must confirm they have permission to access records and is informed that their name is saved. Any user entry issues are highlighted with a red background to make it clear where errors have been made. 

 #### Existing Users
 Existing users should also be able to quickly and easily navigate the program to manage records and monitor applications. 

 ![Workflow](./images/flowchart.png)

 [Back to top](#contents)

## Features  
#### Initial welcome screen and user-name input
The initial welcome asks for a username to be entered and describes the correct input needed for this. It must be between 2 and 15 letters with only letters used. If a user enters anything not conforming with this an alert is raised and they are asked to enter correct name. Once a name that conforms with the requirements is entered, this is checked against a record of login sheet. The user input is all changed to lower case to ensure that no matter if capitals used or not this will still be recognised. 

If the user is already registered access is granted to the program. If the user is a new user they are asked if they have permission to access records. Again a yes or no is required so any other inputs raise an alert to the user. If the user answers yes their name is recorded to the sheet and they are granted access. If the user answers no they are returned to the welcome page. 

[Back to top](#contents)


####  Menu

The menu page contains 4 options. Again these require specified inputs and anything apart from these will raise an error to the user.

The first item in the menu is to identify how many applications are on the system. This returns the number of applications on the system and returns you to the menu. 

The second allows you to see entries over 6 months old and their index in the spreadsheet. You are then asked if you wish to delete files again with only a y/n answer. Any other input will throw an error. If you select no you are returned to the menu. If yes is selected the index/row you wish to delete should be entered. This must be an integer and cannot be row 1 as this contains the title to the spreadsheet columns. In order to access the correct rows, 2 is added to the index numbers to account for the title page and the fact that sheets start at 1 not 0. Once the row is deleted the program returns the number of applications left and the row numbers of those older than 6 months and asks again if you would like to delete a row. With increased security and recording methods multiple deletes at one time could be possible but due to the scope of this project one delete was only allowed to a user. 

The third option is to access applications with issues such as kids under 6. This gives the user return of the index of unsuitable applications due to young kids in the home. If there are no unsuitable applicants on the system it informs user of this. In future development these applications could be moved to another sheet or highlighted in the existing sheet to make management easier. 

The fourth option clears the program and returns to the user login page. 

[Back to top](#contents)

## Features left to implement

Additional features could be to build out to include a more robust login method with a username and password and record of what occurred with login. With this increased security more tasks could be performed for each user for example all applications over 6 months could be deleted. Applications could be highlighted or moved if they do not meet requirements. 

[Back to top](#contents)

## Technologies Used
* Python
* Gitpod
* GitHub
* Heroku
* Google Sheets
* Google Forms

## Libraries Used

* Colorama
* gspread
* google.oauth2.service_account
* datetime
* dateutil
* time

[Back to top](#contents)

## Testing

I tested my code using [Python Checker](https://www.pythonchecker.com/). No errors were given. 

I performed several manual tests on all aspects of the program where user input is required. 

On the initial screen a username must be input. This must be between 2 and 15 letters with no other characters. To test this I entered a single letter, combined letters over 15 characters, letters and numbers, single numbers, letters and characters, single characters to ensure that errors were given in all instances. Error messages were given in all instances and this appears to be functioning well. 

New users are asked if they have permission to access records. This is a simple y/n. Any other input should throw an error back to the user. This again was tested with a wide variety of letters, numbers and characters and appears to be functioning well. "y" should bring the user to the menu page and "n" should return to login page and all appears to be functioning. 

From the menu page only 4 options are given for input a/d/k/f. Again this was tested with multiple different combinations and all functioning. The respective letters lead to different areas of the program and this was seen on testing. 

Within the entry date management area there again is a y/n input question which was tested as above to ensure functionality. Another input asks then for an integer to delete a row. This must be an integer and this was tested as above with many different inputs to ensure only a single number can be entered. After a deletion occurs the program returns updated information on the number of applications remaining and the number of records over 6 months. This was tested to ensure accuracy by deleting rows with no records, deleting rows with old data and new data to ensure all returned data was accurate. 

Within the kid function tests were performed to ensure accuracy of data when no applicants have responded yes and when multiple applications are unsuitable. 

After each function there is an option to finish session or return to menu and the user must input m for menu or f to end session. This was tested as above to ensure functionality. 

[Back to top](#contents)

## Bugs

There was initially an issue with the login name to check the sheet to see if a new or existing user. The code was only checking the first element of the column so existing users lower in the column were being treated as new users. This was due to repetition in the loop being set up as 'for data in data', once changed to 'for row in data' it functioned correctly. 

There was also initially an issue with adding the new users to the list. This was due to the program expecting a list input. Originally written as 'logins.append_row(name)' once changed to logins.append_row([name]) this was rectified and functioning. 

Another issue was formatting the time from the sheet correctly to compare with today's date and time. This was resolved by removing the time and having it stored as month/day/year [datetime.strptime(date, '%m/%d/%Y %H:%M:%S') for date in date_col[1:]]

On deploying the program to Heroku there was an issue with dateutil. Despite it being installed and on the requirements.txt file, Heroku was returning that the module was not found. With aid from tutor support this was rectified by installing a different version of dateutil. 

Initially the delete function contained the check_date function and the delete_row functions so to reduce errors and ensure accurate returned data after deletion these were split. This resolved issue. 

There is one unresolved bug which is unlikely to affect the program running. If rows date and time match exactly to the second, and if the row is over 6 months old, then the return of that row and matching rows in the row_delete function returns only the first row. For example if row 4 is copied and pasted into row 5 and 6, the return of the data over 6 months old will read [4,4,4] rather than [4,5,6]. This is unlikely to occur in reality as two applicants submitting the form at the exact same time to the second is unlikely. However this could be looked into in further development to resolve. 

[Back to top](#contents)

## Deployment

This project developed on Gitpod and committed and pushed to GitHub and then was deployed using Heroku. An app was created in Heroku using my project name and the region of Europe. Two build packs were added in the Settings tab in the order heroku/python and then heroku/nodejs. A Config Car of PORT set to 8000 is also added. Another Config Var called CREDS contains the cred.json contents. In the Deploy tab the method of deployment was through GitHub and GitHub repository was connected to Heroku. The deployment was set to automatic to update the site with each push to GitHub. The branch to deploy is master/main and the site was deployed. 

[Back to top](#contents)

## Credits

The love sandwiches project was used as a guide for setting the Heroku page up and API's.

Some comments from tutoring were also used to rectify issues with dateutil on Heroku and with user input issues. 

[This](https://stackoverflow.com/questions/51171314/find-indexes-of-common-items-in-two-python-lists) helped with some ideas for finding the old_data in the dates_list to find dates over 6 months old. 

[This](https://stackoverflow.com/questions/52696172/limiting-an-input-between-two-numbers-and-checking-if-the-input-is-a-number-or-n#:~:text=You%20can%20use%20a%20while,%22) helped with restricting integer input to between two numbers for the row_delete function. 

[This](https://appdividend.com/2022/07/14/how-to-clear-screen-in-python/) helped with clearing the screen with finish click.

[Back to top](#contents)

Laura Walsh 2022