from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
from classModules.customerAddressClass import objAddresses
from datetime import datetime,timedelta

class Orders:
    def insertProductOrder(self,productId,customer_id):
        sqlProd=text('SELECT * FROM products WHERE id=:productId')
        res=db.engine.execute(sqlProd,productId=productId)
        assocData=res.fetchall()
        jsonData=[dict(row) for row in assocData]
        order_list=list(jsonData)
        

        for item in order_list:
            p_discount=item.get('discount_price',None)
            p_image=item.get('p_image',None)
            p_price=item.get('product_price',None)
            p_mrp=item.get('product_original_price',None)
            p_name=item.get('product_name',None)
            p_color=item.get('p_color',None)
            d_per=item.get('discount_percentage',None)
            p_short_name=item.get('p_name',None)
        #addId=addressId

        odate=datetime.today().strftime('%Y-%m-%d')
        curr_date=datetime.today()
        new_date = curr_date + timedelta(days=5)
        ddate=new_date.strftime('%Y-%m-%d')

        sqlInsOrder=text('INSERT INTO orders(product_id,product_name,product_price,product_image,order_date,delivery_date,customer_id) VALUES(:productId,:p_name,:p_price,:p_image,:odate,:ddate,:customer_id)')
        db.engine.execute(sqlInsOrder,productId=productId,p_name=p_name,p_price=p_price,p_image=p_image,odate=odate,ddate=ddate,customer_id=customer_id)

        return "Order inserted successfully"
    
    def OrderCartProducts(self,customer_id):
        sqlCart=text('SELECT * FROM cart WHERE customer_id=:customer_id')
        res=db.engine.execute(sqlCart,customer_id=customer_id)
        assocData=res.fetchall()

        jsonData=[dict(row) for row in assocData]
        cart_list=list(jsonData)
        

        for item in cart_list:
            p_id=item.get('product_id',None)
            p_image=item.get('product_image',None)
            p_price=item.get('product_price',None)
            p_name=item.get('product_name',None)

            odate=datetime.today().strftime('%Y-%m-%d')
            curr_date=datetime.today()
            new_date = curr_date + timedelta(days=5)
            ddate=new_date.strftime('%Y-%m-%d')

            sqlInsCart=text('INSERT INTO orders(product_id,product_name,product_price,product_image,order_date,delivery_date,customer_id) VALUES(:p_id,:p_name,:p_price,:p_image,:odate,:ddate,:customer_id)')
            db.engine.execute(sqlInsCart,p_id=p_id,p_name=p_name,p_price=p_price,p_image=p_image,odate=odate,ddate=ddate,customer_id=customer_id)

        sqlcartDel=text('DELETE FROM cart WHERE customer_id=:customer_id')
        db.engine.execute(sqlcartDel,customer_id=customer_id)

        return "Order inserted successfully"
    
        
    def getOrderDetails(self,customer_id):
        sqlOrders=text('SELECT * FROM orders WHERE customer_id=:customer_id')
        res=db.engine.execute(sqlOrders,customer_id=customer_id)
        assocData=res.fetchall()

        return jsonify([dict(row) for row in assocData])
    

    def getOrderId(self):
        sqlOrderID=text("select max(order_id) as order_id from orders")
        resId=db.engine.execute(sqlOrderID)
        assocData=resId.fetchall()

        return jsonify([dict(row) for row in assocData])

objOrders=Orders()