from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', Title='home')

@app.route("/about")
def about():
    return render_template('about.html', Title='about')

