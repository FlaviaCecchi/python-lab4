import pymysql

def db_insert_task(text):
    sql = "INSERT INTO todo(task) VALUES (?)"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (text, ))
    connection.commit()
    conn.close()
    return result

def get_sorted_tasks_list():
    tasks_list = []
    sql = "SELECT task FROM todo order by task ASC"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for task in results:
        tasks_list.append(task[0])
    conn.close()
    return tasks_list

def db_contains(task):
    sql = "select task from todo where task = ?"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (task, ))
    results = cursor.fetchall()
    conn.close()
    if (len(results) == 0):
        return False
    else:
        return True

def db_remove_task(task):
    sql = "delete from todo where task = ?"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (task, ))
    conn.commit()
    result = 1
    conn.close()
    return result

def db_remove_multiple_tasks(text):
    sql = "delete from todo where task LIKE ?"
    text = "%" + text + "%"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (text,))
    conn.commit()
    result = 1
    conn.close()
    return result