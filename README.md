# 🔋 NASA Lithium-Ion Battery Life Analytics

An engineering pipeline built in Python to extract, process, and visualize lithium-ion battery degradation characteristics using the **NASA Ames Prognostics Center of Excellence (PCoE)** benchmark dataset.

## 🚀 Project Overview
This project parses multi-dimensional binary MATLAB structures (`.mat`) to track the capacity fade of lithium-ion cells over prolonged cycling. By isolating discharge profiles, the pipeline maps true chemical degradation and identifies critical performance thresholds.

### Key Engineering Insights
* **Capacity Recovery Spikes:** The visible upward fluctuations in capacity demonstrate real-world battery regeneration physics, occurring during electrochemical stabilization rest periods.
* **End-of-Life (EOL) Breach:** The cell successfully flags the standard 80% automotive/aerospace EOL threshold (1.4 Ah) at cycle index **124**.

## 📊 Visualization
![Battery Degradation Curve](Capture%20d'écran%202026-06-29%20140328.png)

## 🛠️ Tech Stack & Concepts
* **Language:** Python
* **Libraries:** SciPy (Binary Matrix Parsing), Matplotlib (Data Visualization)
* **Domain Knowledge:** State of Health (SoH) tracking, Battery Management Systems (BMS), Prognostics.

---
🤝 **Join the Conversation:** Connect with other battery engineers and analytics enthusiasts in our [Telegram Community](https://t.me/+sN7pQLxJtGU4MDc0)!
