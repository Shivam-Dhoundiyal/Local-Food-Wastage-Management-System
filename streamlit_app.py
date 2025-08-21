import streamlit as st
import mysql.connector
import pandas as pd

# -------------------------
# 1. Database Connection
# -------------------------
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",       # 🔹 yaha apne MySQL ka host likhna (local ho to "localhost")
        user="root",            # 🔹 apna MySQL username
        password="password",    # 🔹 apna MySQL password
        database="food_db"      # 🔹 apna database name (jo tumne banaya hai)
    )
    return conn


# -------------------------
# 2. Main Streamlit App
# -------------------------
def main():
    st.title("🍽️ Local Food Wastage Management System")

    menu = ["Home", "View Providers", "View Receivers", "Custom Query"]
    choice = st.sidebar.selectbox("Navigation", menu)

    conn = get_connection()
    cursor = conn.cursor()

    if choice == "Home":
        st.subheader("Welcome to Food Wastage Management Dashboard")
        st.write("Use the sidebar to navigate between different features.")

    elif choice == "View Providers":
        st.subheader("📊 Providers Data")
        query = "SELECT * FROM providers;"   # 🔹 yaha apni SQL table ka naam
        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
        st.dataframe(df)

    elif choice == "View Receivers":
        st.subheader("📊 Receivers Data")
        query = "SELECT * FROM receivers;"   # 🔹 yaha apni SQL table ka naam
        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
        st.dataframe(df)

    elif choice == "Custom Query":
        st.subheader("🛠 Run Your Own SQL Query")
        user_query = st.text_area("Enter SQL Query")
        if st.button("Execute"):
            try:
                cursor.execute(user_query)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error: {e}")

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
