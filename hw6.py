import sqlite3
connect=sqlite3.connect('hw6.db')
cursor=connect.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS to_do_list(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        status BOOLEAN NOT NULL DEFAULT FALSE,
        date DATE
    )
""")

def register():
    description=input('Описание задачи:')
    status=bool(input('Введите статус задачи:'))
    date=input('Введите дату создание задачи:')


    cursor.execute("""INSERT INTO to_do_list
                   (description, status, date)
                   VALUES (?, ?, ?)""", (description, status, date))
    connect.commit()

def update_task_status(new_status, task_id):
    cursor.execute("""
        UPDATE to_do_list 
        SET status = ? 
        WHERE id = ?
    """, (new_status, task_id))
    connect.commit()

        
def delete_task(task_id):
    cursor.execute("DELETE FROM to_do_list WHERE id=?", (task_id,))
    connect.commit()


def all_tasks():
    cursor.execute("SELECT *FROM to_do_list")
    tasks=cursor.fetchall()
    print(tasks)

def find(status):
    cursor.execute("SELECT * FROM to_do_list WHERE status = ?", (status,))
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Описание: {task[1]}, Статус: {'Завершена' if task[2] else 'Незавершена'}, Дата: {task[3]}")
   
register()
find(True)
update_task_status(True, 4)
delete_task(1)
all_tasks()