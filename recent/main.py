from flask import Blueprint,render_template, request, redirect, url_for, flash, session
from auth import session
main = Blueprint('main', __name__)

@main.route('/',methods = ["GET","POST"])
def home():
    if session:
        #print(request.args['name']," home")
        print(session['name'])
        return render_template('index.html',name = session['name'])

    #  if request.method == "GET":
    #     #print(request.args['name']," home")
    #     return render_template('index.html',name = request.args['name'])
    # print(args)
    return render_template('index.html')

@main.route('/profile')
def profile():
    return "<strong> Profile Page </strong>"
    # return render_template('profile.html')    
