# Streamlit Speed Test Web App

Check your Internet speed in under 30 seconds. Speedtest measures the speed between your device and a test server, using your device's internet connection. This web app develop using Streamlit. It is allowed only single-page websites but now they have added a feature for creating multipage web apps. It is easy to learn, built on top of python, and has amazing features for creating web applications.

## Speed Test Script  

```
import speedtest
def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

download_speedtest = bytes_to_mb(test.download())
uploaded_speedtest = bytes_to_mb(test.upload())
```
