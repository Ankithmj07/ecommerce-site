from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from datetime import datetime

class OtherBrands:
    def OneplusData(self):
        sqlOneplus=text('SELECT * FROM `products` WHERE p_name LIKE "%oneplus%";')
        resOneplus=db.engine.execute(sqlOneplus)
        assocData=resOneplus.fetchall()

        return jsonify([dict(row) for row in assocData])
    

    def SamsungData(self):
        sqlSamsung=text('SELECT * FROM `products` WHERE p_name LIKE "%samsung%";')
        resSamsung=db.engine.execute(sqlSamsung)
        assocData=resSamsung.fetchall()

        return jsonify([dict(row) for row in assocData])
    
    def RedmiData(self):
        sqlRedmi=text('SELECT * FROM `products` WHERE p_name LIKE "%redmi%";')
        resRedmi=db.engine.execute(sqlRedmi)
        assocData=resRedmi.fetchall()

        return jsonify([dict(row) for row in assocData])
    
ObjOtherBrands=OtherBrands()