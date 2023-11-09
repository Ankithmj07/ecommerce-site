from flask import Blueprint,request,render_template
from classModules.OrderClass import objOrders
from classModules.customerLoginClass import objLogin


order_blueprint=Blueprint('order_blueprint',__name__)

@order_blueprint.route('/OrderProducts/<product_id>',methods=['GET'])
def OrderProduct(product_id):
    customer_id=objLogin.getCustomerId()
    return objOrders.insertProductOrder(product_id,customer_id)

@order_blueprint.route('/OrderCart',methods=['GET'])
def orderCart():
    customer_id=objLogin.getCustomerId()
    return objOrders.OrderCartProducts(customer_id)


@order_blueprint.route('/get-orders',methods=['GET'])
def getOrders():
    customer_id=objLogin.getCustomerId()
    return objOrders.getOrderDetails(customer_id)


@order_blueprint.route('/OrderSucces',methods=["GET"])
def OrderSucces():
    return render_template('order-success.html')


@order_blueprint.route('/get-order-id',methods=["GET"])
def orderId():
    return objOrders.getOrderId()