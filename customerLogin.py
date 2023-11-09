from flask import Blueprint,request,session,render_template,json
import hashlib
from classModules.emailverificationClass import *
from classModules.insertOtpClass import objinsertOtp
from classModules.customerLoginClass import objLogin
from classModules.insertAddressClass import objInsertAddress
from classModules.customerAddressClass import objAddresses

emailVerification_blueprint=Blueprint('emailVerification_blueprint',__name__)
customerDetails_blueprint=Blueprint('customerDetails_blueprint',__name__)

@emailVerification_blueprint.route('/chkemail',methods=["POST"])
def chkEMail():
    email = request.form['email']
    return objLogin.checkEmailExist(email)



@emailVerification_blueprint.route("/verifyEmail",methods=['POST'])
def verifyEmail():
    emailId=request.form['userEmail']
    current_otp = sendEmailVerificationRequest(receiver=emailId)
    return objinsertOtp.insertEmailOtp(current_otp)
    

@emailVerification_blueprint.route("/validateEmailOtp",methods=['POST'])
def validateEmailOtp():
    
    user_otp=request.form['userOtp']
    emailOtp=objinsertOtp.getEmailOtp()
    
    if int(user_otp)==int(emailOtp):
        return '1'
    else:
        return '0'
    

@customerDetails_blueprint.route("/loginPage",methods=['GET'])
def loginPage():
    return render_template('customer-login.html')


@customerDetails_blueprint.route("/insert-customer-Details",methods=['POST'])
def insCustomer():
    Name=request.form["Name"]
    Email=request.form["Email"]
    PhoneNumber=request.form["PhoneNumber"]
    Password=request.form["Password"]

    encPassword = hashlib.sha256(Password.encode('utf-8')).hexdigest()

    return objLogin.insertDetails(Name,Email,PhoneNumber,encPassword)



@customerDetails_blueprint.route("/customer-login",methods=["POST"])
def login():
    Input= request.form["InputText"]
    password=request.form["password"]

    encPassword=hashlib.sha256(password.encode('utf-8')).hexdigest()

    resultValue=objLogin.validateCustomer(Input,encPassword)

    if resultValue==0:
        return '0'
    else:
        InsCid=objLogin.insertCustomerId(resultValue)
        return InsCid
    
@customerDetails_blueprint.route("/customer-id",methods=['GET'])
def customerId():
    return objLogin.getCustomerId()   
    
       

@customerDetails_blueprint.route("/homePage",methods=['GET'])
def homePage():
    return render_template('index.html')



@customerDetails_blueprint.route("/check-email",methods=['POST'])
def checkEmail():
    emailId=request.form["emailId"]

    resultValue=objLogin.forgotPassword(emailId)

    if resultValue==0:
        return '0'
    else:
        return resultValue
    

@customerDetails_blueprint.route("/logout",methods=["GET"])
def logout():
    return objLogin.logout()


@customerDetails_blueprint.route('/ResetPassword',methods=["POST"])
def ResetPassword():
    newPass = request.form["newPass"]
    encNewPassword=hashlib.sha256(newPass.encode('utf-8')).hexdigest()
    return objLogin.ResetPAssword(encNewPassword)


@customerDetails_blueprint.route('/GoToResetPassword',methods=["GET"])
def GoToResetPassword():
    return render_template('reset-password.html')