# Project Documentation: Brent Oil Change Point Analysis

## 1. Introduction

This document details the analytical approach for the Brent oil price change point analysis. The primary goal is to identify significant shifts in oil price trends and associate them with key historical events, providing data-driven insights for stakeholders in the energy sector.

## 2. Data Analysis Workflow

The analysis is structured into a clear, reproducible workflow managed through a dedicated project directory. The main steps are:

1.  **Data Acquisition:** Raw daily Brent oil price data is sourced and stored in `data/raw/brent_oil_prices.csv`. A curated list of key historical events is stored in `data/events/key_events.csv`.
2.  **Data Preparation:** The `src/data_preparation.py` script cleans the raw data, handles date formatting, and resamples the daily prices into a monthly time series. This processed data is then saved to `data/processed/processed_data.csv`.
3.  **Exploratory Data Analysis (EDA):** The `notebooks/EDA.ipynb` notebook visually explores the time series, checks for trends and seasonality, and overlays historical events to form preliminary hypotheses.
4.  **Modeling:** The `src/model.py` script implements a Bayesian change point model using the `PyMC` library to probabilistically identify the most likely point of structural change in the time series.
5.  **Analysis and Reporting:** The `src/analysis.py` script uses the model's output to visualize the inferred change point and compare it against the key events. The final visualizations and reports are saved to the `reports` directory.

## 3. Understanding the Model and Data

### Time Series Properties and Modeling Choices

The Brent oil price data exhibits a clear **non-stationary trend**, with a significant change in both the mean price and its volatility over the years. This non-stationary nature means traditional linear models (like simple linear regression) are unsuitable.

**Change point models** are ideal for this task as they are designed to detect abrupt shifts in the statistical properties of a time series. By modeling a change point, we can identify a date where the underlying process generating the prices fundamentally changed, which is exactly what we are looking for when investigating the impact of global events.

### Expected Outputs of a Change Point Analysis

The main outputs of our Bayesian change point analysis are:

* **Most Probable Change Point Date:** The single date where the model infers a structural break is most likely to have occurred.
* **Uncertainty of the Change Point:** A posterior distribution for the change point, providing a range of plausible dates rather than a single point estimate. This is a key advantage of the Bayesian approach.
* **Pre- and Post-Change Parameter Estimates:** The model provides posterior distributions for the mean price and volatility *before* and *after* the detected change.

## 4. Assumptions and Limitations

### Assumptions:

1.  **Single Change Point:** Our primary model assumes a single, abrupt change point. While a multi-change point model could be explored, this initial approach simplifies the problem and is often effective for identifying the most dominant shift.
2.  **Causality vs. Correlation:** The model identifies a statistical change in the time series that correlates with historical events. However, it **does not prove causality**. An event might occur near a change point, but this does not definitively mean the event *caused* the change. Further domain expertise is required to confirm a causal link.
3.  **Data Quality:** The analysis assumes the raw Brent oil price data is accurate and free from major errors.

### Limitations:

* **Model Simplification:** The model simplifies the price dynamics by assuming a constant mean and volatility before and after the change point. Real-world oil prices are influenced by complex, continuous factors.
* **Event Data Bias:** The list of key events is curated and may not be exhaustive. Our analysis is limited to the events we have identified.

## 5. Communication and Reporting

Results will be communicated through a combination of formats:

* **Interactive Dashboard:** A web-based dashboard will allow stakeholders to visualize the time series, the inferred change points, and a filterable list of key events. This provides a user-friendly way to explore the findings.
* **Interim and Final Report:** A detailed PDF report (`reports/interim_report.pdf` and `reports/final_report.pdf`) will present the methodology, quantitative results, and conclusions for a more in-depth audience.