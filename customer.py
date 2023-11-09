from flask import Blueprint,request,render_template
from classModules.customerAddressClass import objAddresses
from classModules.insertAddressClass import objInsertAddress
from classModules.customerLoginClass import objLogin

customer_blueprint=Blueprint('customer_blueprint',__name__)


@customer_blueprint.route('/save-address',methods=['POST'])
def saveAddress():
    country=request.form['country']
    fullName=request.form['fullName']
    mobileNumber=request.form['mobileNumber']
    pincode=request.form['pincode']
    addressLine1=request.form['addressLine1']
    addressLine2=request.form['addressLine2']
    landmark=request.form['landmark']
    city=request.form['city']
    state=request.form['state']

    if not fullName and not mobileNumber and not pincode and not addressLine1 and not addressLine2 and not landmark and not city:
        return '[{"errFlag":1,"message":"Some Fields are Empty"}]'
    
    return objInsertAddress.saveAddress(country,fullName,mobileNumber,pincode,addressLine1,addressLine2,landmark,city,state)


@customer_blueprint.route('/getAddresses',methods=['GET'])
def addressData():
    c_id=objLogin.getCustomerId()

    
    return objAddresses.getAddresses(c_id)



@customer_blueprint.route('/sendAddress/<address_id>',methods=['GET'])
def sendAddress(address_id):

    return objAddresses.sendAddress(address_id)


@customer_blueprint.route('/CustomerLogin',methods=["GET"])
def CustomerLogin():
    return render_template('customer-login.html')


@customer_blueprint.route('/customerSignUp',methods=["GET"])
def customerSignup():
    return render_template('sign-up.html')

@customer_blueprint.route('/goToForgot',methods=["GET"])
def ForgotPass():
    return render_template('forgot-password.html')
    