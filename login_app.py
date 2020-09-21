from flask import Flask, render_template, request, flash, redirect
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import login_user
from form import LoginForm

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
        return f"User('{self.name}', '{self.email}')"


@app.route("/register")
def hello():
    return "Hello World!"


@app.route("/", methods=['GET', 'POST'])
def main():
    res=request.get_json()
    print(res)
    if request.method=='POST':
        if res['id']==0:
            typeOfUser=res["selectInput_d"]
            name=res["nameInput_d"]
            email=res["emailInput_d"]
            password=res["passwordInput_d"]
            hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
            user=User(typeOfUser=typeOfUser, name=name, email=email, password=hashed_password)
            print("--------------------------------")
            print(User.query.all())
            print("User('"+name+"', '"+email+"')")
            for i in User.query.all():
                print(i)
                if str("User('"+name+"', '"+email+"')")==str(i):
                    print("nononononono")
                    #insert your code here for if user is already registered
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
            form=LoginForm()
            if form.validate_on_submit():
                user=User.query.filter_by(email=form.email.data).first()
                if user and bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    next_page=request.args.get('next')
                    flash(f'Hey {user.username}! Good to see you back ;)', category='success')
                    if next_page:
                        return redirect(next_page)
                    else:
                        return  render_template('success.html')
                else:
                    flash(f'Login Unsuccessful. Please check the email and/or Password', 'danger')  
                    
            return  render_template('success.html')
    else:        
        return render_template('main.html')


if __name__=="__main__":
    app.run(debug=True)    