import streamlit as st
st.markdown(
    """
<style>
    /* Overall Background */
    .stApp {
        background: linear-gradient(to right, #1c1c1c, #363636);
        color: white;
        font-family: 'Poppins', sans-serif;
        padding: 20px;
        border-radius: 12px;
    }

    /* Title Styling */
    h1 {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        padding-bottom: 10px;
    }

    /* Sidebar Styling (Smoother and Less Contrast) */
    section[data-testid="stSidebar"] {
        background: linear-gradient(to right, #1c1c1c, #363636);
        color: white;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    }

    /* Sidebar Text */
    section[data-testid="stSidebar"] .css-1d391kg {
        color: #e0e0e0; /* Soft white, not too bright */
    }

    /* Sidebar Select Box */
    section[data-testid="stSidebar"] .stSelectbox {
        background: rgba(255, 255, 255, 0.12); /* Slightly visible */
        border-radius: 10px;
        padding: 10px;
        color: #ffffff;
        
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(to right, #545454, #767676);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 20px;
        border-radius: 10px;
        transition: 0.3s ease-in-out;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
        border: none;
    }

    .stButton>button:hover {
        transform: scale(1.07);
        background: linear-gradient(to right, #676767, #8c8c8c);
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
        color: white;
    }

    /* Result Box */
    .result-box {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 0 12px rgba(255, 255, 255, 0.2);
        color: white;
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(to right, #222222, #333333);
        color: #f1f1f1;
        text-align: center;
        padding: 12px 20px;
        font-size: 14px;
        font-family: 'Roboto', sans-serif;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        transition: 0.3s ease-in-out;
    }
    
    .footer:hover {
        background: linear-gradient(to right, #333333, #222222);
        transform: translateX(-50%) scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    .footer a {
        color: #ffdd57;
        text-decoration: none;
        font-weight: bold;
    }
    div[data-testid="stNumberInput"] label, 
    div[data-testid="stSelectbox"] label {
    color: white !important; 
    font-size: 18px;
    font-weight: bold;
    }
    
    .footer a:hover {
        color: #ffffff;
        text-decoration: underline;
    }
    </style>
 
   
    """,
    unsafe_allow_html=True
)

# title and discription

st.markdown("<h1> Unit Convertor  </h1>", unsafe_allow_html=True)
st.write("Easily convert batween different units of length , weight, and temperature.")

# slide bar menu
conversion_type = st.sidebar.selectbox("Choose conversion type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometer", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometer", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Pounds", "Ounces"])
    with col2:
            to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# converted function
def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometer': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000,
        'Pounds': 2.2046, 'Ounces': 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit =="Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value 
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value 

# Button for conversion
if st.button("🤖Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_convertor(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    st.markdown('<div class="footer">📏⚖️ Developed by | <a href="https://www.linkedin.com/in/urooj-shakeel-47ba46272/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_recent_activity_content_view%3BjBbtjJB7Tlml%2BRvkaMVt7g%3D%3D" target="_blank">Urooj shakeel</a> | 🌡️⚙️</div>', unsafe_allow_html=True)
