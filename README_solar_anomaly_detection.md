
# 🌞 Big Data Anomaly Detection in U.S. Solar Power Output

## 📌 Overview
This project analyzes hourly solar power generation data from California ISO (CALISO) to detect abnormal patterns using both statistical and machine learning methods. The primary goal is to improve data quality monitoring, energy forecasting, and operational decision-making in the renewable energy sector.

---

## 🧰 Tools & Technologies
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn
- **Techniques:** Z-Score Thresholding, Isolation Forest (Unsupervised ML)
- **Data Source:** [U.S. Energy Information Administration (EIA) API](https://www.eia.gov/opendata/)
- **Timeframe:** January – March 2024 (hourly data)

---

## 🔍 Project Workflow
1. **Data Collection**
   - Fetched real-time hourly solar generation data via EIA API
   - Focused on `CALISO` region using fuel type `SUN`

2. **Data Cleaning & Feature Engineering**
   - Handled missing/negative values
   - Added time-based features (hour, day, weekday, etc.)

3. **Anomaly Detection**
   - **Z-Score Method:** Identified statistically unusual data points (z > 2 or 3)
   - **Isolation Forest:** Applied unsupervised learning to detect multivariate outliers

4. **Visualization**
   - Plotted time series generation data
   - Highlighted anomalies using Matplotlib

---

## 📈 Key Outputs
- `solar_california_cleaned.csv`: Cleaned dataset with time-based features
- `solar_anomalies_zscore.csv`: Z-score anomaly tagging
- `solar_anomalies_isolation_forest.csv`: ML-based anomaly tagging
- `solar_anomaly_plot.png`: Time series plot with anomaly highlights

---

## 💡 Insights & Recommendations
- Detected 12+ significant anomalies, some exceeding 14,500 MWh
- Unusual spikes may indicate sensor errors or data misreporting
- Companies can integrate these models for:
  - Maintenance alerts
  - Data quality audits
  - Improving solar forecasting accuracy

---

## 📂 Repository Structure
```
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_cleaning_exploration.ipynb
│   ├── 02_anomaly_detection_zscore.ipynb
│   └── 03_anomaly_detection_isolation_forest.ipynb
├── output/
├── scripts/
│   └── download_eia_data.py
├── README.md
└── requirements.txt
```

---

## 🚀 Future Enhancements
- Integrate weather data (temperature, irradiance) for contextual analysis
- Deploy interactive dashboards using Plotly Dash or Streamlit
- Apply forecasting models (ARIMA, Prophet) to predict generation

---

## 👤 Author
**Prathamesh Ankaram**  
[LinkedIn](http://bit.ly/Prathamesh18) | [GitHub](https://github.com/PrathameshAnkaram)

---

## 📜 License
This project is open-source and free to use for educational and non-commercial purposes.
