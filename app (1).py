import streamlit as st
import pickle
import pandas as pd

@st.cache_resource
def load_model():
    with open("flight_price_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

st.title("✈️ Flight Price Prediction App")
st.write("Predict flight ticket prices based on input details.")

st.markdown("---")

airline = st.selectbox("Airline", [
    'Air_India', 'Indigo', 'Vistara', 'AirAsia', 'SpiceJet', 'GO_FIRST'
])

source_city = st.selectbox("Source City", [
    'Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Kolkata', 'Chennai'
])

destination_city = st.selectbox("Destination City", [
    'Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Kolkata', 'Chennai'
])

departure_time = st.selectbox("Departure Time", [
    'Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'
])

arrival_time = st.selectbox("Arrival Time", [
    'Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'
])

stops = st.selectbox("Number of Stops", ['zero', 'one', 'two'])

travel_class = st.selectbox("Class", ['Economy', 'Business'])

duration = st.number_input("Flight Duration (in minutes)", min_value=30, max_value=2000, value=120)

days_left = st.number_input("Days Left Before Journey", min_value=0, max_value=120, value=20)


input_data = pd.DataFrame({
    'airline': [airline],
    'source_city': [source_city],
    'destination_city': [destination_city],
    'departure_time': [departure_time],
    'arrival_time': [arrival_time],
    'stops': [stops],
    'class': [travel_class],
    'duration': [duration],
    'days_left': [days_left]
})


if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🎉 Estimated Flight Price: **₹ {int(prediction)}**")
    except Exception as e:
        st.error("Error in prediction. Check your inputs or model.")
        st.write(e)
