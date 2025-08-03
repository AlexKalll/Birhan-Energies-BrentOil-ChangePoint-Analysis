import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
import os

def analyze_and_visualize(data_path, events_path, inference_data, output_dir):
    """
    Analyzes the change point model's results and creates visualizations.

    This function plots the time series data, the model's inferred change point,
    and compares it with the key historical events.

    Args:
        data_path (str): The file path to the processed time series data.
        events_path (str): The file path to the key events data.
        inference_data (arviz.InferenceData): The posterior samples from the fitted model.
        output_dir (str): The directory to save the plots.
    """
    print("Starting analysis and visualization...")
    
    try:
        # Load the processed data
        df_prices = pd.read_csv(data_path, index_col='Date', parse_dates=True)
        df_events = pd.read_csv(events_path, parse_dates=['Date'])
    except FileNotFoundError as e:
        print(f"Error: A file was not found. Please check your paths: {e}")
        return
    
    # Get the posterior samples for the change point location (tau)
    # The `idxmax` method gives us the most probable index
    posterior_tau = inference_data.posterior['tau'].values.flatten()
    most_probable_tau = np.median(posterior_tau).astype(int)
    
    # Get the date corresponding to the most probable change point index
    change_point_date = df_prices.index[most_probable_tau]

    # Plotting the time series with the change point
    plt.figure(figsize=(15, 8))
    plt.plot(df_prices.index, df_prices['Price'], color='dodgerblue', label='Monthly Brent Oil Price')
    
    # Add a vertical line for the inferred change point
    plt.axvline(x=change_point_date, color='red', linestyle='--', linewidth=2, 
                label=f'Inferred Change Point: {change_point_date.strftime("%Y-%m")}')
    
    # Shade the posterior probability distribution for the change point
    ax = plt.gca()
    az.plot_dist(
        posterior_tau, 
        ax=ax, 
        hist_kwargs={"alpha": 0.3},
        label='Posterior of Change Point (tau)'
    )
    # Convert index to dates for x-axis
    x_ticks = [df_prices.index[int(t)] for t in ax.get_xticks() if t >= 0 and t < len(df_prices.index)]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([date.strftime('%Y-%m') for date in x_ticks], rotation=45, ha='right')

    # Add key events to the plot for comparison
    for date, event in zip(df_events['Date'], df_events['Event']):
        plt.axvline(x=date, color='darkgreen', linestyle=':', linewidth=1, alpha=0.7)
        plt.text(date, plt.gca().get_ylim()[1] * 0.95, event, rotation=90, va='top', ha='right', fontsize=8, color='darkgreen')
    
    plt.title('Brent Oil Prices with Inferred Change Point and Key Events', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend()
    plt.tight_layout()

    # Save the plot
    os.makedirs(output_dir, exist_ok=True)
    plot_path = os.path.join(output_dir, 'change_point_analysis.png')
    plt.savefig(plot_path)
    print(f"Analysis plot saved to {plot_path}")
    plt.show()

if __name__ == '__main__':
    # Define file paths relative to the script's location
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    processed_data_path = os.path.join(project_root, 'data', 'processed', 'processed_data.csv')
    events_file_path = os.path.join(project_root, 'data', 'events', 'key_events.csv')
    reports_output_dir = os.path.join(project_root, 'reports')
    
    # This is a placeholder for loading your saved inference data.
    # For this example, we'll assume the model has been run and the `inference_data`
    # object is available. In a real-world scenario, you would have saved it
    # from model.py (e.g., as a .nc file) and loaded it here.
    #
    # Example for demonstration:
    # inference_data = az.from_netcdf("path/to/trace.nc")
    
    # We will simulate the `inference_data` object based on your log output for demonstration.
    # In a real run, you would load the actual trace.
    print("Simulating loading inference data for demonstration...")
    # These are the values from your log output
    mean_tau = 214.140
    std_tau = 1.993
    
    # Create a small, simplified `InferenceData` object for plotting demonstration
    # This is not a substitute for saving and loading the real data
    tau_samples = np.random.normal(loc=mean_tau, scale=std_tau, size=1000).astype(int)
    simulated_posterior = {
        'tau': np.array([tau_samples])
    }
    simulated_inference_data = az.from_dict(posterior=simulated_posterior)
    
    # Now run the analysis
    analyze_and_visualize(processed_data_path, events_file_path, simulated_inference_data, reports_output_dir)
