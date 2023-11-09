from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class Wishlist:
    def wishlist(self,productId,customer_id):
        sqlWish=text('SELECT * from cart WHERE product_id=:productId AND customer_id=:customer_id')
        res=db.engine.execute(sqlWish,productId=productId,customer_id=customer_id)

        assocData=res.fetchall()
        jsonData=[dict(row) for row in assocData]
        list_data=list(jsonData)


        for item in list_data:
            p_discount_per=item.get('discount_percentage',None)
            p_discount=item.get('discount_price',None)
            p_image=item.get('product_image',None)
            p_price=item.get('product_price',None)
            p_mrp=item.get('product_original_price',None)
            p_name=item.get('product_name',None)
            p_color=item.get('product_color',None)
            p_short_name=item.get('p_name',None)

        sqlIns=text('INSERT INTO wishlist (product_id,product_name,product_price,product_original_price,product_image,product_color,discount_price,p_name,discount_percentage,customer_id) SELECT :productId, :p_name, :p_price, :p_mrp, :p_image, :p_color,:p_discount,:p_short_name,:p_discount_per,:customer_id WHERE NOT EXISTS (SELECT product_id from wishlist WHERE product_id=:productId AND customer_id=:customer_id)')
        db.engine.execute(sqlIns,productId=productId,p_name=p_name,p_price=p_price,p_mrp=p_mrp,p_image=p_image,p_color=p_color,p_discount=p_discount,p_short_name=p_short_name,p_discount_per=p_discount_per,customer_id=customer_id)

        sqlDelWish=text('DELETE FROM cart WHERE product_id=:productId AND customer_id=:customer_id')
        db.engine.execute(sqlDelWish,productId=productId,customer_id=customer_id)

        return '[{"errFlag":1,"message":"Product moved to wishlist Successfully"}]'
    

    def remove(self,productId,customer_id):
        sqlDel=text('DELETE FROM wishlist WHERE product_id=:productId AND customer_id=:customer_id')
        db.engine.execute(sqlDel,productId=productId,customer_id=customer_id)
        
        return '[{"errFlag":1,"message":"Product removed from wishlist Successfully"}]'

objWishlist=Wishlist()