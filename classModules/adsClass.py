from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from datetime import datetime

class ads:

    def saveAdClicks(self):
        # check ad clicks for today
        tdate=datetime.today().strftime('%Y-%m-%d')
        sqlChk=text('SELECT * FROM ads WHERE date=:tdate')
        resChk=db.engine.execute(sqlChk,tdate=tdate)
        assocData=resChk.fetchall()

        
        if len(assocData) > 0:
            # update Click count by 1
            newClickCount=assocData[0].clicks + 1

            sqlUpd=text('UPDATE ads SET clicks=:newClick WHERE date=:tdate')
            db.engine.execute(sqlUpd,newClick=newClickCount,tdate=tdate)

        else:
            # insert data into table
            sqlIns = text('INSERT INTO ads (date , clicks ) VALUES (:tdate,1)')
            db.engine.execute(sqlIns,tdate=tdate)

        return '[{"errFlag":0."message":"Ads Click Logged Successfully"}]'
    
    def todayAdClicks(self):
        tdate=datetime.today().strftime('%Y-%m-%d')
        sqlTAds=text('SELECT clicks FROM ads WHERE date=:tdate')
        resAds=db.engine.execute(sqlTAds,tdate=tdate)
        assocData=resAds.fetchall()


        return jsonify([dict(row) for row in assocData])
    
objAds=ads()