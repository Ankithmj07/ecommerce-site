from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class getCartData:
    def getCartData(self,customer_id):

        sqlGet=text('SELECT * FROM cart WHERE customer_id=:customer_id')
        res=db.engine.execute(sqlGet,customer_id=customer_id)
        assocData=res.fetchall()

        return jsonify([dict(row) for row in assocData])
    

    def subTotal(self,customer_id):
        sqltotal=text('SELECT SUM(product_price) as sub_total,SUM(product_original_price) as price,SUM(discount_price) as discount,COUNT(id) as no_items,SUM(discount_percentage) AS total_discount_percentage FROM cart WHERE customer_id=:customer_id')
        restotal=db.engine.execute(sqltotal,customer_id=customer_id)
        assocData=restotal.fetchall()

        return jsonify([dict(row) for row in assocData])
    
objgetCartData=getCartData()