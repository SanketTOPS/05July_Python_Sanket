import pymysql

try:
    conn=pymysql.connect(host='localhost',user='root',password='',database='hellodb')
    print("Database connected!")
except Exception as e:
    print(e)

cur=conn.cursor()

# Create table
create_tbl="create table studinfo(id integer primary key auto_increment, name text, sub text)"

try:
    cur.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo (name,sub) values ('sanket','python'),('nirav','java'),('hitesh','php'),('ashok','ui'),('pritesh','android')"
try:
    cur.execute(insert_data)
    conn.commit()
    print("Record Inserted successfully!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set sub='iOS' where id=5"
try:
    cur.execute(update_data)
    conn.commit()
    print("Record Updated successfully!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where name='sanket'"
try:
    cur.execute(delete_data)
    conn.commit()
    print("Record Deleted successfully!")
except Exception as e:
    print(e)"""


# Show Data
"""show_data="select * from studinfo"
try:
    cur.execute(show_data)
    #data=cur.fetchall()
    #data=cur.fetchmany(3)
    data=cur.fetchone()
    print(data)
except Exception as e:
    print(e)"""