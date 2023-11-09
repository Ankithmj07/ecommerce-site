from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db

class getWishlist:
    def getWishlistData(self,customer_id):
        sqlwish=text('SELECT * FROM wishlist WHERE customer_id=:customer_id')
        resWish=db.engine.execute(sqlwish,customer_id=customer_id)
        assocData=resWish.fetchall()

        return jsonify([dict(row) for row in assocData])
    
objgetWishlist=getWishlist()