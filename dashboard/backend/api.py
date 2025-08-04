import pandas as pd
from flask import jsonify
import numpy as np
import os
import arviz as az
import config

# --- Data Loading and Processing ---
def load_data():
    """
    Loads processed data and simulates inference results for the dashboard.
    In a production setting, this would load a saved trace.
    """
    try:
        # Load the processed oil price data using the path from config.py
        df_prices = pd.read_csv(config.PROCESSED_DATA_PATH, index_col='Date', parse_dates=True)
        # Load the events data using the path from config.py
        df_events = pd.read_csv(config.EVENTS_FILE_PATH, parse_dates=['Date'])

        # Simulate the inference data based on the log output for demonstration
        # In a real-world scenario, you would load the saved model output here
        mean_tau = 214.140
        std_tau = 1.993
        tau_samples = np.random.normal(loc=mean_tau, scale=std_tau, size=1000).astype(int)
        
        # Calculate the most probable change point date
        most_probable_tau = np.median(tau_samples).astype(int)
        change_point_date = df_prices.index[most_probable_tau]

        return df_prices, df_events, change_point_date

    except FileNotFoundError as e:
        print(f"Error: A file was not found. Please check your paths: {e}")
        return None, None, None

# Load data once at startup
df_prices, df_events, change_point_date = load_data()
if df_prices is None:
    print("Failed to load data. Exiting.")
    # In a real-world app, you might raise an exception or handle this more gracefully
    # For now, we'll just return a tuple of None values
    df_prices, df_events, change_point_date = (None, None, None)

# --- API Endpoints ---
def get_data():
    """
    Serves the Brent oil price time series data.
    """
    if df_prices is None:
        return jsonify({'error': 'Data not loaded'}), 500
        
    price_data = df_prices.reset_index().to_dict('records')
    
    return jsonify({
        'prices': price_data,
        'change_point_date': change_point_date.strftime('%Y-%m-%d') if change_point_date else None,
    })

def get_events():
    """
    Serves the key historical events data.
    """
    if df_events is None:
        return jsonify({'error': 'Data not loaded'}), 500
        
    event_data = df_events.to_dict('records')
    
    return jsonify(event_data)
