from flask import Flask,render_template, request
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/createAccount"
mongodb = PyMongo(app).db.users

@app.get('/signup')
def register():
    return render_template('signup.html')

@app.post('/signup')
def create():
    name=request.form['fname']
    username=request.form['username']
    email=request.form['email']
    password=request.form['password']

    if not name or not username or not email or not password:
        return render_template('signup.html',error = "fill up the required fields")
    
    elif mongodb.find_one({'username':username}):
        return render_template('signup.html',error = "username already exist")
    
    elif mongodb.find_one({'email':email}):
        return render_template('signup.html',error = "email already exist")

    sp = bcrypt.generate_password_hash(password).decode('utf-8')

    mongodb.insert_one({'name':name,'username':username, 'email':email,'password':sp})
    print(name,username,email,password)
    return render_template('signin.html')


@app.get('/login')
def show():
    return render_template('signin.html')



@app.post('/login')
def login():
    # username=request.form['username']
    email=request.form['email']
    password=request.form['password']

    # login_user = mongodb.find_one({'username':username})
    login_user = mongodb.find_one({'email':email})

    if login_user:
       dp =bcrypt.check_password_hash(login_user['password'],password)
       if dp:
           return render_template('landingpage.html')
    return render_template('signin.html',error = "Wrong username and password")
app.run(debug=True,port=4000)