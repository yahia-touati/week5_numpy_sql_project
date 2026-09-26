# week5_numpy_sql_project

An end-to-end data analysis pipeline that builds a PostgreSQl database,
extracte data using SQL and pandas, and generates a formatted analytical report.

# Tech Stack
- Python 3.12
- PostgreSQL
- pandas, NumPy
- SQLAlchemy
- pytest

# Project Structure
week5_numpy_sql_project/
├──  sql
│   ├── queries.sql   # 8 analytical SQL querires (Q1-Q7)
│   ├── schema.sql    # Database shema (Tables, constraints)
│   └── seed_data.sql # Sample data for testing 
├──  src
│   ├── analyze.py        # Analysis functions using pandas DataFrames
│   ├── db_connection.py  # SQLAlchemy engine setup
│   ├── extract_data.py   # Load tables into pandas + NUmPy
│   ├── visulaize.py      # Charts with matplotlib (coming soon)
│   └── main.py           # Main entry point (report generator)
├── tests/
│    ├── test_analyze.py       
│    ├── test_db_connecton.py
│    └── test_extract_data.py
├── README.md
├── requirements.txt
├── conftest.py          # Pytest configuration
└──  images
     └── monthly_revenue.png

## Installation 

Follow these steps to set up the project locally:

1. Clone the repostory:
    '''bash
    git clone https://github.com/yahia-touati/week5_numpy_sql_project.git
    cd week5_numpy_sql_project

2. Create and active a virtual environment
    python3.12 -m venv .venv
    source .venv/bin/activate
    (on windows: .venv/Scripts/activate)

3. Install the required dependencies:
    pip install -r requirements.txt

4. Set up the environment variables:
    copy the example file and fill in your 
    PostgreSQl credentials:
    
    cp .env.example .env

5. Set up the database
    psql -h locahost -U dev -d week5_db -f sql/shema.sql
    psql -h locahost -U dev week5_db -f sql/seed_data.sql

6. Run the project

    python3 src/main.py

## Usage

Run the main script to generate the full analysis report:

`bash
python3 src/main.py

The script will:

1. Connect to the PostgreSQL database.
2. Extract all four tables into pandas DataFrames.
3. Merge them into a single master DataFrame.
4. Run all analysis functions (Q1–Q8).
5. Print a formatted report in the console

Simple Output
========================================
   WEEK 5 DATA ANALYSIS REPORT
========================================

📌 1. BASIC STATISTICS
----------------------------------------
  Total Revenue: $43,329.00
  Mean: $294.76
  Standard Deviation: $482.59
  Median: $70.00
  Max Revenue (single line): $2,400.00

📌 2. REVENUE BY CATEGORY
----------------------------------------
  Electronics: $31,365.00
  Furniture: $9,930.00
  Accessories: $825.00
  ...

========================================
   END OF REPORT
======================================== 

## Features

- Database Design: PostgreSQL schema with 4 related tables (customers, products, orders, order_items) and foreign keys.
- Data Extraction: Load all tables into pandas DataFrames using SQLAlchemy.
- Data Analysis: 8 analytical queries (Q1–Q8) covering revenue, top products, top customers, monthly trends, and more.
- NumPy Statistics: Compute mean, median, standard deviation, and percentiles on revenue data.
- Formatted Report: Generate a clean, readable console report with numbered sections.
- Automated Tests: 10 unit tests with pytest covering connection, extraction, and analysis modules.

## Testing

The project includes a test suite built with pytest that validates:

- Database Connection (test_db_connection.py): engine creation and connectivity.
- Data Extraction (test_extract_data.py): correct structure and content of extracted tables.
- Analysis Functions (test_analyze.py): correctness of all Q1–Q8 analytical functions.

### How to Run Tests

`bash
pytest tests/ -v

## Future Improvements

This project is actively being developed. Planned enhancements include:

- [ ] Data Visualization: Add charts (line, bar, pie) using matplotlib.
- [ ] Interactive Dashboard: Build a web interface with Streamlit.
- [ ] Docker Support: Containerize the project for easy deployment.
- [ ] More Analysis: Add customer segmentation and sales forecasting.
- [ ] CI/CD Pipeline: Automate testing with GitHub Actions.

## 👤 Author

Yahia Touati

- GitHub: [@yahia-touati](https://github.com/yahia-touati)
- Email: yahiatouati75@gmail.com

If you found this project useful, please consider giving it a ⭐️!