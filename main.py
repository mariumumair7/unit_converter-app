import streamlit as st

conversion = {
    "Length": {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084
    },
    "Weight": {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return conversion[category][to_unit](value)
    
    base_value = value / conversion[category][from_unit]
    return base_value * conversion[category][to_unit]

st.title("Unit Converter App")

category = st.selectbox("Select a category", list(conversion.keys()))
units = list(conversion[category].keys())  


from_unit = st.selectbox("From Unit", units)

to_units = [unit for unit in units if unit != from_unit]
to_unit = st.selectbox("To Unit", to_units)

value = st.number_input("Enter Value", value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
