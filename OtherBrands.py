from flask import Blueprint,request,render_template
from classModules.otherBrandClass import ObjOtherBrands

otherBrands_blueprint=Blueprint('otherBrands_blueprint',__name__)

@otherBrands_blueprint.route('/OnePlus',methods=["GET"])
def goToOneplus():
    return render_template("oneplus.html")

@otherBrands_blueprint.route('/oneplus-data',methods=["GET"])
def OneplusData():
    return ObjOtherBrands.OneplusData()

@otherBrands_blueprint.route('/Samsung',methods=["GET"])
def goToSamsung():
    return render_template("samsung.html")

@otherBrands_blueprint.route('/SamsungData',methods=["GET"])
def SamsungData():
    return ObjOtherBrands.SamsungData()

@otherBrands_blueprint.route('/Redmi',methods=["GET"])
def goToRedmi():
    return render_template("redmi.html")

@otherBrands_blueprint.route('/DataofRedmi',methods=["GET"])
def RedmiData():
    return ObjOtherBrands.RedmiData()
