from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
# 建立 Application 物件，可以設定靜態檔案的路徑處理
app=Flask(
    __name__, 
    static_folder="static",
    static_url_path="/"
)

app.secret_key = 'secret'

# 建立路徑 / 對應的處理函式
@app.route("/")
def home():
    if "username" in session:
        return redirect("/member")
    else:
        return render_template("home.html")

# 使用 POST 方法接收 username, password
@app.route("/signin", methods=["POST"])
def signin():
    # 接收 POST 方法的 Query string
    user=request.form["username"]
    # 接收 POST 方法的 Query string
    password=request.form["password"]
    # session["password"]=password
    if ((user=="test") & (password=="test")):
        session["username"]=user
        return redirect("/member")
    elif ((user=="") | (password=="")):
        session["message"]="請輸入帳號、密碼"
        return redirect("/error?message="+session["message"])
    else:
        session["message"]="帳號、或密碼輸入錯誤"
        return redirect("/error?message="+session["message"])

# 登入成功
@app.route("/member")
def member():
    if "username" not in session:
        return redirect("/")
    return render_template("member.html", data=session["username"])

# 登入失敗
@app.route("/error")
def error():
    return render_template("error.html", data=session["message"])

# 登出
@app.route("/signout")
def signout():
    session.pop("username", None)
    return redirect("/")

# 導向計算結果網址
@app.route("/square")
def square():
    positiveNum=request.args.get("positiveNum")
    return redirect(url_for(".result", positiveNum=positiveNum))

# 顯示計算結果
@app.route("/square/<positiveNum>")
def result(positiveNum):
    redirect("/square/<positiveNum>")
    result=int(positiveNum)**2
    return render_template("square.html", data=result)

# 啟動網站伺服器，透過 port 指定埠號 3000
app.run(port=3000)