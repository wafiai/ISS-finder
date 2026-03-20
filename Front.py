from Backendiss import apifetch,reversen_nominatim
import streamlit as st
import pandas as pd


(position, time) = apifetch()
lat, long = position
coordinates = lat, long

(location) = reversen_nominatim()

data = {
    'LAT': lat,
    'LON': long
}

df = pd.DataFrame([data])




st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=1172&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.header("ISS TRACKER")
st.title("Welcome!")
if st.button("Click me!"):
    st.header(f"The current location is {location}")
    st.map(df)



