import pymysql

def db_insert_task(text):
    sql = "INSERT INTO todo(task) VALUES (%s)"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (text, ))
    connection.commit()
    result = 1
    connection.close()
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
    connection.close()
    return tasks_list

def db_contains(task):
    sql = "select task from todo where task = %s"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (task, ))
    results = cursor.fetchall()
    connection.close()
    if len(results) == 0:
        return False
    else:
        return True

def db_remove_task(task):
    sql = "delete from todo where task = %s"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (task, ))
    connection.commit()
    result = 1
    connection.close()
    return result

def db_remove_multiple_tasks(text):
    sql = "delete from todo where task LIKE %s"
    text = "%" + text + "%"
    connection = pymysql.connect(user="root", password="root", host="localhost", database="task_list")
    cursor = connection.cursor()
    cursor.execute(sql, (text,))
    connection.commit()
    result = 1
    connection.close()
    return result
