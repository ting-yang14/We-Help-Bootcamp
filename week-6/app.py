from flask import Flask, request, render_template, redirect, session
from member_func import add_member, check_member, add_message, get_message_content

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def home():
    if "user" in session:
        return redirect("/member")
    return render_template("home.html")

@app.route("/member")
def member():
    if "user" not in session:
        return redirect("/")
    message_content = get_message_content()
    return render_template("member.html", name = session["user"][1], message_content = message_content, len = len(message_content))

@app.route("/error")
def error():
    return render_template("error.html", msg = session["msg"])

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        if (name != "" and username != "" and password != ""):
            if add_member(name, username, password):
                return render_template("home.html")
            else:
                session["msg"] = "帳號已經被註冊"
                return redirect("/error?message="+session["msg"])
        else:
            session["msg"] = "請輸入完整資訊"
            return redirect("/error?message="+session["msg"])
    return redirect("/")

@app.route("/signin", methods = ["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        check_result = check_member(username, password)
        if check_result[0]:
            session["user"] = check_result[1]
            # session["user"] = (1, 'test2', 'test', 'test', 150, datetime.datetime(2022, 10, 17, 17, 48, 29))
            return redirect("/member")
        else:
            session["msg"] = check_result[1]
            return redirect("/error?message="+session["msg"])
    return redirect("/")

@app.route("/signout")
def signout():
    session.pop("user", None)
    return redirect("/")

@app.route("/message", methods=["POST"])
def message():
    member_id = session["user"][0]
    content = request.form["message"]
    if content != "":
        add_message(member_id, content)
    return redirect("/member")
    

if __name__ == "__main__":
    app.run(port = 3000, debug = True)