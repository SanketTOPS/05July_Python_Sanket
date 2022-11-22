import sqlite3

try:
    conn=sqlite3.connect('mydb.db')
    print("Database connected!")
except Exception as e:
    print(e)

# Create table
create_tbl="create table studinfo(id integer primary key autoincrement, name text, sub text)"

try:
    conn.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo (name,sub) values ('sanket','python'),('nirav','java'),('hitesh','php'),('ashok','ui'),('pritesh','android')"
try:
    conn.execute(insert_data)
    conn.commit()
    print("Record Inserted successfully!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set sub='iOS' where id=5"
try:
    conn.execute(update_data)
    conn.commit()
    print("Record Updated successfully!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where name='sanket'"
try:
    conn.execute(delete_data)
    conn.commit()
    print("Record Deleted successfully!")
except Exception as e:
    print(e)"""

cur=conn.cursor()

# Show Data
show_data="select * from studinfo"
try:
    cur.execute(show_data)
    x=cur.fetchall()
    #x=cur.fetchmany(3)
    #x=cur.fetchone()
    for i in x:
        #print(i)
        #print(f"Student[{x.index(i)}]={i}")
        print(f"Student[{x.index(i)}]={i[1]}")
    #print(x)
except Exception as e:
    print(e)
    