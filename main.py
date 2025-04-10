# Trigger rebuild
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from your Movie Budget Prediction App!"

@app.route("/about")
def about():
    return "This is a Movie Budget Prediction App built with ❤️ using Flask!"


if __name__ == '__main__':
    app.run(debug=True)
