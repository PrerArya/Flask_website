from flask import Blueprint,render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db , User


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            # try :
                global session
                email = request.form.get('email.signIn')
                password = request.form.get('password.signIn') 
                user = User.query.filter_by(email=email).first()
                print(user)
                if user:
                    if user.check_password(request.form.get('password.signIn')):
                        session['name'] = user.name
                        return redirect(url_for("main.home"))
                    else:
                        return render_template('login.html', error="Password Incorrect")
                else:
                    return render_template('login.html', error="Incorrect Username")

                return render_template('login.html')
        else:

            return render_template('login.html')


@auth.route('/logout')
def logout():

    return render_template('logout.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form.get('name.signUp')
        email = request.form.get('email.signUp')
        # password = request.form.get('password.signUp')
        user = User(name=name, email=email)
        user.set_password(request.form['password.signUp'])
        db.session.add(user)
        db.session.commit()
        print("Commited user:" , name)
        #flash
        return redirect(url_for("auth.login"))
        # return "<h1> Logged in </h1>"
    return redirect(url_for("auth.login"))

