import pandas as pd
import numpy as np 
from analyze import (top_5_products, top_5_customers,
order_status_percentage)

def test_top_5_products_return_5_items():
    sample_df = pd.DataFrame({
        "name_p": ["a", "b", "c", "d","e",f""],
        "revenue": [100, 200, 300, 2500,3500,5600]
    })

    result = top_5_products(sample_df)

    assert len(result) == 5

def test_top_5_customers_return_5_items():
    sample_df = pd.DataFrame({
        "name_c": ["a", "b", "c", "d", "e", "f"],
        "city": ["algera", "setif", "ciro", "b", "s", "n"],
        "revenue": [100, 200, 300, 2500,3500,5600]
    })
    result = top_5_customers(sample_df)

    assert len(result) == 5

def test_order_status_percentage_values():
    data_test = pd.DataFrame({ 
            "order_id": [1, 2, 3, 4],
            "status": ["delivered", "delivered", "shipped", "pending"]
            })
    result = order_status_percentage(data_test)

    assert result["delivered"] == 50.0
    assert result["shipped"] == 25.0
    assert result["pending"] == 25.0
    
def test_order_status_percentage_sums_to_100():
    data_test = pd.DataFrame({ 
        "order_id": [1, 2, 3],
        "status": ["delivered", "shipped", "pending"]
        })
    result = order_status_percentage(data_test)
    assert abs(result.sum() - 100) < 0.5