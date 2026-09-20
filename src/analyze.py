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
                        on="customer_id",suffixes=("_o","_c"))
    
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

if __name__ == "__main__":
    data = extract_all_tables()
    df = build_full_dataframe(data)
    dict_stat = calculate_basic_stats(df)

    for key, value in dict_stat.items():
        print(f"{key} : {value}")


