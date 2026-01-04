import streamlit as st
import pandas as pd

# Title
st.title("Leads")

# Load CSV
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Lead database CSV.csv")
    except FileNotFoundError:
        df = pd.DataFrame()
    return df

df = load_data()

col1, col2, col3 = st.columns(2)
with col1:
    sector = st.selectbox("Sector", ["Real Estate", "Tech", "Other"])
with col2:
    profession = st.selectbox("Profession", ["Angel Investor", "Family Office", "Investor"])

has_linkedin = st.checkbox("Has LinkedIn")
interacted = st.checkbox("Has interacted with relevant content previously")
has_contact = st.checkbox("Has personal email or phone number")

col3 = st.columns(1)
with col3:
    private_group = st.checkbox("Member of Private Group?")

col4 = st.columns(1)
with col4:
    comp_size = st.selectbox("If yes, select Company Size", ["2-10", "11-50", "50-200"])

col5, col6 = st.columns(2)
with col5:
    green_list = st.checkbox("Green list")
with col6:
    all_list = st.checkbox("All")

st.download_button(
    label="Generate Lead List",
    file_name="Your Leads.csv",
    mime="text/csv"
)
