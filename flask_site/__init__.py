from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from flask_site import routes

# @app.route = ("/")
# def home():
#     return "Welcome to our xxx."

# @app.route = ("/swap")
# def swap():
#     return "Please select the food you want to swap with."


# if __name__ == "__main__":
#     app.run(debug=True)
    