from flask import Flask, render_template
import requests
import json
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)

@app.route('/guess/<name>')
def guess(name):
    age_url = f"https://api.agify.io?name={name}"
    gender_url = f"https://api.genderize.io?name={name}"
    
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    current_year = datetime.datetime.now().year
    return render_template("guess.html", year=current_year, person_name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)