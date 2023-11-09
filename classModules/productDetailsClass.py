from flask import Blueprint,request,jsonify,render_template,url_for
from sqlalchemy.sql import text
from db import db
import json

class productDetails:

    def productDetails(self):
        sqlLast=text('SELECT * FROM products WHERE id=(SELECT product_id FROM products_clicks ORDER BY id DESC LIMIT 1);')
        res=db.engine.execute(sqlLast)
        assocData=res.fetchall()
        jsonData=jsonify([dict(row) for row in assocData])

        return jsonData
        
    
    
objProductDetails=productDetails()