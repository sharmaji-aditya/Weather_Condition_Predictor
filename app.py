import streamlit as st
import pandas as pd
import joblib

# Load the model and scaler
model = joblib.load("weather_model.pkl")
# Condition mapping
condition_map = {
    1: 'sunny 🌞 ',
    2: 'drizzle 💦',
    3: 'rain 🌧',
    4: 'snow ❄️',
    5: 'fog 💨'
}

# Streamlit UI
st.title("🌤️ Weather Condition Predictor")
st.write("Enter today's weather data:")

# Input fields
humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.slider("Wind Speed (km/h)", 0, 100, 10)
temp_max = st.number_input("Maximum Temperature (°C)", value=30.0)
temp_min = st.number_input("Minimum Temperature (°C)", value=20.0)

if st.button("Predict Weather Condition"):
    # Prepare and scale data
    input = pd.DataFrame([[humidity, wind_speed, temp_max, temp_min]],
                            columns=['Humidity', 'WindSpeed', 'TempMax', 'TempMin'])

    # Make prediction
    prediction = model.predict(input)
    condition = condition_map.get(prediction[0], "Unknown") # here unknown is written to handle the error when predicted label goes out of bounds 

    # Output
    st.subheader("☁️ Predicted Weather:")
    st.success(f"The predicted weather condition is: **{condition.upper()}**")
 