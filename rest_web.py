#This script starts a web server on port 5000, searches and updates the zip cod database
#CNA 335, winter 19
#Parker Swift, pdsswift@student.rtc.edu



from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/search/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/update/')
def update():
   return 'test'

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/')
def root():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)