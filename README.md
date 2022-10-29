# **Adotion Form Manipulation**

The purpose of this project is to provide a simple, easy way for users to interact with a spreadsheet containing data from a google form. I currently volunteer with an animal rescue using this method for our rehoming but currently all data is manually changed in the spreadsheet. With GDPR records must be deleted after 6 months and certain applicants are unsuitable for homing. The aim of this project was to trial a method of allowing users to perform these tasks with less effort. 

[View the live project here]() 

## Contents                             1       2

* **[Design](#design)**
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

The google form is designed to collect basic data from potential adopters and colate this into a google sheet. The program is designed to manipulate the data in this sheet to make rehoming of dogs more steamline. 

Upon running the program, the user is prompted for a username. This is to ensure security of the program as contact

Tha background and colour scheme was chosen to give the feeling and ambiance of a card table in a casino with black, red and silver being the primary chosen colours and an image of a man dealing cards. The font again was chosen to invoke that feeling of the Wild West and old time card saloons and is large enough in size to be legible to users.  A fall-back font of Sans-Serif should the browser be unable to access the google fonts was used. One font was used to ensure consistency. 

Icons from font awesome were also utilised to add some extra focus for clients. 

Upon opening the game an alert appears to explain the basic instructions for the game and how to play. This is short and concise so as to keep users engaged.

![Website](./assets/images/readme-images/responsive.png)

[Back to top](#contents)

## User Experience

#### First Time Users
 The goal for first time users is for the game to be easily understood. The user should from opening of the site be able to read the short instructions and be able to play the game. The design is simple in structure so as not to have too many elements to confuse a first time user.  

 #### Existing Users
 Existing users should also be able to quickly and easily navigate the game to keep them engaged and interested in the product. 

## Features  
  * Initial welcome screen and user-name input
   * New user or already user
   * Menu
   * Applications on system
   * Date management
   * Applicants with young kids
   * End session
#### Initial Game Alert 
The inital alert is deigned to easily explain how the game is played. It is designed to upon loading of the page pop up to assist the user and can then be closed to procede with the game. The aim of the game is to beat the computer. The sum total of the players cards should stay below 21 but as close to 21 as possible. 

![Initial Game Alert](./assets/images/readme-images/alert.png)

#### Computer area
  
The computer area displays a '?' for most of the game as the player is unable to see what numbers the computer is being dealt. Once the computer and the player both select to hold, the total sum of the computer cards is displayed. Once the reset button is selected, this area returns to displaying a '?'. On smaller screen sizes the display and font reduce in size, however the overall look appears the same as on larger devices. 

![Computer Area](./assets/images/readme-images/card-area.png)

#### Play area

The play area contains three buttons with different functions. Firstly the reset button resets the game so player and computer are both back to '0'.

The hit button, when selected, will deal a card to the player and the computer (if the computer score is below 17). Once the computer score reaches 17 or above the computer will hold and will not be dealt more cards if the player continues to press hit. This is alerted to the user.

The hold button, when selected by the player means no card is dealt to the player but the computer recieves cards if below 17. Once the computer score reaches 17 it will also display an alert that the computer holds and the game ends. The winner is then revealed. 

On larger screen sizes the buttons are displayed side by side horizontally but for smaller screen sizes they are stacked vertically for ease of use. 

![Play area](./assets/images/readme-images/play-area.png)

#### Player area

The player area again is kept simple in design. It initially displays '0' and each time the player selects hit and a card is dealt the total score for the player is displayed for them. This should help them decide if they want another card to add to this or to hold their score. Once the reset button is selected, this area returns to displaying a '0'. On smaller screen sizes the display and font reduce in size, however the overall look appears the same as on larger devices. 

![Player Area](./assets/images/readme-images/phone.png)

#### Score Area 

The score area records the winners and losers of the games overall. Every time the computer wins a game the computer score increases by one and the same for player score. 

![Score Area](./assets/images/readme-images/score-area.png)

## Features left to implement

Additional features could be to build out the game to include a suit of cards. Currently the player recieves a random number between 1 and 12. This could be expanded to include a deck of cards.

The current layout with three potential card areas for both the player and computer could be modified so that individual cards are dealt and held in each separate div. 

[Back to top](#contents)

## Technologies Used
* HTML5 
* CSS
* JavaScript
* Gitpod
* GitHub
* Google Fonts
* Font Awesome
* Google Chrome DevTools

## Testing

This page was tested in different browsers including Safari and Chrome with the full site and links tested across the different platforms. It was tested across several devices including a laptop, iPad and iPhone. 

All buttons were tested to ensure functionality. The game was run several times to ensure accuracy of functions. Responsiveness was tested and edited using DevTools and then media queries. Responsive design was checked with the 'Am I Responsive' site. 

![Am I Responsive Result](./assets/images/readme-images/responsive.png)

The colour scheme used was identified to be easy to read with contrasting colours and this was tested along with general accessibilty results using the Lighthouse feature on Google Dev Tools. 

![Accessibility](./assets/images/readme-images/lighthouse.png)

[Back to top](#contents)

## Validator Testing
HTML
No errors were returned when passing through the official W3C validator

![HTML testing](./assets/images/readme-images/html.png)

CSS
No errors were found when passing through the official (Jigsaw) validator

![CSS testing](./assets/images/readme-images/css.png)

JavaScript
No errors were found when passing through the official Jshint validator

![JavaScript testing](./assets/images/readme-images/jshint.png)

[Back to top](#contents)

## Bugs
Through the course of the project several issues were identified and recitified. 

* One font awesome icon was not displaying initially, however it was an issue with it not being a free icon and a different icon chosen. 

* Lighthouse performance was reduced due to no CSS height or width on logo image. CSS rule applied to logo class was changed to img instead. 

* There were several issues initially with functions being over-complicated and returning duplicate numbers for players. With testing using console.logs on dev tools, it was identified what functions were causing the issues and these were modified and retested to ensure they were working correctly. The playerHold, computerHold and gamePlay functions were in certain circumstances causing two numbers to be returned due to them being called in close succession. 

* There was an initial issue with displaying the player and computer score on the appropriate areas. After some research and discussion with tutoring it was discovered that the set inner text for these was returning the global variables not the returned value for player1 and player2. This was rectified. 

[Back to top](#contents)

## Deployment

The site was deployed using GitHub pages. This was performed by navigating to the settings page within the repository. The pages tab on the menu to the left of the screen was opened and the source drop-down menu was changed to main. This generated a link to the site after a few minutes. 

[Back to top](#contents)

## Credits

The love maths project was used as a guide for setting the DOM content loaded function and the functions for keeping computer and player game score.

Some comments from tutoring were also used to rectify issues with the display of the player and user score during the game play. 

[Back to top](#contents)

## Content
Images were accessed from Pexels (https://www.pexels.com). 

Icons for the play area were accessed at Font Awesome.

Fonts were accessed from Google Fonts. 

Favicon was generated using favicon.io

Laura Walsh 2022


issue with login check name-only checking first one- adding duplicates to file-?why
adding name to spreadsheet- was expecting list[]
formatting the time correctly for comparison
separateing delete function from check date function as was repeating with each iteration
Adding 1 to index as not 0 indexed
Not recognising interger for input??
adding row in data rather than data in data resolved name spreadsheet issue. 

Date issues tried:
        # both = set(dates_list).intersection(old_data)
        # date_index =[dates_list.index(i) for i in both] 
        # needs +2 added for title and not 0 index, only returning 1 value!!


        # date_index = []
        # for i in old_data:
        #     if i in dates_list:
        #         for j in dates_list:
        #             if i == j:
        #                 if dates_list.index(i) not in date_index:
        #                     date_index.append(dates_list.index(i)+2)


https://stackoverflow.com/questions/51171314/find-indexes-of-common-items-in-two-python-lists
https://stackoverflow.com/questions/60825828/how-to-delete-column-by-user-input-in-excel-in-python-using-openpyxl
https://stackoverflow.com/questions/52696172/limiting-an-input-between-two-numbers-and-checking-if-the-input-is-a-number-or-n#:~:text=You%20can%20use%20a%20while,%22)

after delete row- does not update the data from spreadsheet- still shows deleted row fixed with exit()
https://pypi.org/project/colored/

