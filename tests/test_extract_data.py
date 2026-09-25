import pandas as pd
from extract_data import extract_all_tables

def test_extract_returns_dict():
    """Test that extract_all_tables returns a dictionary."""
    dict_test = extract_all_tables()
    assert isinstance(dict_test, dict)

def test_extract_has_four_tables():
    data = extract_all_tables()
    assert len(data) == 4

def test_extract_has_correct_keys():
    data = extract_all_tables()
    expected_keys = {"customers", "products", "orders", "order_items"}
    assert set(data.keys()) == expected_keys

def test_extract_tables_are_dataframes():
    data = extract_all_tables()
    for name, df in data.items():
        assert isinstance(df, pd.DataFrame), f"{name} is not a DataFrame"
        assert not df.empty, f("{name} is empty")