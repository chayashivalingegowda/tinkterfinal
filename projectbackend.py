import sqlite3
import datetime
#BackEnd


currentDateTime = datetime.datetime.now()
currentDate = currentDateTime.date()
def studentdata():
    con=sqlite3.connect("GemData.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, StdID text, Fname text, Lname text, Timestamp TIMESTAMP, Date TIMESTAMP )")
    con.commit()
    con.close()

def addStdRec(StdID, Fname , Lname):
    studentdata()
    con = sqlite3.connect("GemData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?)", (StdID, Fname , Lname , currentDateTime, currentDate))
    con.commit()
    con.close()

def Viewdata():
    con = sqlite3.connect("GemData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    row=cur.fetchall()
    con.close()
    return row

def deletRec(id):
    con = sqlite3.connect("GemData.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close()

def searchdata(StdID="", Fname="" , Lname=""):
    con = sqlite3.connect("GemData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Fname=? OR Lname=?",\
                (StdID, Fname , Lname ))
    row = cur.fetchall()
    con.close()
    return row

