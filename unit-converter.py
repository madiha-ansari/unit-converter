import streamlit as st

# Streamlit is a library for building web applications.

# Function to convert units based on predefined values.
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000
    }

    key = f"{unit_from}_{unit_to}"
    return value * conversions[key] if key in conversions else None

st.title("Unit Converter")

# User input for value
value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

# Dropdown to select units for conversion
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# Button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    if result is not None:
        st.success(f"Converted Value: {result}")
    else:
        st.warning("Conversion not supported for the selected units.")

# PowerShell commands to activate virtual environment and run Streamlit
# command
# .venv\Scripts\Activate
# streamlit run unit-converter.py
