from mysql.connector import pooling

connection_pool = pooling.MySQLConnectionPool(
    pool_name = "test",
    pool_size = 5,
    pool_reset_session = True,
    host = "localhost",
    user = "root",
    password = "test1234",
    database = "website",
    autocommit = True
)
connection_object = connection_pool.get_connection()
cursor=connection_object.cursor()

def add_member(name, username, password):
    # find repeat username
    sql = "SELECT username FROM member WHERE username = %s"
    adr = (username,) 
    cursor.execute(sql, adr)
    result = cursor.fetchall() # list of repeat username
    if not result: #  list is empty, no repeat username
        # insert new member to database
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        cursor.execute(sql, val)
        return True
    else:
        return False

def check_member(username, password):
    # ckeck whether member have signup
    sql = "SELECT * FROM member WHERE username = %s AND password = %s"
    adr = (username, password) 
    cursor.execute(sql, adr)
    result = cursor.fetchone() # list of signin member data
    if result: #  have member data
        return (True, result) # return is member and member data
    else: # signin fail
        return (False, "帳號或密碼輸入錯誤")

def add_message(member_id, content):
    sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    val = (member_id, content)
    cursor.execute(sql, val)

def get_message_content():
    sql = "SELECT member.username, message.content FROM member INNER JOIN message ON message.member_id=member.id ORDER BY message.time DESC;"
    cursor.execute(sql)
    result = cursor.fetchall() 
    return result # list of member name and message content 