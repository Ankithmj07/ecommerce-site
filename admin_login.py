from flask import Blueprint,request,render_template
from classModules.users import objUsers
import hashlib

users_blueprint=Blueprint('users_blueprint',__name__)
@users_blueprint.route('/validate-cred',methods=['POST'])

def chkAdminUser():
    username=request.form['username']
    password=request.form['password']

    if not username and not password:
        return '[{"errFlag":1,"message":"Please Enter Username and Password"}]'
    
    if not username:
        return '[{"errFlag":1,"message":"Please Enter Username"}]'       
    if not password:
        return '[{"errFlag":1,"message":"Please Enter Password"}]'        # json serialization
    
    # Encrypt Password to sha256
    encPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()

    resultValue = objUsers.validateCred(username,encPassword)

    if resultValue==0:
        return '[{"errFlag":1,"message":"Invalid Username and Password"}]'
    else:
        return resultValue
    
@users_blueprint.route('/AdminLogin',methods=["GET"])
def AdminLoginPage():
    return render_template('admin-login.html')


@users_blueprint.route('/AdminDashBoard',methods=["GET"])
def AdminDash():
    return render_template('admin-dashboard.html')