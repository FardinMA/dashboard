import streamlit as st
import pandas as pd

st.set_page_config(page_title="TekhLeads", layout="wide")

st.title("Leads Dashboard")
st.write("Please select your desired options:")

@st.cache_data
def load_data():
    df = pd.read_csv(
        "Lead database CSV.csv",
        engine="python",
        encoding="utf-8"
    )
    return df

df = load_data()

df = df.rename(columns={
    "Has a LinkedIn?": "has_linkedin",
    "Member of Private Investor Group?": "private_group",
    "Interacted with Relevant Content?": "has_interacted",
    "Company Size": "company_size",
    "Sector": "sector",
    "Profession": "profession",
    "Email": "email",
    "Phone Number": "phone",
    "Classification": "classification"
})

col1, col2 = st.columns(2)
with col1:
    sector = st.selectbox("Sector", ["All", "Real Estate", "Tech", "Other"])
with col2:
    profession = st.selectbox("Profession", ["All", "Angel Investor", "Family Office", "Investor"])

has_linkedin = st.checkbox("Has LinkedIn")
interacted = st.checkbox("Has interacted with relevant content previously")
private_group = st.checkbox("Member of Private Investor Group?")

comp_size = st.selectbox("Company Size", ["All", "2-10", "11-50", "51-200", "201-500"])

col3, col4 = st.columns(2)
with col3:
    green_list = st.checkbox("Green list")
with col4:
    all_list = st.checkbox("All")

filtered = df.copy()

if sector != "All":
    filtered = filtered[filtered["sector"] == sector]

if profession != "All":
    filtered = filtered[filtered["profession"] == profession]

if private_group:
    filtered = filtered[
        filtered["private_group"].astype(str).str.lower().isin(["yes", "true", "1"])
    ]

if comp_size != "All":
    filtered = filtered[filtered["company_size"] == comp_size]

if has_linkedin:
    filtered = filtered[
        filtered["has_linkedin"].astype(str).str.lower().isin(["yes", "true", "1"])
    ]

if interacted:
    filtered = filtered[
        filtered["has_interacted"].astype(str).str.lower().isin(["yes", "true", "1"])
    ]

if green_list:
    filtered = filtered[filtered["classification"].str.lower() == "green"]

if all_list:
    filtered = df.copy()

st.subheader("Filtered Leads")
st.dataframe(filtered, use_container_width=True)

csv_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Lead List",
    data=csv_data,
    file_name="Your list.csv",
    mime="text/csv"
)



