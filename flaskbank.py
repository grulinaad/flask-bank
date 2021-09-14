import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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

    return app


if __name__ == "__main__":
    app.run(debug=True)
