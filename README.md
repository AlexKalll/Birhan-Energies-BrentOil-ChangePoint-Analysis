# Birhan Energies: Brent Oil Change Point Analysis

This project contains the code and documentation for the "Brent Oil Change Point Analysis" challenge. The project aims to analyze Brent oil price data to identify significant shifts and correlate them with major geopolitical, economic, and OPEC policy events.

## Project Structure

* `data/`: Contains raw and processed oil price data.
* `events/`: Stores the curated dataset of key historical events.
* `src/`: Houses the core Python scripts for data preparation, modeling, and analysis.
* `notebooks/`: Includes the Jupyter notebook for exploratory data analysis (EDA).
* `docs/`: Contains project documentation.
* `reports/`: Stores generated reports and visualizations.
* `dashboard/`: Holds the code for the interactive frontend and backend.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/alexkalll/Birhan-Energies-BrentOil-ChangePoint-Analysis.git
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

## Future Works
- Task 2: Change Point Modeling and Insight Generation
- Task 3: Integrate the interactive dashboard into the project.
