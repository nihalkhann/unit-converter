
import streamlit as st

st.set_page_config(
    page_title="Nihal Unit Converter",
    page_icon="🔁",
)

st.markdown("""
<style>
    .main {
        padding: 1rem;
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        height: 3rem;
        margin-top: 1.7rem;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #1976D2;
    }
    .stSelectbox {
        border-radius: 5px;
    }
    /* Result box styling */
    .result-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        border: 1px solid #e9ecef;
    }
    h1 {
        color: #1E88E5;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-style: italic;
        color: #6c757d;
    }
</style>
""", unsafe_allow_html=True)

unit_categories = {
    "Area": {
        "Square Kilometer": 1e6,
        "Square Meter": 1.0,
        "Square Centimeter": 1e-4,
        "Square Millimeter": 1e-6,
        "Square Mile": 2.59e6,
        "Acre": 4046.86,
        "Hectare": 10000.0,
    },
    "Data Transfer Rate": {
        "Bits per second (bps)": 1.0,
        "Kilobits per second (Kbps)": 1e3,
        "Megabits per second (Mbps)": 1e6,
        "Gigabits per second (Gbps)": 1e9,
        "Terabits per second (Tbps)": 1e12,
    },
    "Digital Storage": {
        "Byte": 1.0,
        "Kilobyte": 1e3,
        "Megabyte": 1e6,
        "Gigabyte": 1e9,
        "Terabyte": 1e12,
        "Petabyte": 1e15,
    },
    "Energy": {
        "Joule": 1.0,
        "Kilojoule": 1e3,
        "Calorie": 4.184,
        "Kilocalorie": 4184.0,
        "Watt-hour": 3600.0,
        "Kilowatt-hour": 3.6e6,
    },
    "Frequency": {
        "Hertz": 1.0,
        "Kilohertz": 1e3,
        "Megahertz": 1e6,
        "Gigahertz": 1e9,
    },
    "Fuel Economy": {
        "Kilometers per liter (km/L)": 1.0,
        "Miles per gallon (mpg)": 0.425144,
    },
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
    "Plane Angle": {
        "Degree": 1.0,
        "Radian": 57.2958,
        "Gradian": 0.9,
    },
    "Pressure": {
        "Pascal": 1.0,
        "Kilopascal": 1e3,
        "Bar": 1e5,
        "Atmosphere": 101325.0,
        "Pound per square inch (psi)": 6894.76,
    },
    "Speed": {
        "Meters per second": 1.0,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knot": 0.514444,
    },
    "Temperature": {
        "Celsius": "celsius",
        "Fahrenheit": "fahrenheit",
        "Kelvin": "kelvin",
    },
    "Time": {
        "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
    },
    "Volume": {
        "Cubic Meter": 1.0,
        "Liter": 0.001,
        "Milliliter": 1e-6,
        "Cubic Centimeter": 1e-6,
        "Cubic Inch": 1.63871e-5,
        "Cubic Foot": 0.0283168,
        "Cubic Yard": 0.764555,
    },
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9  # F to C formula
    elif from_unit == "Kelvin":
        celsius = value - 273.15  # K to C formula
    
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15

st.markdown('<h1 style="text-align: center;"> Unit Converter</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; margin-bottom: 30px;">Convert between different units of measurement</p>', unsafe_allow_html=True)


category = st.selectbox("Select measurement category", list(unit_categories.keys()))


units = unit_categories[category]

col1, col2 = st.columns([2, 2])

with col1:
    st.markdown("### From")
    input_unit = st.selectbox("From Unit", list(units.keys()), key="unit_from", label_visibility="collapsed")
    input_value = st.number_input("Enter value", value=1.0, step=0.01, format="%.6g", key="unit_value")

with col2:
    st.markdown("### To")
    output_unit = st.selectbox("To Unit", list(units.keys()), key="unit_to", index=1, label_visibility="collapsed")

convert_button = st.button("Convert Now")

if convert_button:
    if category == "Temperature":
        result = convert_temperature(input_value, input_unit, output_unit)
        unit_symbols = {"Celsius": "°C", "Fahrenheit": "°F", "Kelvin": "K"}
        
        st.markdown("### Conversion Result")
        st.markdown(f"<h2 style='text-align: center; color: #1E88E5;'>{input_value} {unit_symbols[input_unit]} = {result:.6g} {unit_symbols[output_unit]}</h2>", unsafe_allow_html=True)
    else:
        result = input_value * units[input_unit] / units[output_unit]
        
        st.markdown("### Conversion Result")
        st.markdown(f"<h2 style='text-align: center; color: #1E88E5;'>{input_value} {input_unit} = {result:.6g} {output_unit}</h2>", unsafe_allow_html=True)
        
        st.markdown("<p style='text-align: center;'><i>Conversion Formula:</i></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-family: monospace;'>{input_value} × ({units[input_unit]}) ÷ ({units[output_unit]})</p>", unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ by Nihal Khan Ghouri</div>', unsafe_allow_html=True)
