import pandas as pd
from extract_data import extract_all_tables
from analyze import (build_full_dataframe, calculate_basic_stats,
revenue_by_category, customer_order_counts, top_5_customers,
monthly_revenue, average_order_value,sales_by_city,
order_status_percentage, top_5_products
)

# --- Helper functions for formatting ---
def print_header(title):
    print("\n" + "=" * 60)
    print(f"{title.center(56)}")
    print("=" * 60)

def print_section(title):
    print(f"\n {title}")
    print("-" * 60)

def geneerate_report(df):
    """generate and print the final analysis report """
    print_header("WEEK 5 DATA ANALYSIS REPORT")

    #1 Basic Statistcs
    print_section('1. BASIC STATISTICS')
    stats = calculate_basic_stats(df)
    print(f" Total Revenue: ${stats['total_revenue']:,.2f}")
    print(f" Mean: {stats['mean']:,.2f}")
    print(f" Standerd Deviation: ${stats['std']:,.2f}")
    print(f" Median: ${stats['median']:,.2f}")
    print(f" Max Revenue (Single line): ${stats['max']:,.2f}")

    # 2. Revenue by Category
    print_section("2. REVENUE BY CATEGORY")
    rev_cat = revenue_by_category(df)
    for category, total in rev_cat.items():
        print(f" {category}: ${total:,.2f}")

    # 3. Top 5 Products
    print_section("TOP 5 PRODUCTS BY REVENUE")
    top_prod = top_5_products(df)
    for i ,(name, total) in enumerate(top_prod.items(), 1):
        print(f" {i}. {name}: ${total:,.2f}")

    # 4. Customer order Counts (top 5 only for brevity)
    print_section("4. CUSTOMER ORDER COUNTS (TOP 5 )")
    cust_order = customer_order_counts(df)
    for name ,count in cust_order.items():
        print(f" {name}: {count} orders")

    # 5. Top 5 customers
    print_section("TOP 5 CUSTOMERS BY REVENUE")
    top_cust = top_5_customers(df)
    for (name, city), total in top_cust.items():
        print(f" {name} ({city}): ${total:,.2f}")

    # 6. Menthly Revenue
    print_section("6. MENTHLY REVENUE")
    month_rev = monthly_revenue(df)
    for month, total in month_rev.items():
        print(f" {month}: ${total:,.2f}")

    # 7. Average Order Value
    print_section("AVERAGE ORDER VALUE")
    avrage = average_order_value(df)
    print(f"AOV: ${avrage:,.2f}")

    # 8. Sales by City
    print_section("8. SALES BY CITY")
    sales = sales_by_city(df)
    for city, total in sales.items():
        print(f" {city}: ${total:,.2f}")

    # 9. Order Status Percentage
    print_section("9. ORDER STATUS PRECEBTAGE")
    prec = order_status_percentage(df)
    for status, pct in prec.items():
        print(f" {status}: {pct:,.2f}%")

    print_header("END OF REPORT")

def main():
    """ Connecting to the database
    and  Retrieve all tables and convert them to DataFrames return them as dictionaries"""
    dict_data = extract_all_tables()
    # Combine the dataframes into a single table and add the revenue
    df = build_full_dataframe(dict_data)
    # Generate the report 
    geneerate_report(df)

if __name__ == "__main__":
    main()