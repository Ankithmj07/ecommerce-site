from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from datetime import datetime

class Visitors:

    def saveVisitors(self):
        # check ad clicks for today
        tdate=datetime.today().strftime('%Y-%m-%d')
        sqlChk=text('SELECT * FROM visitors WHERE date=:tdate')
        resChk=db.engine.execute(sqlChk,tdate=tdate)
        assocData=resChk.fetchall()

        
        if len(assocData) > 0:
            # update Click count by 1
            newVisitorCount=assocData[0].visitor_count + 1

            sqlUpd=text('UPDATE visitors SET visitor_count=:newCount WHERE date=:tdate')
            db.engine.execute(sqlUpd,newCount=newVisitorCount,tdate=tdate)

        else:
            # insert data into table
            sqlIns = text('INSERT INTO visitors (date , visitor_count ) VALUES (:tdate,1)')
            db.engine.execute(sqlIns,tdate=tdate)

        return '[{"errFlag":0,"message":"Visitor Count Logged Successfully"}]'
    
    def todayVisitors(self):
        tdate=datetime.today().strftime('%Y-%m-%d')
        sqlTVisitors=text('SELECT visitor_count from visitors WHERE date=:tdate')
        resVisitors=db.engine.execute(sqlTVisitors,tdate=tdate)
        assocData=resVisitors.fetchall()

        return jsonify([dict(row) for row in assocData])
    
    def visitorsTrend(self):
    
        sqlTrend=text('SELECT SUM(visitor_count) as monthly_visitors,MONTH(date) as month FROM visitors WHERE DATE_FORMAT(date,"%c") IN (1,2,3,4,5,6,7,8,9,10,11,12)')
        resTrend=db.engine.execute(sqlTrend)
        assocData=resTrend.fetchall()
        return jsonify([dict(row) for row in assocData])
    
objVisitors=Visitors()