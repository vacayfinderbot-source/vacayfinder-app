import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Streamlit page
st.set_page_config(page_title="VacayFinder", page_icon="🌴", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox("Navigate", ["🏠 Home", "🔍 Find My Vacation", "ℹ️ About"])

# --------------------------- HOME PAGE ---------------------------
if page == "🏠 Home":
    st.title("🌴 Welcome to VacayFinder!")
    st.markdown("""
    ### Plan Your Perfect Getaway
    Use filters to find the **best hotels and destinations** that match your dream vacation.  
    Whether you’re after a **beach resort**, a **mountain retreat**, or a **city adventure**,  
    VacayFinder makes your search simple and fun!

    👉 Head to **“Find My Vacation”** to get started.
    """)
    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", use_container_width=True)

# --------------------------- FIND MY VACATION ---------------------------
elif page == "🔍 Find My Vacation":
    st.title("🏖️ Find Your Perfect Vacation Destination")

    destination = st.text_input("Where do you want to go?", placeholder="e.g. Amarillo, Texas")

    st.markdown("### 🎛️ Vacation Filters")

    with st.expander("🏨 Hotel Preferences", expanded=False):
        pool = st.checkbox("Swimming Pool")
        breakfast = st.checkbox("Free Breakfast")
        parking = st.checkbox("Free Parking")
        pet_friendly = st.checkbox("Pet Friendly")
        gym = st.checkbox("Fitness Center / Gym")
        spa = st.checkbox("Spa / Wellness")
        waterpark = st.checkbox("Waterpark")

    with st.expander("🛎️ Room Features", expanded=False):
        wifi = st.checkbox("Free Wi-Fi")
        ac = st.checkbox("Air Conditioning")
        tv = st.checkbox("Smart TV")
        balcony = st.checkbox("Balcony View")
        kitchen = st.checkbox("Kitchen / Kitchenette")

    with st.expander("🎯 Additional Services", expanded=False):
        airport = st.checkbox("Airport Shuttle")
        restaurant = st.checkbox("On-site Restaurant")
        kids_friendly = st.checkbox("Kid Friendly")
        beach_access = st.checkbox("Beach Access")
        mountain_view = st.checkbox("Mountain View")

    filters = []
    for label, val in {
        "pool": pool,
        "breakfast": breakfast,
        "parking": parking,
        "pet friendly": pet_friendly,
        "gym": gym,
        "spa": spa,
        "waterpark": waterpark,
        "wifi": wifi,
        "ac": ac,
        "tv": tv,
        "balcony": balcony,
        "kitchen": kitchen,
        "airport shuttle": airport,
        "restaurant": restaurant,
        "kids friendly": kids_friendly,
        "beach access": beach_access,
        "mountain view": mountain_view
    }.items():
        if val:
            filters.append(label)

    if st.button("🔍 Search Hotels"):
        if not destination:
            st.warning("Please enter a destination first.")
        else:
            with st.spinner("Finding the best hotels for you..."):
                def get_hotels(destination, filters):
                    """Fetch hotels from Google Places API based on destination and filters."""
                    query = f"hotels in {destination}"
                    if filters:
                        query += " with " + ", ".join(filters)

                    url = "https://places.googleapis.com/v1/places:searchText"
                    payload = {
                        "textQuery": query,
                        "languageCode": "en",
                        "maxResultCount": 10
                    }
                    headers = {
                        "Content-Type": "application/json",
                        "X-Goog-Api-Key": API_KEY,
                        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.rating,places.websiteUri,places.location"
                    }

                    response = requests.post(url, headers=headers, json=payload)
                    if response.status_code != 200:
                        return []
                    data = response.json()
                    if "places" not in data:
                        return []
                    return data["places"]

                hotels = get_hotels(destination, filters)

                if hotels:
                    st.success(f"Found {len(hotels)} hotels near {destination} 🌍")
                    for hotel in hotels:
                        st.markdown(f"### 🏨 {hotel['displayName']['text']}")
                        if "formattedAddress" in hotel:
                            st.write(f"📍 Address: {hotel['formattedAddress']}")
                        if "rating" in hotel:
                            st.write(f"⭐ Rating: {hotel['rating']}")
                        if "websiteUri" in hotel:
                            st.write(f"🔗 [Visit Website]({hotel['websiteUri']})")
                        if "location" in hotel:
                            lat = hotel['location']['latitude']
                            lng = hotel['location']['longitude']
                            maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
                            st.write(f"🗺️ [View on Google Maps]({maps_url})")
                        st.markdown("---")
                else:
                    st.warning("No hotels found that match your filters. Some or all of these features might not be available here.")

# --------------------------- ABOUT PAGE ---------------------------
elif page == "ℹ️ About":
    st.title("👦 About VacayFinder")
    st.markdown("""
    Hi! I’m **Daksh Dave**, a 13-year-old who created VacayFinder.  
    I came up with this idea after going on a vacation to **Amarillo, Texas**,  
    and realizing how much easier it could be to find the *perfect* hotel that matches exactly what you want.  

    My awesome parents — **Parul Mehta** and **Utkarsh Dave** — encouraged me to bring this idea to life.  
    VacayFinder is built with **Python** and **Streamlit**, using real Google data to make vacation planning effortless.  

    ✨ Thanks for checking it out, and I hope it helps you plan your next amazing trip!
    """)
