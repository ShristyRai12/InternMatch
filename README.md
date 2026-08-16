# InternMatch

**InternMatch** is an internship recommendation web application that helps students find internships based on their skills and preferences.

The application analyzes the skills entered by a user and recommends relevant internships based on their skill match, preferred work mode, and location.

## Features

* Enter multiple skills to find relevant internships
* Filter internships by work mode
* Filter internships by location
* Calculate an internship **match score**
* Display matched skills for each recommendation
* Identify **skills to learn** for better matches
* Show internship details such as company, category, stipend, location, and application deadline
* Handle invalid or unrecognized skills

## Tech Stack

* **Python**
* **Pandas**
* **Flask**
* **HTML**
* **CSS**

## How It Works

1. The user enters their skills.
2. The user selects their preferred work mode and location.
3. InternMatch compares the user's skills with the skills required for available internships.
4. A match score is calculated for each internship.
5. The most relevant internships are displayed.
6. The application also highlights matched skills and skills the user could learn to improve their chances.

## Project Structure

```text
InternMatch/
│
├── app.py
├── data/
│   └── indian_tech_career_intelligence_2026.csv
│
├── src/
│   └── recommender.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── .gitignore
└── README.md
```

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/ShristyRai12/InternMatch.git
```

### 2. Navigate to the project

```bash
cd InternMatch
```

### 3. Install the required libraries

```bash
pip install pandas flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## Dataset

The project uses the **India Tech Career Intelligence [1M]** dataset from Mendeley Data.

The dataset is licensed under **CC BY 4.0**.

Dataset source: https://data.mendeley.com/datasets/h2rmbfr68t/1

## Future Improvements

* Add direct application links for internships
* Add more advanced recommendation techniques
* Improve the user interface
* Add more filtering options
* Deploy the application online
* Add user profiles and personalized recommendations

## Project Status

🚀 **First version completed**

This is my first end-to-end project, built while learning Python, data processing, recommendation logic, Flask, and web development.
