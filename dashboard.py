import streamlit as st
import pandas as pd

st.title("Leads")
st.write("Please select your desired options:")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(
            "Lead database CSV.csv",
            engine="python",
            encoding="utf-8",
        )
        return df
    except Exception as e:
        st.error("Could not load CSV file.")
        st.write(e)
        st.stop()

df = load_data()

col1, col2 = st.columns(2)
with col1:
    sector = st.selectbox("Sector", ["All", "Real Estate", "Tech", "Other"])
with col2:
    profession = st.selectbox("Profession", ["All", "Angel Investor", "Family Office", "Investor"])

has_linkedin = st.checkbox("Has LinkedIn")
interacted = st.checkbox("Has interacted with relevant content previously")
has_contact = st.checkbox("Has personal email or phone number")

private_group = st.checkbox("Member of Company or Private Group?")
comp_size = st.selectbox("If yes, please select a size", ["All", "2-10", "11-50", "50-200"])

col5, col6 = st.columns(2)
with col5:
    green_list = st.checkbox("Green list")
with col6:
    all_list = st.checkbox("All")

st.write("Columns in CSV:")
st.write(df.columns)
st.write("First rows:")
st.write(df.head())
