from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from datetime import datetime

class productClick:

    def saveProductClick(self,productId):

        tdate=datetime.today().strftime('%Y-%m-%d')
        sqlIns=text("INSERT INTO products_clicks (product_id,date) VALUES (:productId,:tdate)")
        db.engine.execute(sqlIns,productId=productId,tdate=tdate)

        return "Product Clicked Successfully"
    

    def todayProductClicks(self):
        tdate=datetime.today().strftime('%Y-%m-%d')
        sqlTProducts=text("SELECT COUNT(product_id) as product_clicks FROM products_clicks WHERE date=:tdate")
        resTProducts=db.engine.execute(sqlTProducts,tdate=tdate)
        assocData=resTProducts.fetchall()

        return jsonify([dict(row) for row in assocData])
    
objProductClick=productClick()