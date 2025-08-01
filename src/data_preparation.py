import pandas as pd
import numpy as np
import os

def prepare_data(raw_data_path, events_data_path):
    """
    Loads raw Brent oil price data and key events, then cleans and merges them.

    Args:
        raw_data_path (str): The file path to the raw Brent oil price CSV.
        events_data_path (str): The file path to the key events CSV.

    Returns:
        tuple: A tuple containing two pandas DataFrames:
               - The cleaned time series of Brent oil prices.
               - The processed key events data.
    """
    print("Starting data preparation...")
    
    # --- 1. Load Raw Data ---
    try:
        df_prices = pd.read_csv(raw_data_path)
        df_events = pd.read_csv(events_data_path)
    except FileNotFoundError as e:
        print(f"Error: A file was not found. Please check your paths: {e}")
        return None, None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None, None

    # --- 2. Clean and Prepare Price Data ---
    # Convert 'Date' column to datetime objects
    # The format is inferred as '%b %d, %Y' based on the error message 'Apr 22, 2020'
    df_prices['Date'] = pd.to_datetime(df_prices['Date'], format='mixed')
    
    # Handle dates that are in the future due to the '%y' format
    # This assumes all data is from the past.
    current_year = pd.to_datetime('today').year
    df_prices['Date'] = df_prices['Date'].apply(
        lambda x: x - pd.DateOffset(years=100) if x.year > current_year else x
    )

    # Sort the DataFrame by date to ensure the time series is in order
    df_prices = df_prices.sort_values('Date').reset_index(drop=True)
    
    # Set the 'Date' column as the DataFrame index
    df_prices.set_index('Date', inplace=True)
    
    # Resample the daily data to a monthly frequency.
    # We use a mean for the price to get a representative monthly value.
    df_prices_monthly = df_prices['Price'].resample('MS').mean().to_frame()
    
    # Fill any missing values using forward fill, then back fill to handle
    # any NaNs at the beginning of the series.
    df_prices_monthly = df_prices_monthly.ffill()
    df_prices_monthly = df_prices_monthly.bfill()
    
    print("Price data prepared successfully.")

    # --- 3. Clean and Prepare Events Data ---
    # Convert 'Date' column to datetime objects
    df_events['Date'] = pd.to_datetime(df_events['Date'], format='%Y-%m-%d', errors='coerce')
    
    # Ensure the events are also sorted by date
    df_events = df_events.sort_values('Date').reset_index(drop=True)
    
    print("Events data prepared successfully.")
    
    print("Data preparation complete.")

    return df_prices_monthly, df_events

if __name__ == '__main__':
    # Define file paths relative to the script's location
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, '..'))

    raw_file = os.path.join(project_root, 'data', 'raw', 'brent_oil_prices.csv')
    events_file = os.path.join(project_root, 'data', 'events', 'key_events.csv')

    # Run the preparation function
    prices_df, events_df = prepare_data(raw_file, events_file)

    if prices_df is not None and events_df is not None:
        print("\n--- Processed Price Data Head ---")
        print(prices_df.head())
        print("\n--- Processed Events Data Head ---")
        print(events_df.head())
        
        # Save the processed data to the designated path
        processed_dir = os.path.join(project_root, 'data', 'processed')
        os.makedirs(processed_dir, exist_ok=True)
        processed_data_path = os.path.join(processed_dir, 'processed_data.csv')
        prices_df.to_csv(processed_data_path)
        print(f"\nProcessed price data saved to {processed_data_path}")
