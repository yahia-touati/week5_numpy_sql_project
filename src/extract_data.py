import pandas as pd
from db_connection import get_connection

def extract_all_tables():
    conn = get_connection()
    df_customers = pd.read_sql("select * from customers", conn)
    df_products = pd.read_sql("select * from products", conn)
    df_orders = pd.read_sql("select * from orders", conn)
    df_order_times = pd.read_sql("select * from order_items", conn)
    conn.close()

    return {
        "coustomers": df_customers,
        "products": df_products,
        "orders": df_orders,
        "order_itmes": df_order_times
    }