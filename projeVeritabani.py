import sqlite3 as sql

def create_table():
    conn = sql.connect('ders.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
                    id integer PRIMARY KEY,
                    name text,
                    lastname text,
                    username text,
                    password text
                    )
                    """)
    conn.commit()
    conn.close()

def insert_table(name, lastname, username, password):
    conn = sql.connect('ders.db')
    cursor = conn.cursor()
    add_command = """INSERT INTO USERS(name, lastname, username, password) VALUES {}"""
    data = (name, lastname, username, password)
    cursor.execute(add_command.format(data))
    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('ders.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM USERS""")
    list_all = cursor.fetchall()
    for user in list_all:
        print(user)
    conn.close()

def search_username(username):
    conn = sql.connect('ders.db')
    cursor = conn.cursor()
    search_command = """SELECT * from USERS where username = '{}'"""
    cursor.execute(search_command.format(username))
    user = cursor.fetchone()
    conn.close()
    return user

def update_password(username, newPassword):
    conn = sql.connect('ders.db')
    cursor = conn.cursor()
    # sayı olsaydı sıkıntı yoktu ama string olacağı için '{}' şeklinde yazdık
    update_command = """UPDATE USERS SET password = '{}' WHERE username = '{}'"""
    cursor.execute(update_command.format(newPassword, username))
    conn.commit()
    conn.close()

def delete_account(username):
    conn = sql.connect('ders.db')
    cursor = conn.cursor()
    delete_command = """DELETE FROM USERS WHERE username = '{}'"""
    cursor.execute(delete_command.format(username))
    conn.commit()
    conn.close()

def delete_table():
    conn = sql.connect('ders.db')
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE USERS""")
    conn.commit()
    conn.close()






