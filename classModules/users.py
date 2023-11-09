from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db


class Users:
    # Check Username and Password for Validity
    def validateCred(self,username,password):

        sqlCred=text('SELECT * FROM admin_users WHERE username=:username AND password=:password AND status=1') # parameter binding
        resObj=db.engine.execute(sqlCred,username=username,password=password)
        assocData = resObj.fetchall()
        if len(assocData) > 0:
            return jsonify([dict(row) for row in assocData])
        else:
            return 0
        

# object for class User
objUsers=Users()
