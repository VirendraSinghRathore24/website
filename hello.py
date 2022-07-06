from flask import Flask, render_template, request
app = Flask(__name__)

FILE_NAME = "D:\\Work\\test.txt"


@app.route('/')
def hello_world():
    return render_template("login.html")


@app.route("/register", methods=["POST"])
def register():
    return render_template("entry.html")


@app.route("/account", methods=["POST"])
def account():
    username = request.form["username"]
    password = request.form["password"]

    with open(FILE_NAME, "a") as file:
        file.write(f"\n{username}:{password}")
    return f"user {username} registered successfully !!!"


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return validate_login(name, password)


def validate_login(username, password):
    with open(FILE_NAME) as file:
        contents = file.readlines()
        for c in contents:
            details = c.split(':')
            if details[0] == username and details[1] == password:
                return "<h2>Login successful !!!<h2>"
        else:
            return "<h2>Login failed !!!<h2>"
#
# @app.route('/insert/<name>')
# def haa(name):
#     return "abc"


if __name__ == "__main__":
    app.run(debug=True)
