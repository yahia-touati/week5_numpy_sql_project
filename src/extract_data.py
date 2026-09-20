import pandas as pd
from db_connection import get_connection
#Extract all database talbes into pandas DataFrames
def extract_all_tables():

    conn = get_connection()
    df_customers = pd.read_sql("select * from customers", conn)
    df_products = pd.read_sql("select * from products", conn)
    df_orders = pd.read_sql("select * from orders", conn)
    df_order_itmes = pd.read_sql("select * from order_items", conn)
    conn.close()
    #return all DataFrames in dicitonary for easy acces
    return {
        "customers": df_customers,
        "products": df_products,
        "orders": df_orders,
        "order_items": df_order_itmes
    }