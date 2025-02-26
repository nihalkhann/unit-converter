import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Nihal Unit Converter",
    page_icon="📏"
)

unit_categories = {
    "Length": {
        "Kilometer": 1000.0,
        "Meter": 1.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical mile": 1852.0,
    },
    "Mass": {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Microgram": 1e-9,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    },
    "Time": {
        "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
        "Week": 604800.0,
        "Year": 31536000.0,
    },
    "Volume": {
        "Cubic Meter": 1.0,
        "Liter": 0.001,
        "Milliliter": 1e-6,
        "Cubic Centimeter": 1e-6,
        "Cubic Inch": 1.6387e-5,
        "Cubic Foot": 0.0283168,
        "Cubic Yard": 0.764555,
    },
    "Area": {
        "Square Meter": 1.0,
        "Square Kilometer": 1e6,
        "Square Centimeter": 0.0001,
        "Square Millimeter": 1e-6,
        "Square Mile": 2.59e6,
        "Acre": 4046.86,
        "Hectare": 10000.0,
        "Square Yard": 0.836127,
        "Square Foot": 0.092903,
        "Square Inch": 0.00064516,
    },
    "Speed": {
        "Meters per second": 1.0,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Feet per second": 0.3048,
        "Knots": 0.514444,
    },
    "Energy": {
        "Joule": 1.0,
        "Kilojoule": 1000.0,
        "Calorie": 4.184,
        "Kilocalorie": 4184.0,
        "Watt-hour": 3600.0,
        "Kilowatt-hour": 3.6e6,
    },
    "Pressure": {
        "Pascal": 1.0,
        "Kilopascal": 1000.0,
        "Bar": 100000.0,
        "PSI": 6894.76,
        "Atmosphere": 101325.0,
    },
    "Data Transfer Rate": {
        "Bit per second": 1.0,
        "Kilobit per second": 1000.0,
        "Megabit per second": 1e6,
        "Gigabit per second": 1e9,
        "Terabit per second": 1e12,
        "Byte per second": 8.0,
        "Kilobyte per second": 8000.0,
        "Megabyte per second": 8e6,
        "Gigabyte per second": 8e9,
    },
    "Digital Storage": {
        "Bit": 1.0,
        "Kilobit": 1000.0,
        "Megabit": 1e6,
        "Gigabit": 1e9,
        "Terabit": 1e12,
        "Byte": 8.0,
        "Kilobyte": 8000.0,
        "Megabyte": 8e6,
        "Gigabyte": 8e9,
        "Terabyte": 8e12,
    },
    "Fuel Economy": {
        "Kilometers per liter": 1.0,
        "Miles per gallon": 0.425144,
    },
    "Plane Angle": {
        "Degree": 1.0,
        "Radian": 57.2958,
        "Gradian": 0.9,
    },
    "Frequency": {
        "Hertz": 1.0,
        "Kilohertz": 1000.0,
        "Megahertz": 1e6,
        "Gigahertz": 1e9,
    },
}
st.markdown('<h1 style="text-align: center;">Unit Converter</h1>', unsafe_allow_html=True)

#list to select units categories  
category = st.selectbox("Select Unit to convert",list(unit_categories.keys()))

units = unit_categories[category]
col1, col2 , col3 = st.columns(3)

with col1:
    # from to
    input_unit = st.selectbox("From", list(units.keys()), key="unit_from")
    # thats i provide value 
    input_value = st.number_input("Enter value", value=1.0, step=0.01, format="%.6g",
    key="unit_value")

with col2:
    output_unit = st.selectbox("To", list(units.keys()),key="unit_to", index=1)
    
with col3:
    convert_button = st.button("Convert")

if convert_button:
    # simple  input value thats multiply by units thats i provide in object and that devided
    result = input_value * units[input_unit] / units[output_unit]
    st.subheader("Conversion Result")
    st.success(f"{input_value} {input_unit} = {result:.6g} {output_unit}")
    st.success(f"Formula = {input_value} x ({units[input_unit]})  ÷ ({units[output_unit]}) ")


st.markdown('<h1 style="text-align: center; font-size : 18px">made with❤️by Nihal khan Ghouri</h1>', unsafe_allow_html=True)