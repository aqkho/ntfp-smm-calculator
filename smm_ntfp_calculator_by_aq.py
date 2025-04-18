
import streamlit as st

st.title("Skeletal Muscle Mass & Load Stress Calculator by AQ")
st.write("Estimate skeletal muscle mass and load-to-muscle stress ratio for various NTFPs")

# Gender presets
presets = {
    "Male": {"height": 165, "thigh": 48, "forearm": 28, "calf": 36},
    "Female": {"height": 154, "thigh": 45, "forearm": 25, "calf": 34}
}

gender = st.selectbox("Select Gender:", ["Male", "Female"])
if st.button("Use Preset for Gender"):
    st.session_state.update(presets[gender])

# Input fields
height = st.number_input("Enter height (cm):", min_value=100.0, max_value=220.0, value=st.session_state.get("height", 165.0))
thigh_circ = st.number_input("Enter thigh circumference (cm):", min_value=20.0, max_value=80.0, value=st.session_state.get("thigh", 48.0))
forearm_circ = st.number_input("Enter forearm circumference (cm):", min_value=15.0, max_value=50.0, value=st.session_state.get("forearm", 28.0))
calf_circ = st.number_input("Enter calf circumference (cm):", min_value=20.0, max_value=60.0, value=st.session_state.get("calf", 36.0))

# Calculate SMM
smm_g = height * (0.0553 * (thigh_circ ** 2) + 0.0987 * (forearm_circ ** 2) + 0.0331 * (calf_circ ** 2)) - 2445
smm_kg = round(smm_g / 1000, 2)

# NTFP loads
ntfp_loads = {
    "Bamboo": 60.00,
    "Rattan": 40.00,
    "Cinnamon": 23.00,
    "Star Anise": 10.00,
    "Pine Resin": 21.00,
    "Agarwood": 6.40,
    "Malva Nut": 3.00,
    "Bamboo Shoot": 2.50,
    "Wild Honey": 21.75
}

ntfp = st.selectbox("Select an NTFP:", list(ntfp_loads.keys()))
load = ntfp_loads[ntfp]

# Load-to-muscle ratio and stress level
ratio = round(load / smm_kg, 2)
stress_level = "High" if ratio > 2.5 else "Moderate" if ratio > 1.5 else "Low"

# Output results
st.markdown("### Results")
st.write(f"**Estimated Skeletal Muscle Mass:** {smm_kg} kg")
st.write(f"**Selected NTFP Load:** {load} kg")
st.write(f"**Load-to-Muscle Ratio:** {ratio}")
st.success(f"**Predicted Stress Level:** {stress_level}")
