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

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_itel2xi4.json")

download_speedtest = bytes_to_mb(test.download())
uploaded_speedtest = bytes_to_mb(test.upload())

st_lottie(lottie_coding, height=300, key="coding")
st.markdown("<h1 style='text-align: center; color: white;'>SPEEDTEST</h1>", unsafe_allow_html=True)
st.markdown("----", unsafe_allow_html=True)

# if st.button("RUN SPEED TEST"):
#     st.text("Downloading Speed : " + str(download_speedtest) + " mbps")
#     st.text("Uploading Speed : " + str(uploaded_speedtest) + " mbps")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("    ")
   
with col2:
   if st.button("RUN SPEED TEST"):
       st.text("Downloading Speed : " + str(download_speedtest) + " mbps")
       st.text("Uploading Speed : " + str(uploaded_speedtest) + " mbps")

with col3:
   st.header("    ")







    