import pandas as pd
import numpy as np
from extract_data import extract_all_tables

def build_full_dataframe(data):
    """
    Merge all DataFrames into one master DataFrames.
    Args:
        data (dict): Dictionary of DataFrames from extract_data.
    Returns:
        pd.DataFrames: Merged DataFrames with all information.
    """
    df_customers = data["customers"]
    df_products = data["products"]
    df_orders = data["orders"]
    df_order_items = data["order_items"]

    mearge_df = pd.merge(df_order_items, df_orders,on="order_id",
                            suffixes=("_orders","_order_items"))

    merged_df = pd.merge(mearge_df,df_products,
                        on="product_id",suffixes=("_oi","_p"))

    merged = pd.merge(merged_df,df_customers,
                        on="customer_id",suffixes=("_p","_c"))
    
    merged["revenue"] = merged["price"] * merged["quantity"]

    return merged

def calculate_basic_stats(df):
    revenuse = df["revenue"].to_numpy()
    #Now apply Numpy functions
    total = np.sum(revenuse)
    mean = np.mean(revenuse)
    std = np.std(revenuse)
    median = np.median(revenuse)
    p1 = np.percentile(revenuse, 25)
    p3 = np.percentile(revenuse, 75)
    max = np.max(revenuse)
    min = np.min(revenuse)
    argmax = np.argmax(revenuse)
    return {
        "total_revenue" : total,
        'mean': mean,
        "std": std,
        "median": median,
        "p1": p1,
        "p3": p3,
        "max": max,
        "min": min,
        "argmax": argmax
    }
def revenue_by_category(df):
    result = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    return result

def top_5_products(df):
    top_5 = df.groupby("name_p")["revenue"].sum().nlargest(5)
    return top_5

def customer_order_counts(df):
    # count unique orders per customer
    order_count = df.groupby("name_c")["order_id"].nunique().sort_values(ascending=False)
    return order_count

def top_5_customers(df):
    """Top 5 customers by total revenue. """
    top_5_customer = df.groupby(["name_c", "city"])["revenue"].sum().nlargest(5)
    return top_5_customer

if __name__ == "__main__":
    data = extract_all_tables()
    df = build_full_dataframe(data)
    dict_stat = calculate_basic_stats(df)

    for key, value in dict_stat.items():
        print(f"{key} : {value}")

    print(df.columns.tolist())
    print(top_5_products(df))
    print(customer_order_counts(df))
    print(top_5_customers(df))


