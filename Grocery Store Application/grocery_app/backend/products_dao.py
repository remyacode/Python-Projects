from sql_connection import get_sql_connection

def getallproducts(connection):
    #connection is in another file

    cursor=connection.cursor()
    query=("""
        SELECT products.product_id, products.name, products.un_id, products.price_per_unit, um.um_name
        FROM products
        INNER JOIN um ON products.un_id = um.um_id
    """)
    cursor.execute(query)

    response=[]

    for (product_id,name,un_id,price_per_unit,um_name) in cursor:
        response.append(
            {
            'product_id':product_id,
            'name':name,
            'un_id':un_id,
            'price_per_unit':price_per_unit,
            'um_name':um_name
            }
            )

    return response

def get_uom(connection):
    #connection is in another file

    cursor=connection.cursor()
    query=("""SELECT * FROM um""")
    cursor.execute(query)

    response=[]

    for (um_id,um_name) in cursor:
        response.append(
            {
            'um_id':um_id,            
            'um_name':um_name
            }
            )

    return response

def insert_new_product(connection,product):
    cursor=connection.cursor()

    query=("""
           INSERT INTO products
           (name,un_id,price_per_unit)
           VALUES (%s,%s,%s)
           """)
    data=(product['product_name'],product['un_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor=connection.cursor()
    query=("DELETE FROM products WHERE product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()



if __name__=='__main__':
    connection=get_sql_connection()
    

#Sequelize('expense','root','your_new_password',{dialect:'mysql',host:'localhost'})