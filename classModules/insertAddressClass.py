from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class InsertAddress:
    def saveAddress(self,*addressInfo):
        country=addressInfo[0]
        fullName=addressInfo[1]
        mobileNumber=addressInfo[2]
        pincode=addressInfo[3]
        addressLine1=addressInfo[4]
        addressLine2=addressInfo[5]
        landmark=addressInfo[6]
        city=addressInfo[7]
        state=addressInfo[8]

        sqlIns=text('INSERT INTO addresses (full_name,phone_number,pincode,address_line1,address_line2,landmark,city,state,country) VALUES (:fullName,:mobileNumber,:pincode,:addressLine1,:addressLine2,:landmark,:city,:state,:country)')
        db.engine.execute(sqlIns,fullName=fullName,mobileNumber=mobileNumber,pincode=pincode,addressLine1=addressLine1,addressLine2=addressLine2,landmark=landmark,city=city,state=state,country=country)

    

        return '[{"errFlag":0,"message":"Address Info Saved Successfully"}]'
        
    
objInsertAddress=InsertAddress()

