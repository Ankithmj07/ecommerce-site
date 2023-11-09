from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from datetime import datetime

class Contact:

    def saveContact(self,*contactInfo):

        customerName=contactInfo[0]
        customerEmail=contactInfo[1]
        customerMobile=contactInfo[2]
        customerQuery=contactInfo[3]
        

        tdate=datetime.today().strftime('%Y-%m-%d')

        sqlIns=text('INSERT INTO contact_data (customer_name,email,mobile,query,date) values(:customerName,:customerEmail,:customerMobile,:customerQuery,:tdate)')
        db.engine.execute(sqlIns,customerName=customerName,customerEmail=customerEmail,customerMobile=customerMobile,customerQuery=customerQuery,tdate=tdate)

        return '[{"errFlag":0,"message":"Contact Info Saved Successfully"}]'

objContact=Contact()