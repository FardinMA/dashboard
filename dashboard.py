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

# First row dropdowns
col1, col2 = st.columns(2)
with col1:
    sector = st.selectbox("Sector", ["Real Estate", "Tech", "Other"])
with col2:
    profession = st.selectbox("Profession", ["Angel Investor", "Family Office", "Investor"])

# Second row
col3, col4 = st.columns(2)
with col3:
    private_group = st.checkbox("Member of Private Group?")
with col4:
    comp_size = st.selectbox("Company Size", ["2-10", "11-50", "50-200"])

# Third row checkboxes
has_linkedin = st.checkbox("Has LinkedIn")
interacted = st.checkbox("Has interacted with relevant content previously")
has_contact = st.checkbox("Has personal email or phone number")

# Fourth row
col5, col6 = st.columns(2)
with col5:
    green_list = st.checkbox("Green list")
with col6:
    all_list = st.checkbox("All")

# Show current selections
st.write("You selected:", sector, profession, private_group, comp_size,
         has_linkedin, interacted, has_contact, green_list, all_list)

st.download_button(
    label="Generate Lead List",
    file_name="Your Leads.csv",
    mime="text/csv"
)
