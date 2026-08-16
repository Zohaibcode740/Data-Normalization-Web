import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from io import BytesIO
def detect_dataset_type_offline(df):
    cols = [c.lower() for c in df.columns]
    if any(k in cols for k in ["employee", "salary", "age", "department", "job", "position", "hr"]):
        return "👨‍💼 Employee / HR Data"
    elif any(k in cols for k in ["car", "model", "engine", "speed", "mileage", "vehicle", "fuel"]):
        return "🚗 Car / Vehicle Data"
    elif any(k in cols for k in ["product", "item", "price", "category", "stock", "sales"]):
        return "🛍️ Product / Sales Data"
    elif any(k in cols for k in ["student", "class", "grade", "marks", "school", "university", "course"]):
        return "🎓 Student / Education Data"
    elif any(k in cols for k in ["date", "temperature", "humidity", "weather", "rainfall", "climate"]):
        return "🌦️ Weather / Climate Data"
    elif any(k in cols for k in ["country", "city", "region", "population", "area", "continent"]):
        return "🌍 Geographic / Demographic Data"
    else:
        return "❓ Unknown / Miscellaneous Data"


# -------------------------
# ⚙️ Streamlit Page Setup
# -------------------------
st.set_page_config(page_title="Smart Data Normalizer", page_icon="📊", layout="wide")

# -------------------------
# 💅 Custom Dark Theme CSS
# -------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
    color: #60a5fa;
    font-weight: 700;
    letter-spacing: 0.5px;
}

[data-testid="stSidebar"] {
    background: #1e293b;
    border-right: 1px solid #334155;
}

.stButton > button {
    background: linear-gradient(90deg, #3b82f6, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 1.3rem;
    font-size: 1rem;
    font-weight: 600;
    box-shadow: 0px 4px 12px rgba(59, 130, 246, 0.3);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 6px 18px rgba(59, 130, 246, 0.5);
}

.stDownloadButton > button {
    background: linear-gradient(90deg, #10b981, #059669);
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    box-shadow: 0px 4px 12px rgba(16, 185, 129, 0.3);
    transition: 0.3s;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 6px 18px rgba(16, 185, 129, 0.5);
}

.stSelectbox, .stFileUploader {
    background-color: #1e293b !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
    border: 1px solid #334155 !important;
}

.stDataFrame {
    border-radius: 10px !important;
    background: #0f172a !important;
    color: #e2e8f0 !important;
}

.css-1d391kg, .stTextInput > div > div > input {
    background-color: #1e293b !important;
    color: #e2e8f0 !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
}

.stAlert {
    background-color: #1e3a8a !important;
    border-radius: 10px !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 🧠 App Content
# -------------------------
st.title("📊 Smart Data Normalizer (Dark Mode)")
st.markdown("### Upload your dataset, detect its type, and normalize numeric columns automatically — now in a **sleek dark blue theme.**")

uploaded_file = st.file_uploader("📤 Upload CSV or Excel File", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Original Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    dataset_type = detect_dataset_type_offline(df)
    st.success(f"**Detected Dataset Type:** {dataset_type}")

    method = st.selectbox("⚙️ Choose Normalization Method", ["Min-Max", "Standard"])
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    st.write(f"Detected Numeric Columns: `{numeric_cols}`")

    if st.button("🚀 Normalize Data"):
        if not numeric_cols:
            st.warning("⚠️ No numeric columns found to normalize.")
        else:
            scaler = MinMaxScaler() if method == "Min-Max" else StandardScaler()
            df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

            st.success("✅ Data normalized successfully!")
            st.subheader("📈 Normalized Data Preview")
            st.dataframe(df.head(), use_container_width=True)

            if uploaded_file.name.endswith(".csv"):
                output_file = "normalized_data.csv"
                data_bytes = df.to_csv(index=False).encode("utf-8")
                mime_type = "text/csv"
            else:
                output_file = "normalized_data.xlsx"
                buffer = BytesIO()
                with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False)
                data_bytes = buffer.getvalue()
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            st.download_button("📥 Download Normalized File", data_bytes, output_file, mime_type)

else:
    st.info("⬆️ Upload a dataset to get started.")
