from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return "Hello World Page!"

@app.route('/foo')
def foo():
    return "Foo page"

@app.route('/user/<username>')
def show_user_profile(username):
    return "User %s" % username

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
