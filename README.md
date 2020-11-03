# Milestone Project 3: InhabitU 


![https://github.com/LaiMo2020/InhabitU/blob/master/static/images/presentation-page.png](static/images/presentation-page.png)
## InhabitU
#### InhabitU is an application to facilitate and keep track on a balanced lifestyle. Options to create, edit and keep track on frequent habits in the three categories “Heart”, “Body” and “Brain” make it easy to stay motivated and keep an overview over how well we balance and spend time in the three categories.


## UX
#### The application is made for everyone that feels it hard sometimes to bring the three main categories that define our physical and mental well-being in balance. In a rushed everyday life, it can be hard to equally set out time on staying fit and healthy (“Body”), spending time with friends and family (“Heart”) as well as being focused and centred in our mind (“Brain”). Defining and following habits can help to achieve a balance, stay motivated and not forget of one of the categories. InhabitU enables the user to achieve this balance through a habit-based approach. It provides options to create habits for each three categories, edit them according to changing circumstances and keep track in a personal profile and overview.

### Wireframes
#### For the creation of my wireframes I used the Balsamiqu program (see “technologies used). Throughout the development of the webpage the wireframes were very helpful for me to reach the final design.
#### I have created mobile wireframes and desktop wireframes.


1. Desktop Wireframes

  - [Home-page](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/desktop.home%20copy.png)
  - [LogIn](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/desktop.login%20.png)

  - [Register](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/desktop.register.png)
 - [Create Habit](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/desktop.create.png)



2. Mobile Wireframes 

  - [Home-page](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/mobile.home.png)
  - [LogIn](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/mobile.login.png)

  - [Register](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/mobile.register.png)
 - [Create Habit](https://github.com/LaiMo2020/InhabitU/blob/master/static/wireframe/mobile.create%20copy.png)

## User stories
- As a user I want to create and edit a personal profile, so that I can store and return to my created habit-lists.

  InhabitU enables the user by providing an option to register in the page and create a personal profile

- As a user I want to create new habits, so that I can be more active in a certain category of my life-balance

  InhabitU enables the user in his/her profile with an option to create new habits, linked to the three categories “heart, brain and body” and add them to a personal list of active habits

- As a user I want to define new habits by name and description, so that I can easily remember and return to their purpose

  In the “create a new habit” dialogue the user can give it a name and longer description

- As a user I want to define a start-day for each habit, so that I can stay motivated and get a regularity in my daily life 

  In the “create a new habit” dialogue the user can define a start-day for the habit

- As a user I want to mark certain habits as prioritised, so that I can be remembered on what is important just now 

  In the “create a new habit” dialogue the user can set “prioritize” to the habit he or she creates

- As a user I want to edit a habit, so I can adapt it to new circumstances in my life

  InhabitU enables the user in the “my habits” overview with an option to edit existing habits

- As a user I want to delete a habit, so I can get more time to spend on another habit or category

 InhabitU enables the user in the “my habits” overview with an option to delete existing habits



Color theme
In order to make it easy for users to keep track on the three categories and linked habits the application design is based on a color-coding system, supported by icons that visualize each category. 
The overall color theme of the menu is kept in a simple and calm background color, giving space to the three categories, which are the main content and focus point for the user:
The heart category and all linked habits are designed in red, a warm color, which is commonly referred to love, and relationship related topics
The body category and all linked habits are designed in blue, a colder and dynamic color, which inspires the user to physical activities and more movement
The brain category and all linked habits are designed in green, a color that stays for growth and positivity. It inspires the user to stay focused, grow new lifestyles and be motiviated
Wireframes

Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.
In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

Features Left to Implement
Another feature idea


Header– without being logged in
The section “Home” in the header allows user that are not logged in to get information on a balanced lifestyle. To get started they can choose from options to “log in” or “register” 
“Log in” allows the user to log in to their profile by filling in their e-mail address and password. 
Pushing “register account “ at the bottom of the log-in dialogue allows the user to reach the “register” dialogue
“Register” allows the user to register a new account by filling in a user name, their e-mail address and define a password. 

Header– as a logged in user
Home
The “+” button allows the user to create a new habit

Profile
The profile enables the user to add a predefined habit to their list by choosing from one of the options in the categories
The profile enables the user to add a new custom habit to their list by pushing the “+” button

Create a new habit
The dialogue enables the user to create a custom habit by choosing categorie, filling in name, description and frequency and choosing if it is prioritized or not.
The “add new habit” button enables the user to add the filled in habit to their list by pushing the button

My habits
Provides an overview over all active habits added by the user
The habit-boxes enable the user to get more information about them by pushing the arrow 
The habit-boxes enable the user to delete a habit by pushing “delete” 
The habit-boxes enable the user to edit an existing a habit by pushing “edit” 

Log out
“Log out” enables the user to log out of his or her profile by pushing the link in the header

Features Left to Implement
A counter for the habits that helps the user to check off certain activities and follow up their frequency



Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
JQuery
The project uses JQuery to simplify DOM manipulation.

Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.
For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:
Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.


## Testing 

### Testing and review of the webpage

1. I have tested the webpage myself in the following browsers and devices:
- Google Chrome

- Safari
- Iphone XR
- MacBook Air

2. I have sent the webpage to family and friends who tested the page and responsiveness on following browser and devices:
- Google Chrome

- Safari
- iPad
- iPhone SE

### Validation of the code/ Screenshoot 

- [vlaidator/screnshoot/Craete-HTML](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/create-html.png)
- [vlaidator/screnshoot/Edit-HTML](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/edit-html.png)
- [vlaidator/screnshoot/Login-HTML](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/login-html.png)
- [vlaidator/screnshoot/Register-HTML](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/register-html.png)
- [vlaidator/screnshoot/Home-HTML](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/home-html.png)

- [vlaidator/screnshoot/CSS](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/CSS-vlaidation.png)
- [vlaidator/screnshoot/JS](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/JS%20validation.png)
- [vlaidator/screnshoot/PYTHON](https://github.com/LaiMo2020/InhabitU/blob/master/static/Validation/python%20validation-%20pep8.png)

### I have used the follwoing tech to test my code:
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
to visualise/edit my code live.
- [W3C/HTML](https://validator.w3.org/)
to check my  HTML code.

- [W3C/CSS](https://jigsaw.w3.org/css-validator/)
to check my CSS code.
- [Jshint](https://jshint.com/)
to check my JS code.
- [PEP8](http://pep8online.com/)
to check my python code
## Deployment

#### The project is stored in a Github [repository](https://github.com/LaiMo2020/InhabitU)  & hosted on [Heroku](https://inhabitu-flask-app.herokuapp.com/).



#### I have made the follwoing steps to deploye my app: 

- Creating a new databas in mongoDB
- Creating a new repo in GitHub “InhabitU”
- Opening the repo in gitpod  and create my flask app
- Create .gitignoe to stor the file I don’t want to push and make it public
- Creating env.py to stor the festive data such as secret keys
- Creating requirements.tex so gitpod knows how and what application I’m doing 
- Create Profile
- Install flask on gitpod
- Deploy my app inhabitU to Heroku
- Connect flask to mongoDB
- install flask-pymongo and dnspython



Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

### Content
The project is inspired from task manager project in the module. 

### Media
The static images used accross the page were obtained from https://unsplash.com/

### Acknowledgements
A very big thank you goes to my Code Institute Mentor Brian M. for his invaluable support and guidance throughout this project. 
Slack community and the tutor team for
### Disclaimer
The content of this website is for educational purposes only.