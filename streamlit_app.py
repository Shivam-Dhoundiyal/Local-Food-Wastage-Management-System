import streamlit as st
import pandas as pd

# Page ka title set karo
st.set_page_config(page_title="Food Wastage Dashboard", layout="wide")

st.title("Local Food Wastage Management System 🍲")

try:
    # Step 1: Database se connect karo (ye automatically .streamlit/secrets.toml se details le lega)
    # 'mysql_db' naam secrets.toml mein section [connections.mysql_db] se match hona chahiye
    conn = st.connection('mysql_db', type='sql')

    # Step 2: Query run karke data fetch karo
    # ttl=600 ka matlab hai ki data 10 minute (600 seconds) tak cache mein rahega
    st.write("Fetching data from the database...")
    providers_df = conn.query('SELECT * FROM providers;', ttl=600)

    # Step 3: Data ko screen par display karo
    st.subheader("List of Food Providers")
    st.dataframe(providers_df)

except Exception as e:
    st.error(f"Database se connect nahi ho pa raha hai. Error: {e}")
    st.info("Please check your secrets.toml file and database firewall settings.")
