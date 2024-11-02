# TechCrunch Scraping

## Project Name

Scraping TechCrunch website categories and articles and creating a small API.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  
## Overview

This project provides a complete solution for scraping, storing, and visualizing article data from TechCrunch, a leading technology news website. It is designed to retrieve articles based on their categories (such as crypto, apps, etc.) and store them in a selected database for further analysis and visualization. The project also includes a dashboard prototype for data visualization and an API to facilitate access to the stored data.

## Features

- **Dynamic Scraping**: 
  The project includes a scraping tool capable of retrieving articles from various TechCrunch categories.
- **Data Storage**: 
  The retrieved articles are used to create two SQL insertion files for categories and articles, which should be executed afterward to insert them into the database (categories -> articles).
- **Interactive Dashboard**: 
  A dashboard is provided to visualize and analyze article data.
- **API**: 
  The project includes an API for viewing data in the database.
- **Detailed Documentation**: 
  The project comes with complete documentation, making it easy to set up and use.


## Prerequisites

- selenium (version 4.15.2 or higher)
- streamlit (version 1.30.0 or higher)
- seaborn (version 0.13.1 or higher)
- pandas (version 0.3.1 or higher)
- cx_Oracle (version 8.3.0 or higher)
- matplotlib (version 3.8.2 or higher)
- google chrome (version 114.0.5735.90 or lower)
- Oracle Database (CMD or IDE); sqldeveloper was used here
- Python (version 3.10.4 or higher)
- (optional) Jupyter Notebook to read the .ipynb file 

## Installation

To install and set up this project locally, follow the steps below:

1. **Clone the Repository**:
   - Open a terminal and clone the project repository using:
     ```
     git clone [YOUR_REPOSITORY_URL]
     ```
   - Navigate to the project directory:
     ```
     cd Scrapping_TechCrunch
     ```

2. **Environment Setup**:
   - Ensure that Python is installed on your machine. You can download it from [the official Python website](https://www.python.org/downloads/).
   - It’s recommended to use a virtual environment for managing dependencies. Create a virtual environment by running:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       .\venv\Scripts\activate
       ```
     - On Unix or MacOS:
       ```
       source venv/bin/activate
       ```

3. **Install Dependencies**:
   - Install all necessary dependencies using pip:
     ```
     pip install selenium streamlit seaborn matplotlib pandas cx_Oracle
     ```

4. **Database Configuration**:
   - Make sure Oracle Database is installed and configured on your machine.
   - Create a new database or use an existing one to store scraped data.
   - Update the project’s configuration files to point to your database.

5. **(Optional) Run the Scraper**:
   - Run the scraping script to start fetching data:
     ```
     python Web_Scrapping.py
     ```

6. **Execute Insertion Scripts**:
   Follow these steps:
   - Run the table creation script `table_creation.sql`
   - Run the insertion script for categories `insert_categories.sql`
   - Run the insertion script for articles `insert_articles.sql`

8. **Start the API**:
   - Launch the API to access stored data:
     ```
     streamlit run app.py
     ```

9. **(Optional) Jupyter Notebook**:
   - If you want to use Jupyter Notebook for data visualization or analysis, ensure it’s installed:
     ```
     pip install notebook
     ```
   - Launch Jupyter Notebook:
     ```
     jupyter notebook
     ```

You can now use this project to scrape, store, and visualize TechCrunch article data!
