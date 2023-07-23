from flask import Flask,request,jsonify
from flask_cors import CORS
import products_dao
from sql_connection import get_sql_connection

app=Flask(__name__)

CORS(app)

connection=get_sql_connection()

@app.route('/getProducts',methods=['GET'])
def get_products():
    products=products_dao.getallproducts(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUOM',methods=['GET'])
def getuom():
    
    uom=products_dao.get_uom(connection)
    response=jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteProduct',methods=['POST'])
def deleteproduct():
    print(request.form)
    uom=products_dao.delete_product(connection,'1')
    
    response=jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
'''
@app.route('/insertProduct',methods=['POST'])
def getuom():
    
    uom=products_dao.insert_new_product(connection,request.form['product_id'])
    response=jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
'''


if __name__=="__main__":
    print("Starting python flask server for grocery store management system")
    app.run(debug=True,port=5000)