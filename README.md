# Birhan Energies: Brent Oil Change Point Analysis

This project contains the code and documentation for the "Brent Oil Change Point Analysis" challenge. The project aims to analyze Brent oil price data to identify significant shifts and correlate them with major geopolitical, economic, and OPEC policy events.

## Project Structure

* `data/`: Contains raw and processed oil price data.
* `events/`: Stores the curated dataset of key historical events.
* `src/`: Houses the core Python scripts for data preparation, modeling, and analysis.
* `notebooks/`: Includes the Jupyter notebook for exploratory data analysis (EDA).
* `docs/`: Contains project documentation, including detailed analysis insights.
* `reports/`: Stores generated reports and visualizations.
* `dashboard/`: Holds the code for the interactive frontend (React/Vite) and backend (Flask).

## Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/alexkalll/Birhan-Energies-BrentOil-ChangePoint-Analysis.git](https://github.com/alexkalll/Birhan-Energies-BrentOil-ChangePoint-Analysis.git)
cd Birhan-Energies-BrentOil-ChangePoint-Analysis
```

### 2\. Set Up the Environment

First, create a virtual environment and activate it:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

Next, install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 3\. Run the Analysis

Follow the steps below to run the full analysis workflow:

1.  **Data Preparation:** Execute the data preparation script to clean and process the time series data.
    ```bash
    python src/data_preparation.py
    ```
2.  **Exploratory Data Analysis (Optional):** Open and run the `EDA.ipynb` notebook to visually explore the data.
    ```bash
    jupyter notebook notebooks/EDA.ipynb
    ```
3.  **Model Fitting:** Run the modeling script to perform the Bayesian change point detection. The output will be logged to `logs/modeling.log`.
    ```bash
    python src/model.py
    ```
4.  **Analysis and Visualization:** Execute the analysis script to generate a plot comparing the model's change point with the key events. The plot will be saved to the `reports` directory.
    ```bash
    python src/analysis.py
    ```

### 4\. Detailed Analysis and Insights (Task 2)

The core analysis of the Brent oil price series is documented in `docs/analysis_and_insights.md`. This document details:

  * The implementation of the Bayesian Change Point detection model using PyMC3.
  * The identification of statistically significant structural breaks (change points) in the Brent oil price series.
  * The association of detected change points with researched key events.
  * A quantitative description of the impact of these changes (e.g., shift in mean price).

You can review the detailed findings in `docs/analysis_and_insights.md`.

### 5\. Interactive Dashboard (Task 3)

An interactive dashboard has been developed using Flask (backend) and React (frontend) to visualize the analysis results.

#### 5.1. Running the Backend (Flask API)

The backend provides API endpoints to serve the processed data and events to the frontend.

1.  Navigate to the backend directory:
    ```bash
    cd dashboard/backend
    ```
2.  Install the Python dependencies for the backend:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Flask application. **Ensure you specify a port, e.g., 5001, if port 5000 is in use.**
    ```bash
    python app.py --port 3000
    ```
    The API will be accessible, e.g., at `http://localhost:5001/api/data` and `http://localhost:5001/api/events`.

#### 5.2. Running the Frontend (React with Vite)

The frontend is a React application that consumes data from the Flask API and visualizes it.

1.  Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```
2.  Install the Node.js dependencies:
    ```bash
    npm install
    # Also ensure recharts is installed
    npm install recharts
    ```
3.  Start the Vite development server:
    ```bash
    npm run dev
    ```
    The dashboard will typically open in your browser at `http://localhost:5173/` (or a similar port). Ensure your backend server is running *before* starting the frontend.

## Future Works

While the core objectives of change point detection and dashboard creation are complete, there are several avenues for advanced analysis and enhancement:

  * **Explore Other Potential Factors:** Incorporate other macroeconomic data sources (e.g., GDP, inflation rates, exchange rates) to build a more comprehensive explanatory model.
  * **Consider Advanced Models:** Implement other models like VAR (Vector Autoregression) to analyze dynamic relationships between oil prices and macroeconomic variables, or Markov-Switching models to define and detect different market regimes (e.g., 'calm' vs. 'volatile').
  * **Enhanced Frontend Features:** Add more interactive elements to the dashboard, such as date range filters, event selection, and comparison tools.
  * **Deployment:** Containerize the entire application using Docker and deploy it to a cloud platform (e.g., AWS, Azure, GCP) for broader accessibility.
