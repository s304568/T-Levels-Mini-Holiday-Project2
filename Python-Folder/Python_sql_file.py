from random import randrange
import sqlite3
from sqlite3 import Error
import json


from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

with open("G:\ALEX\web_dev\T-level-mini-holiday-project\T-level-mini-holiday-project\src\Python-Folder\OneJson.json","r") as file:
    j2 = json.load(file)
    

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password') 

    Final_q= check_credentials(username, password)
    print("Final q: " + Final_q)
    queryOne(conn,Final_q)
    message = Response(conn, data)
    
    return username ,password

    
@app.route('/message', methods = ["GET"])
def get_message():
    message = request.args.get("message")
    return jsonify(message)

    if __name__ == "__main__":
        app.run(debug=True)
       


#--------------------------------------------------------------------------------------------------------
    
def check_credentials(username, password):
    for el in j2:
        q = ""
        q = q+el
        c = ""
        for el2 in j2[el]["Columns"]:
            for el3 in j2[el]["Columns"][el2]:
                c+= el2 + "." + el3 +","
            q += " " + c
            q = q[:-1]
            tb = ""
            for t in j2[el]["Table"]:
                tb += t + ","
            tb = tb[:-1]
        #print(tb)
        q += " From " + tb
        #print(q)
        where = []
        string = ""
        for el4 in j2[el]["Where"]:
            #print(el4)
            for el5 in j2[el]["Where"][el4]:
                #print(el5)
                where.append(el5)
        string1 = where[0]
        string2 = where[1]
        #print(string1)
        strTwo = ""
        strOne = ""   
        strOne = string1[0]  + " = '" + username + "'"
        strTwo = string2[0] + " = '" + password + "'"
        str3 = strOne + " And " + strTwo
        Final_q = q +" Where "+ str3

        return Final_q
    

conn = sqlite3.connect(r"G:\ALEX\web_dev\T-level-mini-holiday-project\T-level-mini-holiday-project\src\Python-Folder\UserName-PassWord.db",check_same_thread=False)


def queryOne(conn, Final_q):
    cu = conn.cursor()
    #self.cx = sqlite3.connect(file_path, check_same_thread=False)
    cu.execute(Final_q)
    conn.commit()
    data = cu.fetchall()
    
    
    return data


def Response(conn, data):
    if data:
        random_num = randrange(1, 3)
        q = "From HolidayMessages.Messages Where HolidayMessages.Messages =" + random_num
        cu = conn.cursor()
        cu.execute(q)
        conn.commit()
        message = cu.fetchall()
        print(message)
    else:
        message = "Not found"
    return message

if __name__ == "__main__":
    app.run()


q232 = """Select Games.Game_Name, From Games,Genre
Where Games.Genre = Genre.ID , Genre.Genre_Name = RPG"""

q2 = """Select UserData.UserName, UserData.Password From
UserData Where UserData.UserName = ?, UserData.Password = ?"""

qq = """Select UserData.UserName,UserData.Password From 
UserData Where UserData.UserName = zafewaf And UserData.Password = awefa"""