import streamlit as st


# Custom Styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #4CAF50, #2196F3);
            font-family: Arial, sans-serif;
        }
        .stSlider {
            color: #ff5733 !important;
        }
        .bmi-box {
            background: #f1f1f1;
            padding: 15px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Subtitle
st.title("⚖️ BMI Calculator")
st.subheader("Check your health status with an easy BMI calculation! 🏋️‍♂️")

# Input Sliders
height = st.slider("📏 Select your height (in cm)", 100, 250, 170)
weight = st.slider("🏋️ Select your weight (in kg)", 30, 200, 70)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Determine BMI Category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 😟", "#3498db"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight ✅", "#2ecc71"
    elif 25 <= bmi < 29.9:
        return "Overweight ⚠️", "#f39c12"
    else:
        return "Obese ❌", "#e74c3c"

category, color = get_bmi_category(bmi)

# Display BMI Result
st.markdown(
    f"""
    <div class="bmi-box" style="border-left: 8px solid {color};">
        Your BMI: <span style="color: {color}; font-size: 24px;">{bmi:.2f}</span> <br>
        <span style="color: {color}; font-size: 22px;">{category}</span>
    </div>
    """,
    unsafe_allow_html=True
)

# BMI Categories Info
st.write("### 📊 BMI Categories")
st.success("✔ **Underweight**: BMI less than 18.5")
st.info("✔ **Normal weight**: BMI between 18.5 and 24.9")
st.warning("✔ **Overweight**: BMI between 25 and 29.9")
st.error("✔ **Obesity**: BMI 30 or greater")

st.write("💡 **Tip:** Maintain a balanced diet and exercise regularly for a healthy BMI!")


