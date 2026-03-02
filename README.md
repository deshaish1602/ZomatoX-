 #  Zomato Data Analysis Using Python

##  Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a Zomato restaurant dataset to uncover insights about customer ordering behavior, restaurant types, ratings, spending patterns, and online vs offline trends.

The goal of this project is to analyze restaurant data and generate meaningful business insights using Python and data visualization techniques.

---

##  Dataset Description

The dataset contains restaurant-level information including:

- `name` – Restaurant name  
- `online_order` – Online ordering availability (Yes/No)  
- `book_table` – Table booking availability  
- `rate` – Restaurant rating (out of 5)  
- `votes` – Number of customer votes  
- `approx_cost(for two people)` – Average cost for two people  
- `listed_in(type)` – Type of restaurant (Dining, Cafes, Buffet, etc.)

---

##  Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook / VS Code  

---

##  Project Workflow

### 1. Data Loading
- Imported dataset using `pandas.read_csv()`
- Displayed initial rows using `.head()`
- Checked dataset structure using `.info()`

### 2. Data Cleaning
- Converted `rate` column from string format (e.g., `4.1/5`) to float
- Removed denominator from rating values
- Ensured correct data types for analysis

### 3. Exploratory Data Analysis (EDA)

The following business questions were analyzed:

---

###  Q1: What type of restaurant do the majority of customers order from?

- Used `countplot`
- Found that **Dining restaurants dominate the dataset**

---

###  Q2: How many votes has each type of restaurant received?

- Used `groupby()` and `sum()`
- Dining restaurants received the highest number of votes

---

###  Q3: What ratings do the majority of restaurants receive?

- Plotted histogram
- Majority ratings fall between **3.5 to 4.0**

---

###  Q4: What is the average spending of couples?

- Analyzed `approx_cost(for two people)`
- Most couples prefer restaurants costing around **₹300**

---

###  Q5: Which mode (online or offline) has received maximum rating?

- Used `boxplot` comparison
- Online orders received higher average ratings compared to offline

---

### Q6: Which type of restaurant received more offline orders?

- Created pivot table
- Generated heatmap
- Dining restaurants receive more offline orders

---

##  Visualizations Included

- Count Plot  
- Line Plot  
- Histogram  
- Box Plot  
- Heatmap  

These visualizations help in understanding customer behavior trends and restaurant performance.

---

##  How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zomato-data-analysis.git
```
### 2. Install Required Libraries
```bash
pip install pandas numpy matplotlib seaborn
```
### 3. Run the Script
```bash
python zomato_analysis.py
```
Or open the notebook file and run all cells.

## Project Structure:

Zomato_Data_Analysis/
│
├── zomato_analysis.py
├── Zomato data .csv
└── README.md
### Key Insights
Dining restaurants are the most common category.
Most restaurants have ratings between 3.5 and 4.0.
Online orders tend to receive higher ratings.
Couples prefer moderately priced restaurants.
Offline orders are more common in dining category.
### Learning Outcomes
Through this project, I gained hands-on experience in:
Data Cleaning
Exploratory Data Analysis
Data Visualization
Business Insight Generation
Working with real-world datasets





