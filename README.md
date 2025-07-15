Green-tracker-tree Project

1. Introduction
This project, 'Green Tracker Tree', was developed as part of the B9IS123 module assessment. The purpose of this project is to provide a platform to track planted trees, their location, date planted, and health status. The application was created using Flask (Python) for the backend and HTML/CSS/JavaScript for the frontend.
2. AI and Assistance Declaration 
This project has code that I wrote with some help from a friend and AI (ChatGPT) just for refining ideas. There is no complete copy-paste code from ChatGPT in the final project without going through manual changes and testing. I used AI mainly for assistance in editing and organizing. I developed custom functions, named routes, and structured logic on my own, with a friend reviewing my work. To maintain academic honesty, any ideas from ChatGPT have been renamed, simplified, and clearly commented.Also using W3School website for learning Flask routes.
 3. Project Features
- User Login with session control
- Add, Edit, Delete tree records
- Frontend with responsive form
- Backend API using Flask
- SQLite database setup and connection
- Basic authentication using hardcoded login
- Deployed and tested locally on localhost:5000



4. What I Have to Offer
- All route functions have been renamed and commented out.
 - created an HTML layout using a CSS background and form design.
- A manual session timeout was implemented.
- A custom edit form that uses JavaScript and handles tree updates dynamically.
- Using.gitignore, the database was eliminated from Git commits
5.Project Structure
Greentracker-tree/
│
├── backend/
│ ├── app.py # Main Flask server
│ ├── test_api.py # API testing script
│
├── templates/
│ └── index.html # Web interface
│ └── login.html # Login page
│
├── static/
│ ├── style.css # Styles
│ ├── script.js # JS logic
│ └── images/ # Background image
│
└── trees.db # Local database (ignored in git)
6. Testing & Deployment
Python `requests` in `test_api.py` was used to test the API. The routes POST, GET, PUT, and DELETE were all successfully tested.
The project was manually tested using the browser interface after being deployed locally.
Commits that matched the stages of development were pushed to GitHub step-by-step.




location 
(https://www.google.com/maps?q=jinnah+stadium+sialkot)
7.Reference
https://www.geeksforgeeks.org/python/flask-app-routing
https://www.w3schools.com/python/
