[![Open in Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)](https://cameronjoejones-streamlit-sales-dashboard-app-3pmk71.streamlit.app/)

# Sales Dashboard

This is a Sales Dashboard built using Streamlit, a popular Python library for building interactive web applications. The dashboard allows you to filter and explore a sales dataset, and visualize key performance metrics, sales by product line over time, and top 10 customers, products, and total sales by product line.

## Prerequisites

To run this dashboard, you need to have Python 3.6 or later installed on your computer, as well as the following libraries:

- Streamlit
- Pandas
- Plotly Express



## How to use

1. Download the `sales_data_sample.csv` file and put it in the `data` folder.
2. Run the script in your terminal or command prompt: `streamlit run app.py`
3. The dashboard will open in your web browser. You can use the filters on the sidebar to explore the dataset and visualize the metrics and charts.

## Features

### Filters

The sidebar of the dashboard includes four filters that allow you to filter the dataset:

- Date range filter: choose a start and end date to filter by the order date.
- Product line filter: select one or more product lines to filter by.
- Country filter: select one or more countries to filter by.
- Order status filter: select one or more order statuses to filter by.

### KPI Metrics

The dashboard displays four key performance indicators (KPIs) for the filtered dataset:

- Total sales
- Total orders
- Average sales per order
- Unique customers

The KPIs are displayed in a metric format with the current value and percentage change from the previous value.

### Sales by Product Line Over Time

This chart displays the total sales by product line over time. You can hover over the chart to see the details for a specific date and product line.

### Top 10 Customers, Products, and Total Sales by Product Line

 These tables display the top 10 customers, products, and total sales by product line for the filtered dataset.


---

## Requirements

- Python 3.11
- streamlit
- pandas
- plotly

You can use either Pipenv (Pipfile provided) or plain pip/venv.

## Installation

- Using Pipenv

  ```bash
  pip install --user pipenv
  pipenv install
  pipenv run python init_db.py
  pipenv run streamlit run app.py
  ```

- Using pip + venv

  ```bash
  python -m venv .venv
  .venv\Scripts\activate  # Windows
  pip install streamlit pandas plotly
  python init_db.py
  streamlit run app.py
  ```

## Usage

- Dataset: ensure `data/sales_data_sample.csv` exists (already included in this repo).
- Initialize the local SQLite database (creates `data/users.db` and seeds users):

  ```bash
  python init_db.py
  ```

- Launch the dashboard:

  ```bash
  streamlit run app.py
  ```

- Default login credentials (created by `init_db.py`):
  - admin / admin123
  - user / user123

## Features Overview

- Authenticated access with username/password stored in SQLite (`data/users.db`).
- KPI metrics: Total Sales, Total Orders, Average Sales per Order, Unique Customers.
- Interactive filters: Date range, Product Line, Country, Order Status.
- Visuals with Plotly: Area chart over time, Top Customers/Products tables, Sales by Product Line summary.

## Project Structure

```text
streamlit-sales-dashboard/
├─ app.py                  # Main Streamlit app (dashboard)
├─ login.py                # Login and signup logic (SQLite-backed)
├─ init_db.py              # Initializes users table and seed users
├─ data/
│  ├─ sales_data_sample.csv
│  └─ users.db
├─ assets/
│  └─ screenshots/
│     └─ .gitkeep
├─ Pipfile
├─ Pipfile.lock
└─ README.md
```

## Screenshots

Add screenshots to `assets/screenshots/` with these filenames and they will render below.

- Overview

  ![Dashboard Overview](screenshots/dashboardpowerbi)

- Filters and KPIs

  ![Filters and KPIs](screenshots/filterandKPI)

- Login Page

  ![Login Page](screenshots/login)

- Top Tables and Sales by Product Line

  ![Tables and Sales by Product Line](screenshots/Tables)

## Deployment

- Streamlit Community Cloud
  - Connect this GitHub repo.
  - App file: `app.py`
  - Python: 3.11
  - Ensure `data/sales_data_sample.csv` is present in the repo or configure external data source.

## Acknowledgements

- Built with Streamlit, Plotly, and Pandas.
- Dashboard by Ramanpreet Singh and Priyansh Thakur.

## License

This project is provided as-is for educational purposes.
