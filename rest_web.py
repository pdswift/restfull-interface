#This script starts a web server on port 5000, searches and updates the zip cod database
#CNA 335, winter 19
#Parker Swift, pdsswift@student.rtc.edu
#some of ths code was Wyatt

import mysql.connector
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database=' zip code data',
                               buffered = True)
cursor = conn.cursor()

print('connected to  zip code data database')



@app.route('/success/<name>')
def success(name):
    cursor.execute("SELECT * FROM `zip` WHERE 'zipcode'=%s", [name])
    name = cursor.fetchall()
    return '%s' % name

@app.route('/nowupdate/<name> <name2>')
def nowupdate(name, name2):
    cursor.execute("UPDATE `zip` SET EstimatedPopulation=%s WHERE EstimatedPopulation=%s", (name2, name))
    return 'success'

@app.route('/search',methods = ['get'])
def search():
   user = request.args.get('nm')
   return redirect(url_for('success',name = user))

@app.route('/update',methods = ['POST', 'GET'])
def update():
    user = request.form['zip']
    user2 = request.form['EstimatedPopulation']
    return redirect(url_for('nowupdate', name=user, name2=user2))

@app.route('/')
def root():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)