from flask import Flask, request, render_template, redirect, session, jsonify
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from member_func import add_member, check_member, add_message, get_message_content, get_member_info, update_member_name

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def home():
    if "user" in session:
        return redirect("/member")
    return render_template("home.html")

@app.route("/member")
def member():
    if "username" not in session:
        return redirect("/")
    message_content = get_message_content()
    return render_template("member.html", name = session["name"], message_content = message_content, len = len(message_content))

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
            session["id"] = check_result[1][0]
            session["name"] = check_result[1][1]
            session["username"] = check_result[1][2]
            
            return redirect("/member")
        else:
            session["msg"] = check_result[1]
            return redirect("/error?message="+session["msg"])
    return redirect("/")

@app.route("/signout")
def signout():
    session.pop("id", None)
    session.pop("name", None)
    session.pop("username", None)
    return redirect("/")

@app.route("/message", methods=["POST"])
def message():
    member_id = session["id"]
    content = request.form["message"]
    if content != "":
        add_message(member_id, content)
    return redirect("/member")
    
@app.route("/api/member", methods=["GET"])
def get():
    if "username" in session:
        try:
            member = request.args.get("username", None)
            result=get_member_info(member)
            return jsonify({"data":{"id":result[0],"name":result[1],"username":result[2]}})
        except:
            return jsonify({"data":None})
    return jsonify({"data":None})

@app.route("/api/member", methods=["PATCH"])
def patch():
    if "username" in session:
        try:
            request_params=request.get_json()
            new_name=request_params["name"]
            update_member_name(new_name,session["username"])
            session["name"]=new_name
            return jsonify({"ok":True})
        except:
            return jsonify({"error":True})
    return jsonify({"error":True})

if __name__ == "__main__":
    app.run(port = 3000, debug = True)