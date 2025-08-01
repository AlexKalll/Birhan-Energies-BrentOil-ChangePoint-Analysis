# Data Analysis Workflow for Brent Oil Price Change Point Analysis

## 1. Defining the Data Analysis Workflow

### a. Steps and Processes Involved:

1.  **Data Acquisition and Loading**: Load historical Brent oil prices from `brent_oil_prices.csv` and key events from `key_events.csv`.
2.  **Data Preprocessing**: Clean and prepare the time series data. This includes handling missing values, ensuring correct data types (especially for dates), and potentially resampling if necessary.
3.  **Exploratory Data Analysis (EDA)**: Analyze the Brent oil price data for key time series properties such as trend, seasonality (if any), and stationarity. Visualize the data to identify initial patterns and potential change points.
4.  **Event Data Integration**: Align the researched key events with the oil price time series. This involves mapping event dates to the price data.
5.  **Change Point Model Building (PyMC3)**: Construct a Bayesian change point model using PyMC3 to identify significant shifts in the mean and/or variance of Brent oil prices over time.
6.  **Model Inference and Sampling**: Run the Markov Chain Monte Carlo (MCMC) sampler to obtain posterior distributions for the model parameters, including the number and locations of change points, and the parameters of the price distribution before and after each change point.
7.  **Model Evaluation and Interpretation**: Analyze the posterior distributions to identify the most probable change points. Interpret the changes in oil price behavior (mean, variance) associated with these points.
8.  **Event Correlation and Impact Measurement**: Correlate the identified statistical change points with the compiled geopolitical and economic events. Quantify the impact of these events on price changes.
9.  **Insight Generation and Storytelling**: Synthesize the findings into clear, data-driven insights that address the business objectives. Focus on explaining *how* and *why* certain events impacted oil prices.
10. **Dashboard Development**: Build an interactive dashboard (Flask/React) to visualize the data, change points, and event correlations, providing an intuitive interface for stakeholders.
11. **Reporting and Communication**: Prepare a comprehensive report detailing the methodology, findings, and recommendations.

### b. Research and Compile Event Data:

(This section will be populated with 10-15 key events and their approximate start dates, to be stored in `data/events/key_events.csv`.)

### c. Assumptions and Limitations of the Analysis:

**Assumptions:**

*   **Data Quality**: Assumes that the provided historical Brent oil price data is accurate and reliable.
*   **Event Relevance**: Assumes that the selected geopolitical and economic events are indeed relevant and have a potential impact on oil prices.
*   **Bayesian Model Appropriateness**: Assumes that a Bayesian change point model is an appropriate statistical framework for identifying structural breaks in the time series.
*   **Stationarity (or transformability to stationarity)**: While time series often exhibit non-stationarity, the modeling approach will assume that either the data is stationary or can be transformed to achieve stationarity for valid analysis.

**Limitations:**

*   **Correlation vs. Causation**: A crucial limitation is the distinction between statistical correlation and causal impact. While the analysis aims to identify *associations* between events and price changes, proving direct *causation* is inherently difficult and requires careful interpretation. The model will identify *when* changes occurred, and we will *correlate* these with known events, but this does not definitively prove that the event *caused* the change. Other unobserved factors might be at play.
*   **Event Data Granularity**: The precision of event start dates might vary, which could affect the exact alignment with price changes.
*   **Model Complexity**: Overly complex models might overfit the data, while overly simplistic models might miss subtle change points.
*   **External Factors**: The model might not account for all external factors influencing oil prices (e.g., technological advancements, natural disasters not explicitly listed as events).
*   **Forecasting Limitations**: While identifying past change points, the model's direct utility for future price forecasting is limited without further predictive modeling.

### d. Main Media Channels and Formats for Communicating Results to Stakeholders:

*   **Interactive Dashboard**: The primary channel for dynamic exploration of insights, allowing stakeholders to interact with the data, visualize change points, and filter by events. This will be built using Flask (backend) and React (frontend).
*   **Comprehensive Report (PDF/Markdown)**: A detailed document (e.g., `reports/final_report.pdf`, `docs/project_documentation.md`) outlining the methodology, findings, statistical interpretations, and strategic recommendations. This will include visualizations from the analysis.
*   **Presentations (Slides)**: Summarized key findings and actionable insights for executive briefings or broader stakeholder meetings.
*   **Technical Documentation**: Detailed explanations of the model, code, and data preparation steps for technical audiences (e.g., within `docs/project_documentation.md`).

## 2. Understanding the Model and Data

### a. Main References:

(This section would typically list academic papers, books, or online resources on Bayesian change point analysis, PyMC3, and time series analysis. For this project, the core concepts are understood as part of the AI's knowledge base.)

### b. Analyze Time Series Properties (Brent Oil Price Data):

(This section will be populated after performing EDA on `brent_oil_prices.csv` in the `notebooks/EDA.ipynb`.)

### c. Purpose of Change Point Models:

Change point models are statistical tools used to identify points in time where the statistical properties of a time series (e.g., mean, variance, trend) undergo a significant and abrupt change. In the context of analyzing Brent oil price fluctuations, these models are crucial for:

*   **Identifying Structural Breaks**: Pinpointing specific dates or periods when the underlying dynamics of oil prices shifted. These shifts could be due to external events (geopolitical, economic) or internal market changes.
*   **Understanding Market Regimes**: Helping to delineate different "regimes" or phases in the oil market, each characterized by distinct price behaviors. This allows for a more nuanced understanding than a single, static model.
*   **Attributing Changes to Events**: By identifying the timing of these structural breaks, we can then investigate and potentially correlate them with known major events, providing a quantitative link between events and market impact.
*   **Improved Forecasting and Risk Management**: Recognizing change points can improve the accuracy of forecasting models by allowing them to adapt to new market conditions. It also aids in risk management by highlighting periods of increased volatility or shifts in price levels.

### d. Expected Outputs and Limitations of Change Point Analysis:

**Expected Outputs:**

*   **Number of Change Points**: The estimated number of significant shifts in the time series.
*   **Dates/Locations of Change Points**: The specific time indices (dates) where these changes are most likely to have occurred.
*   **Parameter Values for Each Segment**: The estimated statistical parameters (e.g., mean price, price volatility) for the periods *between* the identified change points. This allows for a quantitative description of how the market behaved in different regimes.
*   **Uncertainty Estimates**: Bayesian models provide full posterior distributions for all parameters, including change point locations, offering a measure of confidence or uncertainty around these estimates.

**Limitations:**

*   **Assumption of Abrupt Changes**: Many change point models assume sudden, discrete shifts, which might not always reflect gradual transitions in real-world phenomena.
*   **Sensitivity to Noise**: Noisy data can sometimes lead to spurious change points or obscure real ones.
*   **Prior Specification (Bayesian)**: The choice of prior distributions in Bayesian models can influence the results, especially with limited data.
*   **Computational Cost**: Bayesian MCMC methods can be computationally intensive, especially for long time series or complex models.
*   **Interpretation Challenge**: While models identify statistical changes, the *causal* explanation for these changes still requires domain expertise and careful analysis of external events. The model tells us *when* a change happened, but not necessarily *why*.