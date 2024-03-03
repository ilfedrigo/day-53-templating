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

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", blog_post=all_posts)

if __name__ == "__main__":
    app.run(debug=True)