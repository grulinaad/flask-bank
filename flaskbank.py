from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', Title='home')

@app.route("/about")
def about():
    return render_template('about.html', Title='about')

@app.route("/login")
def login():
    return render_template('login.html', Title='login')

@app.route("/register")
def login():
    return render_template('register.html', Title='register')


if __name__ == "__main__":
    app.run(debug=True)
