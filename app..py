# --- FILTER SECTION (real Streamlit widgets) ---
import streamlit as st

# Styling
st.markdown("""
<style>
.big-selectbox > div > div {
    padding: 14px 18px;
    font-size: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.subheader("🎯 Filter Your Vacation")
st.write("Choose what matters most to you — hover or click to expand each section and select your preferences!")

# Hotel Features
with st.expander("🏨 Hotel Features", expanded=False):
    wifi = st.checkbox("Free WiFi")
    breakfast = st.checkbox("Breakfast Included")
    pool = st.checkbox("Pool")
    waterpark = st.checkbox("Waterpark")
    pet_friendly = st.checkbox("Pet Friendly")

# Location Type
with st.expander("🗺️ Location Type", expanded=False):
    beach = st.checkbox("Near Beach")
    city = st.checkbox("Near City Center")
    mountain = st.checkbox("Mountain View")
    countryside = st.checkbox("Countryside")

# Price Range
with st.expander("💰 Price Range", expanded=False):
    budget = st.checkbox("Budget")
    midrange = st.checkbox("Mid-range")
    luxury = st.checkbox("Luxury")

st.write("---")
