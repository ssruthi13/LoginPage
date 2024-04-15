from flask import Blueprint,render_template , request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
      return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods = ['GET','POST'])
def sign_up():
  if (request.method == 'POST'):
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('passwsord1')
    password2 = request.form.get('passwsord2')
    
    if len(email) < 4:
      flash('Email must be greater than 3 characters.', category = 'Error')
    elif len(firstName) < 2 :
      flash('FirstName must be greater than 1 characters.', category = 'Error')
    elif password1!=password2:
      flash('Passwords don\'t match.', category = 'Error')
    elif len(password1) < 6:
      flash("Password must be atleast 6 characters.", category='Error')
    else:
      flash('Account created!.', category = 'Success')
      
  return render_template("sign_up.html")
