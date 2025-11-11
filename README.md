<!-- Badges -->
<p align="center">
  <a href="https://cameronjoejones-streamlit-sales-dashboard-app-3pmk71.streamlit.app/">
    <img src="https://img.shields.io/badge/Open%20in%20Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit App"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/>
</p>

<h1 align="center">💹 Sales Dashboard</h1>
<p align="center">
  <i>Interactive Sales Analytics Dashboard built with Streamlit, Plotly, and Pandas 💼</i>
</p>

---

## 🧭 Overview  

The **Sales Dashboard** lets you filter and explore a real-world sales dataset using a sleek interactive interface.  
It helps visualize **key performance metrics**, **top customers**, **sales trends**, and more — all in real time.  

<p align="center">
  <img src="screenshots/dashboardpowerbi.png" width="750">
</p>

---

## 🧰 Prerequisites  

Before running the dashboard, ensure you have the following installed:  

- 🐍 **Python 3.11+**
- 📦 **Streamlit**
- 📊 **Plotly**
- 🧮 **Pandas**

---

## ⚙️ How to Use  

1. 📂 Place `sales_data_sample.csv` inside the `data` folder.  
2. ▶️ Run this command in your terminal:

   ```bash
   streamlit run app.py

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

🔑 Default Credentials

After initializing the database (init_db.py), log in using:

👑 admin / admin123

👤 user / user123

☁️ Deployment

You can host this dashboard for free using Streamlit Community Cloud:

🔗 Connect your GitHub repository.

🧩 Set main file path → app.py.

🐍 Set Python version → 3.11.

📂 Ensure data/sales_data_sample.csv exists in your repo.

🏆 Acknowledgements

Built with ❤️ using Streamlit, Plotly, and Pandas

Developed by Ramanpreet Singh & Priyansh Thakur (Thakur Sahab 👑)

Inspired by modern data analytics and real-time BI dashboards

📜 License

This project is licensed under the MIT License.
Feel free to fork, modify, and use it for educational purposes.

<p align="center"> <img src="https://img.shields.io/badge/Made%20with%20❤️-in%20Python-blue?style=for-the-badge&logo=python&logoColor=white"> </p> ```
💎 Highlights:

Fully colored emoji sections 🎨

Badges for Streamlit, Python, and License

Centered banner image and screenshots

Professional sectioning with dividers and icons

Looks perfect in GitHub’s dark/light themes
