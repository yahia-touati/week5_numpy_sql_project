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

def monthly_revenue(df):
    #Step 1: Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])
    #Step 2: Create new column with only the month
    df["month"] = df["order_date"].dt.to_period("M")
    # Step 3: Group by month and sum revenue
    month_revenue = df.groupby("month")["revenue"].sum()
    return month_revenue

def average_order_value(df):
    """ Average order value (AOV) """
    averge_order = round(df.groupby("order_id")["revenue"].sum().mean(),2)
    return averge_order

def sales_by_city(df):
    sales_city = df.groupby("city")["revenue"].sum().sort_values(ascending=False)
    return sales_city

def order_status_percentage(df):
    """Percentage of order by status."""
    # step 1: Get unique orders only (remove duplicates)
    unique_orders = df.drop_duplicates(subset="order_id")
    # Step 2: count each status
    counts = unique_orders["status"].value_counts()
    # Setp 3: Calculate percentage
    percentage = (counts / counts.sum()) * 100
    
    return round(percentage, 2)


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
    print(monthly_revenue(df))
    print(average_order_value(df))
    print(sales_by_city(df))
    print(order_status_percentage(df))

