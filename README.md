# Streamlit Speed Test Web App

Check your Internet speed in under 30 seconds. Speedtest measures the speed between your device and a test server, using your device's internet connection. This web app develop using Streamlit. It is allowed only single-page websites but now they have added a feature for creating multipage web apps. It is easy to learn, built on top of python, and has amazing features for creating web applications.

## Speed Test Script  

```
import speedtest

test = speedtest.Speedtest()
download_byte = int(test.download())
upload_byte = int(test.upload())

download_speedtest = download_byte/1048576
uploaded_speedtest = upload_byte/1048576
```

## Screenshot

![Speed Tester](https://github.com/amogh9594/speedtest/blob/main/speedtest.png)
