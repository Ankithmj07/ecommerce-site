from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class DeleteCart:
    def deleteCart(self,productId,customer_id):
        sqlDel=text('DELETE FROM cart WHERE product_id=:productId AND customer_id=:customer_id')
        db.engine.execute(sqlDel,productId=productId,customer_id=customer_id)
        
        return '[{"errFlag":1,"message":"Product deleted from cart Successfully"}]'
    
objDeleteCart=DeleteCart()