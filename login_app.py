from flask import Flask, render_template, request, flash, redirect
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='12334566545443234323432'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    typeOfUser=db.Column(db.String(10), nullable=False)
    name=db.Column(db.String(150), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.username}')"


@app.route("/register")
def hello():
    return "Hello World!"


@app.route("/", methods=['GET', 'POST'])
def main():
    res=request.get_json()
    if request.method=='POST':
        if res['id']==0:
            typeOfUser=res["selectInput_d"]
            name=res["nameInput_d"]
            email=res["emailInput_d"]
            password=res["passwordInput_d"]
            hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
            user=User(typeOfUser=typeOfUser, name=name, email=email, password=hashed_password)
            print(0)
            print(res)
            try:
                db.session.add(user)
                db.session.commit()
                print("User Registered")
                return redirect("tp.html")
            except:
                print("User Not Registered")
                return render_template("main.html")    
            
        else:  
            print(0)
            print(res) 
    else:        
        return render_template('main.html')


if __name__=="__main__":
    app.run(debug=True)    