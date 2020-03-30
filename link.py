from get import db
from flask import Flask
import mysql.connector

conn = mysql.connector.connect(host=db['host'], user=db['user'], passwd=db['passwd'], 
                                database=db['database'], charset='utf8mb4')
db=conn.cursor()
def create(name,gender,grade,area,college,phone,department,faceTime,introduction):
    db.execute('''insert into spring (`name`, `gender`,`grade`,`area`,`colleage`,`phone`,`department`,`faceTime`,`introduction`) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)''', (name,gender,grade,area,college,phone,department,faceTime,introduction))
    conn.commit()
    return db.rowcount

def find(phone):
    db.execute('select * from spring where `phone`=%s',(phone,))
    result = db.fetchall()
    return result                               