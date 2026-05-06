# Sandhya Aqua - Daily Feed Calculator

A professional Streamlit web application designed for aquaculture farms to calculate **daily feed requirement** and **corrected FCR (Feed Conversion Ratio)** using real-world shrimp farming formulas.

---

##  Live App
👉 [https://your-app-name.streamlit.app](https://sandhya-aqua-feed-calculator-w7ytz86crjtej29a7h2ugf.streamlit.app/)

---

##  Project Overview

This application helps shrimp farmers and analysts:

- Estimate **daily feed requirement (Kg)**
- Calculate **Feed Conversion Ratio (FCR)**
- Adjust FCR based on **natural productivity**
- Reduce manual calculation errors from Excel models

---

##  Key Features

-  Clean and professional UI (Streamlit)
-  Real-time input validation
-  Accurate domain-specific calculations
-  Instant results with meaningful formatting
-  Lightweight and fast deployment

---

## Input Parameters

- Population (in millions)
- Survival (%)
- Estimated ADG (g)
- Feed Protein (%)
- Digestibility (%)
- Natural Productivity (%)

---

## Output

- Estimated Daily Feed (Kg)
- Corrected FCR

---

##  Formula Logic

- Biomass = (Population × Survival × ADG) / 1000  
- Protein Increase = Biomass × 0.21  
- Digestible Protein = Feed Protein × Digestibility (%)  
- Daily Feed = Protein Increase / (Digestible Protein × NPU)  
- FCR = Daily Feed / Biomass  
- Corrected FCR = FCR − (FCR × Productivity)

> Note: NPU is fixed at 0.5 based on domain standards.

---

## Tech Stack

- Python
- Streamlit
- Basic Data Modeling

---

##  How to Run Locally

```bash
pip install streamlit
streamlit run app.py
