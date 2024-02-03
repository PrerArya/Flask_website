from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models import db , User

app = Flask(__name__)

def create_app():

    
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database1.db" #configure database
    app.config['SECRET_KEY'] = "thisisasecret" #configure secret key
    
    db.init_app(app) #initialize database)    )
        
    import main
    app.register_blueprint(main.main)

    import auth
    app.register_blueprint(auth.auth)
    
    
    return app


if __name__ == '__main__':

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)



    ###########################################
    ## TO INITIALIZE THE DATABASE 
# >>> from __init__ import *      
# >>> from models import User
# >>> create_app()
# <Flask '__init__'>
# >>> with app.app_context():
# ...     db.create_all()