import sqlite3
import os

db_path = os.getenv('DB_PATH')
#db_path = 'datab.db'


def init():
    with sqlite3.connect(db_path) as con:

        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY, 
                    title TEXT,
                    description TEXT,
                    category TEXT,
                    price DOUBLE,
                    rating INTEGER,
                    stock INTEGER
                    )
                ''')

        cur.execute('SELECT COUNT(*) FROM products')
        row_count = cur.fetchone()[0]
        
        if row_count == 0:
            cur.execute('''INSERT INTO products (
                        "product_id" ,
                        "title" ,
                        "description" ,
                        "category" ,
                        "price" ,
                        "rating" ,
                        "stock")
                        VALUES (1234,"product1","description1","category1",100,5,10)
                        
                        ''')
            con.commit()

            
def read_all():
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        if len(rows) == 0:
            return None
        
        products = [{"product_id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "category": row[3],
                    "price": row[4],
                    "rating": row[5],
                    "stock":row[6] } for row in rows]

    return products
        
def read(id):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM products WHERE product_id = ?", (id,))
        row = cur.fetchone()

        if row:
            product = [{"product_id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "category": row[3],
                    "price": row[4],
                    "rating": row[5],
                    "stock":row[6]}]
        else:
            return None
        
    return product

        
def create(product):
    with sqlite3.connect(db_path) as conn:
        
    
        cur = conn.cursor()
       
        cur.execute('''
            INSERT INTO products (
                        "product_id" ,
                        "title" ,
                        "description" ,
                        "category" ,
                        "price" ,
                        "rating" ,
                        "stock")
                        VALUES (:product_id,:title,:description,:category,:price,:rating,:stock)''', product[0])
       
        
        new_product_id = cur.lastrowid

        conn.commit()

    return new_product_id



def delete(id):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE product_id= ?", id)
        conn.commit()


