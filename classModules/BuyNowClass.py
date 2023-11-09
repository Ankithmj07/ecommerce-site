from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class BuyNow:
    def getpId(self,productId):
        self.productId=productId

        return '[{"errFlag":1,"message":"ProductId moved to Buy now Successfully"}]'


    def getProducts(self):
        p_id=self.productId


        sqlProd=text('SELECT id as product_id,product_name,p_name,product_price,product_original_price,SUM(product_price) AS subtotal, CAST(product_original_price - product_price AS DECIMAL(10, 2)) as discount_price,p_image,p_color,CAST(((product_original_price - product_price)/product_original_price*100) AS INT) as discount_percentage FROM products WHERE id=:p_id')

        resProd=db.engine.execute(sqlProd,p_id=p_id)

        assocData=resProd.fetchall()

        return jsonify([dict(row) for row in assocData])
    

    def getCartProducts(self,customer_id):  
        sqlGet=text('SELECT * FROM cart WHERE customer_id=:customer_id')
        res=db.engine.execute(sqlGet,customer_id=customer_id)
        assocData=res.fetchall()

        return jsonify([dict(row) for row in assocData])

objBuynow=BuyNow()
