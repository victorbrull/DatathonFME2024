import os
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model_file = os.path.join("models", "model.pkl")

if os.path.exists(model_file):
    with open(model_file, "rb") as file:
        model = pickle.load(file)
else:
    st.error(f"Model file {model_file} not found. Please ensure the file is in the correct directory.")
    st.stop()


# Application title
st.title("Real Estate Price Predictor 🏠")

# Application description
st.write("""
Application to predict the price of real estate based on user-provided variables.\n
Please fill in the details below to get a prediction.
""")

# Function to get user input
def get_user_input():

    # Location and Geographical Information
    st.subheader("Location Information 📍")
    with st.expander("Location and Address"):
        Latitude = st.number_input("Latitude", value=41.85)
        Longitude = st.number_input("Longitude", value=-87.65)

    # Property Characteristics
    st.subheader("Property Characteristics 🏡")
    with st.expander("Property Details 🔎"):
        LotSizeSquareFeet = st.number_input("Lot Size (sqft)", value=5000, step=10)
        LivingArea = st.number_input("Living Area (sqft)", value=1500, step=10)
        BedroomsTotal = st.number_input("Total Bedrooms", value=3, step=1)
        BathroomsFull = st.number_input("Full Bathrooms", value=2, step=1)
        YearBuilt = st.number_input("Year Built", value=1980, step=1)

    # Quality and Condition Information
    st.subheader("Quality and Condition Information ✅")
    st.write("From 6 (worst) to 1 (best)")
    with st.expander("Bathroom 🛀"):
        bathroom_quality = st.number_input("Bathroom Condition", value=4.0, step=1.0)
        bathroom_q1q6 = st.number_input("Bathroom Quality", value=4.0, step=1.0)
    
    with st.expander("Exterior 🌼"):
        exterior_quality = st.number_input("Exterior Condition", value=4.0, step=1.0)
        exterior_q1q6 = st.number_input("Exterior Quality", value=4.0, step=1.0)
    
    with st.expander("Interior 🚪"):
        interior_quality = st.number_input("Interior Condition", value=4.0, step=1.0)
        interior_q1q6 = st.number_input("Interior Quality", value=4.0, step=1.0)
    
    with st.expander("Kitchen 🍎"):
        kitchen_quality = st.number_input("Kitchen Condition", value=4.0, step=1.0)
        kitchen_q1q6 = st.number_input("Kitchen Quality", value=4.0, step=1.0)
    
    with st.expander("Property 📪"):
        property_quality = st.number_input("Property Condition", value=4.0, step=1.0)
        property_q1q6 = st.number_input("Property Quality", value=4.0, step=1.0)
    
    # Structure and Other Features
    st.subheader("Structure and Other Features")
    with st.expander("Below Grade Areas 🔧"):
        below_grade_finished_area = st.number_input("Below Grade Finished Area", value=0, step=10)
        below_grade_unfinished_area = st.number_input("Below Grade Unfinished Area", value=0, step=10)
    
    with st.expander("Others"):
        fireplaces_total = st.number_input("Total Fireplaces 🔥", value=0, step=1)
        garage_spaces = st.number_input("Garage Spaces 🚗", value=1, step=1)
        bathrooms_half = st.number_input("Half Bathrooms 🚽", value=3, step=1)

    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        "Characteristics_LotSizeSquareFeet": [LotSizeSquareFeet],
        "ImageData_c1c6_summary_bathroom": [bathroom_quality],
        "ImageData_c1c6_summary_exterior": [exterior_quality],
        "ImageData_c1c6_summary_interior": [interior_quality],
        "ImageData_c1c6_summary_kitchen": [kitchen_quality],
        "ImageData_c1c6_summary_property": [property_quality],
        "ImageData_q1q6_summary_bathroom": [bathroom_q1q6],
        "ImageData_q1q6_summary_exterior": [exterior_q1q6],
        "ImageData_q1q6_summary_interior": [interior_q1q6],
        "ImageData_q1q6_summary_kitchen": [kitchen_q1q6],
        "ImageData_q1q6_summary_property": [property_q1q6],
        "Location_GIS_Latitude": [Latitude],
        "Location_GIS_Longitude": [Longitude],
        "Structure_BathroomsFull": [BathroomsFull],
        "Structure_BathroomsHalf": [bathrooms_half],
        "Structure_BedroomsTotal": [BedroomsTotal],
        "Structure_BelowGradeFinishedArea": [below_grade_finished_area],
        "Structure_BelowGradeUnfinishedArea": [below_grade_unfinished_area],
        "Structure_FireplacesTotal": [fireplaces_total],
        "Structure_GarageSpaces": [garage_spaces],
        "Structure_LivingArea": [LivingArea],
        "Structure_YearBuilt": [YearBuilt],
    })

    return input_data


# Get user input
user_input = get_user_input()

# Make a prediction 
if st.button("Predict Price"):
    prediction = model.predict(user_input)[0]
    st.write(f"Predicted Price: ${prediction:,.2f}")