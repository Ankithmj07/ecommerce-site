from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from datetime import datetime

class customerDetails:

    def checkEmailExist(self,email):
        sqlCheckEmail=text('SELECT COUNT(*) > 0 as email_exist FROM customers WHERE EXISTS(SELECT email FROM customers WHERE email=:email);')
        resCheck=db.engine.execute(sqlCheckEmail,email=email)
        assocDataCheck=resCheck.fetchall()

        j_data=[dict(row) for row in assocDataCheck]
        checkList= list(j_data)
        for i in checkList:
            chkEmail=i.get('email_exist',None)

        return str(chkEmail)


    def insertDetails(self,name,email,phoneNumber,password):


        sqlIns=text('INSERT INTO customers(customer_name,email,phone_number,password) VALUES (:name,:email,:phoneNumber,:password);')
        db.engine.execute(sqlIns,name=name,email=email,phoneNumber=phoneNumber,password=password)

        return "Customer details successfully stored"
    
    def validateCustomer(self,Input,password):
        sqlcheck=text('SELECT customer_id FROM customers WHERE (email=:Input OR phone_number=:Input) AND password=:password')
        res=db.engine.execute(sqlcheck,Input=Input,password=password)

        assocData=res.fetchall()
        data=[dict(row) for row in assocData]
        data_list=list(data)

        for i in data_list:
            c_id=i.get('customer_id',None)
            c_id_str=str(c_id)

        if len(assocData) > 0:
            return c_id_str
        else:
            return 0

    def forgotPassword(self,email):
        self.email=email
        sqlcheckEmail=text('SELECT email FROM customers WHERE email=:email')
        res=db.engine.execute(sqlcheckEmail,email=email)

        assocData=res.fetchall()
        

        if len(assocData) > 0:
            return jsonify([dict(row) for row in assocData])
        else:
            return 0
        

    def insertCustomerId(self,c_id):
        sqlInsertCustID = text("INSERT INTO c_id(c_id) VALUES (:c_id);")
        db.engine.execute(sqlInsertCustID,c_id=c_id)

        return "Customer id inserted"
    


    def getCustomerId(self):
        sqlGetCustID = text("SELECT c_id FROM c_id WHERE id=(SELECT id FROM c_id ORDER BY id DESC LIMIT 1);")

        res=db.engine.execute(sqlGetCustID)

        assocData=res.fetchall()

        jsonData=[dict(row) for row in assocData]
        c_id_list=list(jsonData)

        c_id=None
        for item in c_id_list:
            c_id=item.get('c_id',None)
        
        if c_id is None:
            return '0'
        else:
            return str(c_id)
    

    def logout(self):
        sqlLogout=text('DELETE FROM c_id')
        db.engine.execute(sqlLogout)
        
        return "Logged out Successfully"
    

    def ResetPAssword(self,newPass):
        email=self.email
        sqlResetPassword = text("UPDATE customers SET password=:newPass WHERE email=:email;")
        db.engine.execute(sqlResetPassword, newPass=newPass, email=email)
        return "Password reset successfully"

objLogin=customerDetails()