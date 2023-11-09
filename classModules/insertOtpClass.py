from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from datetime import datetime,time

class insertOtp:
    def insertEmailOtp(self,emailOtp):
        sqlIns=text('INSERT INTO email_session (otp) VALUES (:email_otp)')
        db.engine.execute(sqlIns,email_otp=emailOtp)

        dtime=datetime.now()
        cur_time=dtime.strftime('%Y-%m-%d %H:%M:%S')

        """sqlDel=text('CREATE EVENT delete_old_rows ON SCHEDULE EVERY 1 MINUTE DO DELETE FROM email_session WHERE insert_time < :cur_time - INTERVAL 1 MINUTE;')
        db.engine.execute(sqlDel,cur_time=cur_time)"""

        return '[{"errFlag":1,"message":"Otp sended sucessfully"}]'
    
    def getEmailOtp(self):
        sqlget=text('SELECT otp FROM email_session WHERE id=(SELECT id FROM email_session ORDER BY id DESC LIMIT 1);')
        res=db.engine.execute(sqlget)

        assocData=res.fetchall()

        jsonData=[dict(row) for row in assocData]
        otp_list=list(jsonData)

        for item in otp_list:
            otp=item.get('otp',None)
        
        return otp
    
objinsertOtp=insertOtp()