import streamlit as st

# Function to calculate estimated HbA1c
def calculate_hba1c(average_blood_glucose):
    # Formula for estimated HbA1c based on average blood glucose (mg/dL)
    return (average_blood_glucose + 46.7) / 28.7

# Function to provide health advice based on fasting and postprandial levels
def provide_health_advice(fasting_glucose, postprandial_glucose):
    advice = ""
    if fasting_glucose < 70:
        advice += "Your fasting glucose is low (Hypoglycemia). You should consult a doctor.\n\n"
    elif 70 <= fasting_glucose <= 100:
        advice += "Your fasting glucose is within the normal range.\n\n"
    else:
        advice += "Your fasting glucose is high (Hyperglycemia). You should consult a doctor.\n\n"
    
    if postprandial_glucose < 140:
        advice += "Your postprandial glucose is within the normal range.\n\n"
    elif 140 <= postprandial_glucose < 200:
        advice += "Your postprandial glucose is slightly elevated (Prediabetes). Consider lifestyle changes.\n\n"
    else:
        advice += "Your postprandial glucose is high (Diabetes). Consult a healthcare provider.\n\n"
    
    return advice

# Streamlit App Interface
st.title("Blood Glucose Level Assessment and HbA1c Calculator")

# User inputs for blood glucose levels
st.subheader("Enter your blood glucose levels")
fasting_glucose = st.number_input("Fasting Blood Glucose (mg/dL)", min_value=0.0, step=1.0, format="%.1f")
postprandial_glucose = st.number_input("Postprandial Blood Glucose (mg/dL)", min_value=0.0, step=1.0, format="%.1f")

# Calculate estimated HbA1c
if st.button("Calculate Estimated HbA1c"):
    # Average blood glucose (considering both fasting and postprandial)
    average_glucose = (fasting_glucose + postprandial_glucose) / 2
    estimated_hba1c = calculate_hba1c(average_glucose)
    st.write(f"### Estimated HbA1c: {estimated_hba1c:.2f}%")

# Provide health advice
if st.button("Get Health Advice"):
    advice = provide_health_advice(fasting_glucose, postprandial_glucose)
    st.write(f"### Health Advice:\n{advice}")
