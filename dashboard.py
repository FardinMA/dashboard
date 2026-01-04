import streamlit as st
import pandas as pd

# Title
st.title("Leads")
st.write("Please select your desired options:")

# Load CSV
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(
            "Lead database CSV.csv",
            engine="python",
            encoding="utf-8",
        )
        return df
    except FileNotFoundError:
        df = pd.DataFrame()
    return df

df = load_data()

col1, col2= st.columns(2)
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
if sector != "All":
    filtered = filtered[filtered["sector"] == sector]

if profession != "All":
    filtered = filtered[filtered["profession"] == profession]

if private_group:
    filtered = filtered[filtered["private_group"] == True]

if comp_size != "All":
    filtered = filtered[filtered["company_size"] == comp_size]

if has_linkedin:
    filtered = filtered[filtered["has_linkedin"] == True]
if interacted:
    filtered = filtered[filtered["has_interacted"] == True]
if has_contact:
    filtered = filtered[filtered["has_contact"] == True]

if green_list_check:
    filtered = filtered[filtered["green_list"] == True]

if all_check:
    filtered = df.copy()


st.subheader("Filtered Data")
st.dataframe(filtered, use_container_width=True)

csv_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Lead List",
    data=csv_data,
    file_name="lead_list.csv",
    mime="text/csv"
)

st.write(df.head())
st.write(df.columns)

