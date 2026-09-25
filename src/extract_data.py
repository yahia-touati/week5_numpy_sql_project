import pandas as pd
from db_connection import get_engine
#Extract all database talbes into pandas DataFrames
def extract_all_tables():

    engine = get_engine()

    df_customers = pd.read_sql("select * from customers", engine)
    df_products = pd.read_sql("select * from products", engine)
    df_orders = pd.read_sql("select * from orders", engine)
    df_order_itmes = pd.read_sql("select * from order_items", engine)
    #return all DataFrames in dicitonary for easy acces
    return {
        "customers": df_customers,
        "products": df_products,
        "orders": df_orders,
        "order_items": df_order_itmes
    }

