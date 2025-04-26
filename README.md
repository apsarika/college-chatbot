# college-chatbot
This project is a chatbot designed to help college students by providing real-time answers to common questions about the college. Built using Python and Flask, the chatbot utilizes TF-IDF-based semantic search to pull relevant information from a data.json file, which is populated by scraping data from the official college website. The bot answers queries on various topics such as admissions, courses, placements, and infrastructure.

##Tech Stack
Python Libraries: Flask, TF-IDF, BeautifulSoup, requests
Data: Scraped from the official college website and stored in a structured data.json file
Flask: Web framework for serving the chatbot

##Project Features
Web Interface: Interact with the chatbot through a simple web page.
Real-time Answers: Get answers to questions about the college’s infrastructure, admissions, courses, etc.
TF-IDF Semantic Search: Uses text analysis to find the most relevant information from the data.

##How to Run Locally
Clone the repository using git clone https://github.com/apsarika/college-chatbot.git, and then navigate into the project folder by running cd college-chatbot.
After that, install all the required dependencies using pip install -r requirements.txt. 
Once the dependencies are installed, run the Flask application by executing python app.py.
After the server starts, open your browser and go to http://127.0.0.1:5000/ to access the chatbot.
Make sure the data.json file is present and properly populated before running the application.

