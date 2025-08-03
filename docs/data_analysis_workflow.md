# Brent Oil Price Change Point Analysis: Data Analysis Workflow and Insights

## 1. Defining the Data Analysis Workflow

### a. Steps and Processes Involved

1. **Data Acquisition and Loading**  
   Load historical Brent oil prices from `brent_oil_prices.csv` and key events from `key_events.csv`.

2. **Data Preprocessing**  
   Clean and prepare the time series data:
   - Handle missing values.
   - Ensure correct data types (especially dates).
   - Resample the data if necessary.

3. **Exploratory Data Analysis (EDA)**  
   Analyze the Brent oil price data for key time series properties:
   - Trend
   - Seasonality (if any)
   - Stationarity  
   Visualize the data to identify patterns and potential change points.

4. **Event Data Integration**  
   Align key geopolitical and economic events with the oil price time series by mapping event dates to the dataset.

5. **Change Point Model Building (PyMC3)**  
   Construct a **Bayesian change point model** using PyMC3 to detect significant shifts in the **mean** and/or **variance** of Brent oil prices over time.

6. **Model Inference and Sampling**  
   Run **MCMC (Markov Chain Monte Carlo)** to obtain posterior distributions:
   - Number and locations of change points
   - Parameters before and after each change point

7. **Model Evaluation and Interpretation**  
   Analyze the posterior results to identify probable change points. Interpret changes in price behavior (mean, variance) associated with those points.

8. **Event Correlation and Impact Measurement**  
   Correlate statistical change points with known historical events. Quantify their impact on oil price shifts.

9. **Insight Generation and Storytelling**  
   Synthesize data-driven insights that explain *how* and *why* events impacted oil prices.

10. **Dashboard Development**  
    Build an interactive dashboard (Flask + React) for:
    - Visualizing time series data
    - Displaying change points
    - Overlaying historical events

11. **Reporting and Communication**  
    Prepare a comprehensive report summarizing methodology, findings, and strategic insights.

---

### b. Research and Compile Event Data

*To be populated with 10–15 key geopolitical and economic events and their dates in `data/events/key_events.csv`.*

---

### c. Assumptions and Limitations of the Analysis

#### Assumptions

- **Data Quality**: Assumes Brent oil price data is accurate and complete.
- **Event Relevance**: Assumes chosen events are relevant to oil price movements.
- **Model Validity**: Assumes Bayesian change point models are suitable for identifying structural breaks.
- **Stationarity**: Assumes data is or can be made stationary for valid statistical analysis.

#### Limitations

- **Correlation ≠ Causation**: Statistical correlation with events does *not* imply causation.
- **Event Date Precision**: Varies and may impact alignment accuracy.
- **Model Complexity**: Risk of overfitting/underfitting.
- **Unobserved Variables**: Some influencing factors may not be included in the data.
- **Forecasting Use**: Change point models are primarily backward-looking.

---

### d. Communication Channels and Formats

- **Interactive Dashboard**  
  Built using **Flask (backend)** and **React (frontend)**. Allows dynamic exploration of:
  - Change points
  - Time series plots
  - Event overlays

- **Comprehensive Report**  
  Delivered as `reports/final_report.pdf` or `docs/project_documentation.md`, including:
  - Methodology
  - Visualizations
  - Interpretations
  - Recommendations

- **Presentation Slides**  
  Summarized findings for executive or stakeholder review.

- **Technical Documentation**  
  Detailed documentation of the model, code, and analysis in `docs/project_documentation.md`.

---

## 2. Understanding the Model and Data

### a. Main References

(To be listed: papers/books on Bayesian change point analysis, PyMC3, and time series modeling.)

---

### b. Analyze Time Series Properties

(To be populated after EDA in `notebooks/EDA.ipynb`.)

---

### c. Purpose of Change Point Models

Change point models detect **structural breaks** in time series data. They help:

- **Identify abrupt shifts** in mean/variance
- **Understand different market regimes**
- **Correlate shifts with real-world events**
- **Improve forecasting and risk analysis** by accounting for regime changes

---

### d. Expected Outputs and Limitations of Change Point Analysis

#### Expected Outputs

- **Number of Change Points**  
- **Dates/Locations** of structural shifts
- **Parameter Values** for each segment (e.g., mean price, volatility)
- **Uncertainty Estimates** (via full posterior distributions)

#### Limitations

- **Assumption of Sudden Shifts**  
  Gradual changes may be missed.
- **Sensitivity to Noise**  
  Noise may introduce false positives.
- **Choice of Priors (Bayesian)**  
  Affects outcomes, especially with limited data.
- **Computational Expense**  
  MCMC methods can be slow on large datasets.
- **Causal Interpretation**  
  Domain expertise is essential for interpreting causes.

---

## 3. Analysis and Insights from Brent Oil Change Point Model

This section summarizes results from the PyMC3-based change point model and correlates them with real-world events.

---

### 1. Identified Change Point and Interpretation

- **Most Probable Change Point Index**:  
  Posterior summary from `model.py` shows the **mean of tau ≈ 214**.  
  Given a start date of **May 1987**, this corresponds to approximately **September 2005**.

- **Posterior Certainty**:  
  The **credible interval** (HDI 2.5% to 97.5%) for tau is **[211, 218]**, indicating high confidence and a time window of about 7 months.  
  This suggests a **highly significant structural break**.

---

### 2. Association with Causal Events

The detected change point (~September 2005) aligns with a major shift in global oil dynamics:

- **Rapid Global Demand Growth**  
  Particularly from **China** and **India**.

- **Geopolitical Instability**  
  Ongoing tensions in the **Middle East** contributed to risk premiums.

- **Decline in Spare Capacity**  
  By 2005, **OPEC’s spare production** was critically low, increasing market sensitivity.

> These factors likely triggered a **new regime of higher oil prices**, and the model’s findings reflect this shift.

---

### 3. Quantitative Impact

The model estimates average prices:

- **Before Change Point (`mu1`)**: **$21.40**
- **After Change Point (`mu2`)**: **$75.79**

This is a **254% increase** in average Brent oil price after the detected change point — statistically significant and economically meaningful.

---

### 4. Advanced Extensions

To expand the analysis:

#### **a. Log Returns and Volatility**

- Use **log(P_t) - log(P_t-1)** instead of raw prices.
- Easier to model **stationary processes**.
- Enables modeling of **volatility clustering** and shifts in **market turbulence**.

#### **b. Advanced Models**

- **Vector Autoregression (VAR)**  
  Models interactions between oil price, GDP, inflation, etc.

- **Markov-Switching Model**  
  Explicitly models multiple regimes (e.g., high/low volatility), not just discrete change points.

> These models allow richer, more dynamic interpretations of market behavior.

---

## ✅ Summary

This project applies Bayesian change point modeling to Brent oil price data to detect structural breaks and correlate them with real-world events. A key change point around **September 2005** was identified with high certainty and matched major shifts in global oil dynamics. This analysis provides **quantitative**, **interpretable**, and **visualizable** insights into the impact of macro events on oil markets — with actionable directions for future modeling and business intelligence.

---
