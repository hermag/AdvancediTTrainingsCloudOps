from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/about")
def about():
    return "<h1 style='color:red'>About!</h1>"

@app.route("/home")
def home():
    return "<h1 style='color:blue'>Home!</h1>"


if __name__=="__main__":
    app.run()
