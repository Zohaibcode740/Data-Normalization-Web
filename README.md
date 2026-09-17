# 🤖 Offline Smart Data Normalizer (AI-Inspired Project)

A **Streamlit web app** that automatically detects dataset type (like Employee, Car, or Student data) and normalizes numeric columns using **Python, Pandas, and Scikit-Learn** — all **offline** and **free**.

> 💡 Originally designed to work with OpenAI / Google Gemini APIs, but now optimized for offline use — no API key or internet required!

---
# Data WorkFlow
![logo](https://github.com/Zohaibcode740/Zohaibcode740/blob/main/%40Syed%20Zohaib%20ALi.png)

## 🚀 Features

- 📤 **Upload CSV or Excel files**  
  Supports `.csv` and `.xlsx` formats up to 200MB.

- 🧠 **Automatic Dataset Type Detection (Offline)**  
  The app smartly detects dataset type (Employee, Student, Car, etc.) using column names.

- ⚙️ **Data Normalization**
  - Min-Max Normalization  
  - Standard (Z-Score) Normalization

- 📊 **Live Data Preview**  
  View your original and normalized data instantly.

- 📥 **Download Normalized File**  
  Export normalized data in both CSV and Excel formats.

- 💾 **Offline & Free**  
  100% local — no API calls, no cost, no rate limits.

---

## 🧰 Technologies Used

| Technology | Purpose |
|-------------|----------|
| 🐍 **Python 3.10+** | Core programming language |
| 📊 **Pandas** | Data handling & cleaning |
| 🧮 **Scikit-Learn** | Data normalization (MinMaxScaler, StandardScaler) |
| 📘 **OpenPyXL** | Excel file support |
| 🌐 **Streamlit** | Interactive web UI |
| 🧠 *(Optional)* **Gemini / OpenAI API** | For future AI dataset detection |

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ZohaiAli/offline-data-normalizer.git
cd offline-data-normalizer
