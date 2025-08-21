# ​ Local Food Wastage Management System  

[![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)](https://www.mysql.com/)  
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)  
![Made with VS Code](https://img.shields.io/badge/Made%20with-VS%20Code-blue?logo=visualstudiocode)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  

---

## ​ Table of Contents

- 📌 [Project Overview](#-project-overview)  
- 📂 [Dataset Description](#-dataset-description)  
- 🎯 [Objectives](#-objectives)  
- 🛠 [Technologies Used](#-technologies-used)  
- ⚙️ [Project Steps](#-project-steps)  
- 📁 [Repository Structure](#-repository-structure)  

---

## ​ Project Overview

The **Local Food Wastage Management System** aims to reduce food wastage by connecting surplus food providers with NGOs, organizations, and individuals in need.

- Uses **MySQL** for structured data storage and queries.  
- **Python & Pandas** for data preprocessing and analysis.  
- **Streamlit** to build an interactive dashboard with filters and CRUD operations.  
- Provides insights using **15+ SQL queries** on donations and claims.  

---

## ​ Dataset Description

The system works with four key datasets:

### **1. Providers**  
Food donors such as restaurants, grocery stores, and supermarkets.  
- `provider_id` – Unique ID  
- `name` – Provider name  
- `type` – Category (Restaurant, Grocery, etc.)  
- `contact` – Contact number  
- `address`, `city` – Location details  

### **2. Receivers**  
Details of NGOs, organizations, or individuals receiving food.  
- `receiver_id` – Unique ID  
- `name` – Receiver name  
- `contact` – Contact number  
- `address`, `city` – Location details  

### **3. Food Listings**  
Information about available food items.  
- `food_id`, `food_name`, `quantity`, `expiry_date`  
- `provider_id`, `provider_type`  
- `location`, `food_type`, `meal_type`  

### **4. Claims**  
Tracks claims made by receivers.  
- `claim_id`, `food_id`, `receiver_id`  
- `status` (Pending, Completed, Cancelled)  
- `timestamp` (date & time)  

---

## ​ Objectives

- Build an end-to-end system to **track, analyze, and visualize** food donations.  
- Enable **filters** by city, provider, food type, and meal type.  
- Provide **contact details** of providers/receivers for coordination.  
- Generate insights using **SQL queries** to study donation and claim trends.  

---

## ​ Technologies Used

- **Python** – Data handling & integration  
- **MySQL** – Database management & queries  
- **Pandas** – Data cleaning and analysis  
- **Streamlit** – Dashboard development  
- **GitHub** – Version control & sharing  

---

## ​​ Project Steps

1. **Database Setup** → Created MySQL database with 4 tables.  
2. **Data Loading** → Imported CSV datasets.  
3. **SQL Analysis** → Wrote 15+ queries in `Analysis.sql`.  
4. **Data Handling** → Scripts in `Handle Data.sql` for cleaning & validation.  
5. **Streamlit Dashboard** → Built in `app.py` with filters & CRUD.  
6. **Deployment** → Hosted on **Streamlit Cloud**.  

---

## ​ Repository Structure

| File / Folder        | Description                                              |
|----------------------|----------------------------------------------------------|
| 📄 `app.py`          | Streamlit application (main dashboard)                   |
| 📄 `Analysis.sql`    | Contains 15+ SQL queries for analysis                    |
| 📄 `Handle Data.sql` | SQL scripts for cleaning & updating records              |
| 📦 `requirements.txt`| Python dependencies                                     |
| 📝 `README.md`       | Project documentation (this file)                        |
| 📂 `Data/`           | CSV datasets (providers, receivers, listings, claims)    |
| 🚫 `.gitignore`      | Files/folders ignored in Git                            |

---

🔗 **Live App:** *(Insert your live Streamlit app link here if any)*  
📂 **GitHub Repo:** [Shivam-Dhoundiyal/Local-Food-Wastage-Management-System](https://github.com/Shivam-Dhoundiyal/Local-Food-Wastage-Management-System)

---

