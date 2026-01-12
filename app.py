import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
# Title
# -------------------------------
st.title("AI-Based Single Plate Clutch Design Web App")
st.subheader("Real-Time Calculation, Graph & AI Recommendation")

# -------------------------------
# Input Section
# -------------------------------
st.header("Input Design Parameters")

P = st.number_input("Power (kW)", value=7.5, step=0.1)
N = st.number_input("Speed (rpm)", value=1500)
Ri = st.number_input("Inner Radius Ri (mm)", value=50)
Ro = st.number_input("Outer Radius Ro (mm)", value=100)
n = st.number_input("Number of friction surfaces", value=2)

mu_traditional = st.number_input("Coefficient of friction (Traditional)", value=0.3, step=0.01)
mu_sustainable = st.number_input("Coefficient of friction (Sustainable)", value=0.4, step=0.01)

# -------------------------------
# Calculations
# -------------------------------
Rm = (Ri + Ro) / 2
T = (9550 * P) / N

W_traditional = (T * 1000) / (mu_traditional * Rm * n)
W_sustainable = (T * 1000) / (mu_sustainable * Rm * n)

# -------------------------------
# Output Section
# -------------------------------
st.header("Calculated Results")

st.write(f"**Torque Transmitted:** {T:.2f} Nm")

col1, col2 = st.columns(2)
col1.metric("Traditional Axial Force (N)", f"{W_traditional:.0f}")
col2.metric("Sustainable Axial Force (N)", f"{W_sustainable:.0f}")

# -------------------------------
# Graph Section
# -------------------------------
st.header("Graphical Comparison")

fig, ax = plt.subplots()
ax.bar(
    ["Traditional Design", "Sustainable Design"],
    [W_traditional, W_sustainable]
)
ax.set_xlabel("Design Type")
ax.set_ylabel("Axial Force (N)")
ax.set_title("Traditional vs Sustainable Clutch Design")

st.pyplot(fig)

# -------------------------------
# AI-Based Recommendation
# -------------------------------
st.header("AI Recommendation")

reduction = ((W_traditional - W_sustainable) / W_traditional) * 100

if reduction > 20:
    st.success(
        f"AI Recommendation: Sustainable design is strongly recommended. "
        f"It reduces axial force by approximately {reduction:.1f}%, "
        "leading to lower wear, reduced heat generation, and improved energy efficiency."
    )
else:
    st.info(
        "AI Recommendation: Both designs are acceptable, "
        "but sustainable materials still offer better long-term performance."
    )

# -------------------------------
# Execution Readiness Note
# -------------------------------
st.markdown("---")
st.write("✔ This application is execution-ready and updates results automatically when inputs change.")
