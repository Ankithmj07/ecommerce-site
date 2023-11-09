from flask import Blueprint,request,jsonify,render_template,url_for
from sqlalchemy.sql import text
from db import db
import json

class Search:
    def searchProducts(self,product_name):
        p_name_value=product_name

        sqlSearch=text('SELECT id,p_name FROM `products` WHERE p_name LIKE :p_name;')
        res=db.engine.execute(sqlSearch,{'p_name': f"%{p_name_value}%"})
        assocData=res.fetchall()

        return jsonify([dict(row) for row in assocData])
    
    
objSearch=Search()    