import streamlit as st
import pandas as pd
import plotly.express as px

# Import core features
try:
    from core.patient_chat import answer_patient_query
except ModuleNotFoundError:
    st.error("❌ Missing: core/patient_chat.py")

try:
    from core.disease_prediction import predict_disease
except ModuleNotFoundError:
    st.error("❌ Missing: core/disease_prediction.py")

try:
    from core.treatment_plan.generate_treatment_plan import generate_treatment_plan
except ModuleNotFoundError:
    st.error("❌ Missing: core/treatment_plan/generate_treatment_plan.py")

try:
    from core.analytics.health_insights import generate_health_insights
except ModuleNotFoundError:
    st.error("❌ Missing: core/analytics/health_insights.py")

try:
    from core.profile.profile_manager import initialize_profile, update_profile, get_profile
except ModuleNotFoundError:
    st.error("❌ Missing: core/profile/profile_manager.py")


# Set page config
st.set_page_config(page_title="HealthAI", layout="wide")
st.sidebar.title("HealthAI Navigation")
page = st.sidebar.radio("Choose a Feature:", ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics", "Patient Profile"])


# ------------------- Patient Chat -------------------
if page == "Patient Chat":
    st.title("🩺 Patient Chat - Ask Your Health Questions")
    user_query = st.text_input("Enter your health-related question:")

    if st.button("Ask", key="ask_button"):
        if user_query.strip():
            with st.spinner("🤖 Fetching AI response..."):
                try:
                    response = answer_patient_query(user_query)
                    st.success("✅ Response:")
                    st.markdown(response)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a question before asking.")

# ------------------- Disease Prediction -------------------
elif page == "Disease Prediction":
    st.title("🔍 Disease Prediction System")

    symptoms = st.text_area("Enter your symptoms (e.g., fever, cough, fatigue):")
    age = st.number_input("Age (optional)", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender (optional)", ["", "Male", "Female", "Other"])

    if st.button("Predict Disease", key="predict_button"):
        if symptoms.strip():
            with st.spinner("🔬 Analyzing symptoms..."):
                try:
                    prediction = predict_disease(symptoms, age, gender)
                    st.success("✅ Prediction Result:")
                    st.markdown(prediction)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter symptoms to proceed.")

# ------------------- Treatment Plans -------------------
elif page == "Treatment Plans":
    st.title("💊 Treatment Plan Generator")
    st.markdown("Provide patient details to receive a personalized treatment plan.")

    condition = st.text_input("Diagnosed Condition")
    age = st.number_input("Age", min_value=0, max_value=120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    allergies = st.text_input("Known Allergies (comma-separated)")

    if st.button("Generate Plan", key="plan_button"):
        if condition.strip():
            with st.spinner("🧠 Generating treatment plan..."):
                try:
                    plan = generate_treatment_plan(condition, age, gender, allergies)
                    st.success("✅ Treatment Plan:")
                    st.markdown(plan)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a condition to generate a plan.")

# ------------------- Health Analytics -------------------
elif page == "Health Analytics":
    st.title("📊 Health Analytics Dashboard")
    st.markdown("AI-generated insights from weekly patient health trends.")

    from data.sample_patient_data import get_sample_health_data
    from core.analytics.health_insights import generate_health_insights

    data = get_sample_health_data()

    st.subheader("📅 Weekly Health Metrics")
    st.json(data)

    if st.button("Generate AI Insights", key="insight_button"):
        with st.spinner("🧠 Analyzing patient data with AI..."):
            try:
                insights = generate_health_insights()
                st.success("✅ Health Insights:")
                st.markdown(insights)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ------------------- Patient Profile -------------------
elif page == "Patient Profile":
    st.title("👤 Patient Profile Management")

    initialize_profile()
    profile = get_profile()

    name = st.text_input("Name", profile.get("name", ""))
    age = st.number_input("Age", min_value=0, max_value=120, value=profile.get("age", 0))
    gender = st.selectbox("Gender", ["", "Male", "Female", "Other"], index=["", "Male", "Female", "Other"].index(profile.get("gender", "")))
    allergies = st.text_input("Known Allergies", profile.get("allergies", ""))
    contact = st.text_input("Contact Number", profile.get("contact", ""))

    if st.button("Update Profile"):
        update_profile(name, age, gender, allergies, contact)
        st.success("✅ Profile updated successfully!")

    st.subheader("📄 Current Profile (JSON)")
    st.json(get_profile())



