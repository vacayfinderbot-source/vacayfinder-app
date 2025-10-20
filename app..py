import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="VacayFinder 🌴", page_icon="🌎", layout="wide")

# --- SIDEBAR NAVIGATION ---
menu = st.sidebar.radio("Navigate", ["🏠 Home", "🔍 Find My Vacation", "ℹ️ About"])

# --- HOME PAGE ---
if menu == "🏠 Home":
    st.title("Welcome to VacayFinder 🌴")
    st.markdown("""
    ### Plan your dream vacation in minutes!
    VacayFinder helps you explore **real hotels** that match your style and comfort.
    
    🌴 Whether you’re looking for **waterparks, spas, luxury, or budget stays**, 
    you’ll find the perfect destination right here.
    """)

    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", caption="Adventure awaits!", use_container_width=True)
    st.write("👉 Go to the **Find My Vacation** tab to start planning!")

# --- FIND MY VACATION PAGE ---
elif menu == "🔍 Find My Vacation":
    st.title("Find My Perfect Vacation 🏖️")

    location = st.text_input("📍 Enter a city or destination (e.g., Amarillo, TX):")

    budget = st.selectbox("💰 Choose your budget", ["$", "$$", "$$$", "$$$$"])
    pool = st.checkbox("🏊 Pool")
    wifi = st.checkbox("📶 Free WiFi")
    breakfast = st.checkbox("🥐 Free Breakfast")
    spa = st.checkbox("💆 Spa")
    waterpark = st.checkbox("🌊 Waterpark")

    st.write("---")

    if st.button("Show Matching Hotels"):
        if location.strip() == "":
            st.warning("Please enter a destination first.")
        else:
            with st.spinner("Searching for hotels..."):
                # --- Travel Advisor API Call ---
                url = "https://travel-advisor.p.rapidapi.com/locations/search"
                querystring = {"query": location, "limit": "10", "offset": "0", "units": "km", "currency": "USD", "sort": "relevance", "lang": "en_US"}

                headers = {
                    "x-rapidapi-key": "b8f9afd504msh3fcda23c3cdad2ep1d8b53jsn349118264ec9",  # 👈 REPLACE THIS with your real key
                    "x-rapidapi-host": "travel-advisor.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers, params=querystring)
                
                if response.status_code == 200:
                    data = response.json()
                    results = data.get("data", [])

                    if results:
                        st.success(f"Found {len(results)} results near {location}:")
                        for item in results:
                            if "result_object" in item and "name" in item["result_object"]:
                                name = item["result_object"]["name"]
                                lat = item["result_object"]["latitude"]
                                lon = item["result_object"]["longitude"]
                                st.write(f"🏨 **{name}**")
                                st.markdown(f"[📍 View on Google Maps](https://www.google.com/maps?q={lat},{lon})")
                                st.write("---")
                    else:
                        st.warning("No hotels found — try a different city.")
                else:
                    st.error("Error connecting to the hotel database. Try again later!")

# --- ABOUT PAGE ---
elif menu == "ℹ️ About":
    st.title("About VacayFinder 💡")
    st.markdown("""
    Hi! I’m **Daksh Dave**, a 13-year-old who built VacayFinder with love 💻✨  
    This idea came from one of my vacation experiences in **Amarillo, Texas**, where I realized how fun — but tricky — it can be to find the *perfect* place to stay.
    
    With a little help from my parents, **Parul Mehta** and **Utkarsh Dave**, I designed this app to make vacation planning simpler, faster, and more fun! 🌴
    
    Thanks for checking it out — and get ready for your next great getaway! 🚀
    """)
