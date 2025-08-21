# Local-Food-Wastage-Management-System
A Python and Streamlit application to manage and reduce local food waste by connecting donors with receivers.  A data-driven web app using Streamlit and SQL to tackle food insecurity by redistributing surplus food.  A platform connecting food providers with those in need to fight food waste in the community. Built with Python.
📑 Table of Contents

📌 Project Overview

📂 Dataset Description

🎯 Objectives

🛠 Technologies Used

⚙️ Project Steps

📁 Repository Structure

📌 Project Overview

The Local Food Wastage Management System is designed to tackle the growing issue of food wastage by connecting surplus food providers (restaurants, stores, etc.) with receivers (NGOs, individuals, organizations).

The system integrates:

MySQL for structured data storage and queries.

Python & Pandas for data analysis and preprocessing.

Streamlit for an interactive web dashboard that displays insights, trends, and filtering options.

This project not only reduces food waste but also contributes to social good by making food more accessible to those in need.

📂 Dataset Description

The system uses four key datasets:

1. Providers

Details of food donors (restaurants, supermarkets, grocery stores).

provider_id – Unique ID

name – Provider’s name

type – Category (Restaurant, Grocery, etc.)

contact – Contact number

address, city – Location details

2. Receivers

Details of NGOs, organizations, or individuals receiving food.

receiver_id – Unique ID

name – Receiver’s name

contact – Contact number

address, city – Location details

3. Food Listings

Details of food available for donation.

food_id, food_name, quantity, expiry_date

provider_id, provider_type

location, food_type, meal_type

4. Claims

Tracks claims made by receivers.

claim_id, food_id, receiver_id

status (Pending, Completed, Cancelled)

timestamp (date & time of claim)

🎯 Objectives

Provide an end-to-end system for tracking, analyzing, and visualizing food donations.

Enable filtering by city, provider, food type, and meal type.

Display contact details of providers/receivers for coordination.

Generate insights using 15+ SQL queries to identify trends in food donations and claims.

🛠 Technologies Used

Python — Programming & data handling

MySQL — Relational database management

Pandas — Data cleaning and analysis

Streamlit — Interactive dashboard development

GitHub — Version control & project sharing

⚙️ Project Steps

Database Setup

Created MySQL database food_wastage_mgmt_db with four tables.

Loaded data from CSV datasets.

SQL Analysis

Developed 15 queries in Analysis.sql to study providers, receivers, and claims.

Data Handling

Added scripts in Handle Data.sql for cleaning, updating, and validating records.

Dashboard Development

Built a Streamlit app (app.py) that:

Connects to the database.

Runs SQL queries dynamically.

Provides interactive filters and visualizations.

Deployment

Deployed on Streamlit Cloud for public access.

📁 Repository Structure
File / Folder	Description
📄 app.py	Streamlit application (main dashboard)
📄 Analysis.sql	Contains 15+ SQL queries for analysis
📄 Handle Data.sql	SQL scripts for cleaning, updating, and validating data
📦 requirements.txt	Python dependencies list
📝 README.md	Project documentation
📂 Data/	Folder containing CSV datasets (providers, receivers, listings, claims)
🚫 .gitignore	Files/folders excluded from version control

🔗 Live App: Streamlit App Link

📂 GitHub Repo: GitHub Repository Link
