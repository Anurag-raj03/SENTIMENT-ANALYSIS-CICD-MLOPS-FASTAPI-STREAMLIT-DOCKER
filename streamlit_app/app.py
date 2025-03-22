import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://backend:8000/predict/")

st.title("📝 Sentiment Analysis App")
st.markdown("Enter text to analyze sentiment.")

if "text_input" not in st.session_state:
    st.session_state.text_input = ""

text_input = st.text_area("Enter text:", value=st.session_state.text_input, height=150)

if st.button("Predict Sentiment 🚀"):
    if text_input.strip():
        st.session_state.text_input = text_input  
        try:
            response = requests.post(
                API_URL, 
                json={"text": text_input},
                headers={"Content-Type": "application/json"} 
            )
            if response.status_code == 200:
                result = response.json()
                st.success(f"Sentiment: **{result['sentiment'].upper()}** 🎯")
            else:
                st.error(f"❌ Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ API request failed: {e}")
    else:
        st.warning("⚠️ Please enter text to analyze.")
