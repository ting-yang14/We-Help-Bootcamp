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

def add_member(name, username, password):
    # find repeat username
    connection = connection_pool.get_connection()
    cursor=connection.cursor()
    sql = "SELECT username FROM member WHERE username = %s"
    adr = (username,) 
    cursor.execute(sql, adr)
    result = cursor.fetchall() # list of repeat username
    if not result: #  list is empty, no repeat username
        # insert new member to database
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        cursor.execute(sql, val)
        cursor.close()
        connection.close()
        return True
    else:
        cursor.close()
        connection.close()
        return False

def check_member(username, password):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM member WHERE username = %s AND password = %s"
    adr = (username, password) 
    cursor.execute(sql, adr)
    result = cursor.fetchone() # list of signin member data
    if result: #  have member data
        cursor.close()
        connection.close()
        return (True, result) 
        # result=(1, 'test2', 'test', 'test', 150, datetime.datetime(2022, 10, 17, 17, 48, 29))
    else: # signin fail
        cursor.close()
        connection.close()
        return (False, "帳號或密碼輸入錯誤")

def add_message(member_id, content):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    val = (member_id, content)
    cursor.execute(sql, val)
    cursor.close()
    connection.close()

def get_message_content():
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = "SELECT member.username, message.content FROM member INNER JOIN message ON message.member_id=member.id ORDER BY message.time DESC;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result 

def get_member_info(username):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM member WHERE username = %s;"
    val = (username,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def update_member_name(new_name, username):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = "UPDATE member SET name = %s WHERE username = %s;"
    val = (new_name, username)
    cursor.execute(sql, val)
    cursor.close()
    connection.close()