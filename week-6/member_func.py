import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "website"
)
def add_member(name, username, password):
    # find repeat username
    mycursor = mydb.cursor()
    sql = "SELECT username FROM member WHERE username = %s"
    adr = (username,) 
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall() # list of repeat username
    if not myresult: #  list is empty, no repeat username
        # insert new member to database
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    else:
        return False

def check_member(username, password):
    # ckeck whether member have signup
    mycursor = mydb.cursor()
    sql = "SELECT * FROM member WHERE username = %s AND password = %s"
    adr = (username, password) 
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchone() # list of signin member data
    if myresult: #  have member data
        print(myresult)
        return (True, myresult) # return is member and member data
    else: # signin fail
        return (False, "帳號或密碼輸入錯誤")

def add_message(member_id, content):
    mycursor = mydb.cursor()
    sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    val = (member_id, content)
    mycursor.execute(sql, val)
    mydb.commit() #

def get_message_content():
    mycursor = mydb.cursor()
    sql = "SELECT member.username, message.content FROM member INNER JOIN message ON message.member_id=member.id ORDER BY message.time DESC;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall() 
    return myresult # list of member name and message content 