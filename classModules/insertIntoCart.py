from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
import json

class CartDetails:
    def getCartProduct(self,productId,customer_id):

        sqlcart=text('SELECT id as product_id,product_name,p_name,product_price,product_original_price, CAST(product_original_price - product_price AS DECIMAL(10, 2)) as discount_price,p_image,p_color,CAST(((product_original_price - product_price)/product_original_price*100) AS INT) as discount_percentage FROM products WHERE id=:productId')
        resCart=db.engine.execute(sqlcart,productId=productId)

        assocData=resCart.fetchall()
        json_data=[dict(row) for row in assocData]
        cart_list= list(json_data)
        for item in cart_list:
            p_discount=item.get('discount_price',None)
            p_image=item.get('p_image',None)
            p_price=item.get('product_price',None)
            p_mrp=item.get('product_original_price',None)
            p_name=item.get('product_name',None)
            p_color=item.get('p_color',None)
            d_per=item.get('discount_percentage',None)
            p_short_name=item.get('p_name',None)

        
        """sqlCheckItem=text('SELECT COUNT(product_id) > 0 as item_exist FROM cart WHERE EXISTS(SELECT product_id FROM cart WHERE product_id=:productId);')
        resCheck=db.engine.execute(sqlCheckItem,productId=productId)
        assocDataCheck=resCheck.fetchall()

        j_data=[dict(row) for row in assocDataCheck]
        checkList= list(j_data)
        for i in checkList:
            chkProduct=i.get('item_exist',None)

        if chkProduct==0:"""

        sqlIns=text('INSERT INTO cart (product_id,product_name,product_price,product_original_price,product_image,product_color,discount_price,product_qty,discount_percentage,p_name,customer_id) SELECT :productId, :p_name, :p_price, :p_mrp, :p_image, :p_color,:p_discount,1,:d_per,:p_short_name,:customer_id WHERE NOT EXISTS (SELECT product_id from cart WHERE product_id=:productId AND customer_id=:customer_id)')
        db.engine.execute(sqlIns,productId=productId,p_name=p_name,p_price=p_price,p_mrp=p_mrp,p_image=p_image,p_color=p_color,p_discount=p_discount,d_per=d_per,p_short_name=p_short_name,customer_id=customer_id)

        return '[{"errFlag":1,"message":"Product Added to cart Successfully"}]'
        
        """else:
            sqlUpt=text('UPDATE cart SET product_qty=product_qty+1 WHERE product_id=:productId')
            db.engine.execute(sqlUpt,productId=productId)

            return '[{"errFlag":1,"message":"Quantity Updated in cart Successfully"}]'"""



    
objcartDetails=CartDetails()


