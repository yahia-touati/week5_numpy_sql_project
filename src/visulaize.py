import matplotlib.pyplot as plt

def plot_monthly_revenue(df):
    """
    Plot monthly revenue as a line chart.
    Args:
        df(pd.DataFrame): The full merged DataFrame.
    """
    from analyze import monthly_revenue
    monthly = monthly_revenue(df)


    plt.figure(figsize=(10, 5), dpi=100)
    plt.plot(monthly.index.astype(str), monthly.values, marker='o', color='steelblue')

    plt.title("Monthly Revenue", fontsize=14, fontweight='bold')
    plt.xlabel("Monthly")
    plt.ylabel('Revenue ($)')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig('images/monthly_revenue.png')
    plt.close()