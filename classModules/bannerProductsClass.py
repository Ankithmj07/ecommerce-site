from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class BannerProducts:
    def bannerPid(self,pName):
        sqlPid=text('SELECT id FROM products WHERE p_name=:pName')
        resPid=db.engine.execute(sqlPid,pName=pName)
        assocData=resPid.fetchall()

        return jsonify([dict(row) for row in assocData])
    
objBannerProducts=BannerProducts()