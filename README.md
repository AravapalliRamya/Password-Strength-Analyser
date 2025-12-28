# Password Strength Analyzer

A Python Flask-based web application that analyzes password strength and provides
a strength percentage along with the estimated time required to crack the password.

## Features
- Calculates password strength based on:
  - Length
  - Uppercase and lowercase characters
  - Numbers
  - Special characters
- Displays password strength percentage
- Estimates time required to crack the password
- Simple and user-friendly interface

## Tech Stack
- Python
- Flask
- HTML
- CSS
- JavaScript

## How to Run the Project
1. Clone the repository:
   git clone https://github.com/AravapalliRamya/Password-Strength-Analyser.git
2. Navigate to the project folder:
   cd Password-Strength-Analyser
3. Install dependencies:
   pip install flask
4. Run the application:
   python app.py
5. Open browser and go to:
   http://127.0.0.1:5000/

## Future Improvements
- Use hashing algorithms like bcrypt
- Add database support
- Improve cracking time estimation
