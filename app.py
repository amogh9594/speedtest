import speedtest
import streamlit as st
import requests
from streamlit_lottie import st_lottie

test = speedtest.Speedtest()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_itel2xi4.json")

download_byte = int(test.download())
upload_byte = int(test.upload())

download_speedtest = download_byte/1048576
uploaded_speedtest = upload_byte/1048576

st_lottie(lottie_coding, height=300, key="coding")
st.markdown("<h1 style='text-align: center; color: white;'>SPEEDTEST</h1>", unsafe_allow_html=True)
st.markdown("----", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.header("    ")
   
with col2:
   if st.button("RUN INTERNET SPEED TEST"):
       st.text("Downloading Speed : " + str(int(download_speedtest)))
       st.text("Uploading Speed : " + str(int(uploaded_speedtest)))

with col3:
   st.header("    ")







    
