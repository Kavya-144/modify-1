import streamlit as st
import random
import time

# Simulate sensor data
def get_sensor_data():
    temperature = random.uniform(20, 80)
    vibration = random.uniform(0.2, 2.0)
    return temperature, vibration

# Analyze machine health
def check_health(temp, vib):
    if temp > 70 or vib > 1.5:
        return ("❌ High Risk of Failure!", "red", 
                "🔧 **Shut down** machine immediately. Check cooling system, bearings, and lubrication.")
    elif temp > 50 or vib > 1.0:
        return ("⚠ Maintenance Needed Soon", "orange", 
                "🛠 Schedule inspection. Clean filters and check motor alignment.")
    else:
        return ("✅ Machine Healthy", "green", 
                "👍 All systems normal. No action needed.")

# App layout config
st.set_page_config(page_title="AI Co-Pilot Dashboard", layout="wide")

# Sidebar
st.sidebar.title("AI Co-Pilot Settings")
st.sidebar.write("This dashboard simulates equipment health for maintenance.")

# Title
st.title("🛠️ AI Co-Pilot Dashboard - Machine Health Monitor")
st.markdown("Real-time simulation of temperature and vibration data for predictive maintenance.")

# Button to start
if st.button("🚀 Start Monitoring"):
    for i in range
