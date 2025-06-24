# 🧠 HealthAI: Intelligent Healthcare Assistant

HealthAI is an intelligent, AI-powered healthcare assistant built using **Streamlit**, **OpenAI/Gemini APIs**, and **interactive data visualizations**. It provides users with accurate medical insights through features like patient chat, disease prediction, treatment plan generation, and health analytics dashboards.

---

## 🚀 Features

### 🩺 Patient Chat System
- Conversational interface to ask health-related questions.
- Responses powered by OpenAI GPT-3.5 / Gemini Pro.
- Session-based chat history for better user interaction.

### 🔬 Disease Prediction System
- Input symptoms to get possible medical conditions.
- Includes patient age and gender for better predictions.
- AI-generated likelihood and recommended next steps.

### 💊 Treatment Plan Generator
- Input diagnosed condition and patient details.
- Generates a complete treatment plan including:
  - Medications
  - Lifestyle changes
  - Follow-up care suggestions

### 📈 Health Analytics Dashboard
- Visualize patient health data (heart rate, glucose, blood pressure).
- AI-generated insights for long-term trend analysis.
- Dynamic and interactive charts with summaries.

---

## 📁 Project Structure

```bash
├── app.py                       # Main application file (Streamlit)
├── core/
│   ├── __init__.py
│   ├── patient_chat.py
│   ├── disease_prediction.py
│   ├── treatment_plan/
│   │   └── generate_treatment_plan.py
│   ├── analytics/
│   │   └── health_insights.py
│
├── utils/
│   └── openai_client.py         # OpenAI or Gemini API wrapper
│
├── data/
│   └── sample_health_data.py    # Sample patient health metrics
│
├── .env                         # Environment variables (API keys)
└── README.md                    # Project documentation
