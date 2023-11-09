from flask import Blueprint,request
from classModules.visitorClass import objVisitors
from classModules.adsClass import objAds
from classModules.productClickClass import objProductClick
from classModules.visitorClass import objVisitors


admin_dashboard_blueprint=Blueprint(__name__,'admin_dashboard_blueprint')
@admin_dashboard_blueprint.route('/today-visitors',methods=['GET'])

def tVisitors():
    return objVisitors.todayVisitors()

@admin_dashboard_blueprint.route('/today-ad-clicks',methods=['GET'])
def tAdsClicks():
    return objAds.todayAdClicks()

@admin_dashboard_blueprint.route('/today-products-clicks',methods=['GET'])
def tProductClicks():
    return objProductClick.todayProductClicks()

@admin_dashboard_blueprint.route('/visitor-trend',methods=['GET'])
def visitorTrend():
    return objVisitors.visitorsTrend()