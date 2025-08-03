import pymc as pm
import numpy as np
import pandas as pd
import os
import logging

# --- Setup Logging ---
def setup_logging():
    """
    Sets up a logger to write to a file in the logs directory.
    """
    # Define file paths relative to the script's location
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    logs_dir = os.path.join(project_root, 'logs')
    
    # Create the logs directory if it doesn't exist
    os.makedirs(logs_dir, exist_ok=True)
    
    log_file = os.path.join(logs_dir, 'modeling.log')
    
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # Create a file handler
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.INFO)
    
    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(file_handler)
    
    return logger

# Initialize the logger
logger = setup_logging()

def fit_model(data, num_samples=1000, num_chains=2):
    """
    Fits a Bayesian change point detection model to the time series data.

    This model assumes a single change point where the mean of the time series
    shifts. It uses a Poisson distribution for the change point location and
    Normal distributions for the pre-change and post-change means.

    Args:
        data (pd.DataFrame): A DataFrame with a 'Price' column, representing the
                             time series data.
        num_samples (int): The number of MCMC samples to draw.
        num_chains (int): The number of MCMC chains to run.

    Returns:
        arviz.InferenceData: An object containing the posterior samples and
                             model-related information.
    """
    logger.info("Starting Bayesian model fitting...")

    # Get the time series values as a numpy array
    time_series = data['Price'].values
    n = len(time_series)

    # Use a PyMC model context
    with pm.Model() as change_point_model:
        # Define the change point location prior
        # The change point can occur at any month index from 0 to n-1.
        # We use a DiscreteUniform distribution for a more robust prior.
        # A Beta-Binomial could also be used for more flexibility.
        tau = pm.DiscreteUniform("tau", lower=0, upper=n-1)

        # Define the prior distributions for the mean prices before and after the change point
        # The mean before the change point (mu1) is assumed to follow a Normal distribution
        # with a mean based on the entire time series data and a large standard deviation.
        mu1 = pm.Normal("mu1", mu=time_series.mean(), sigma=100)
        # Similarly, the mean after the change point (mu2) is defined.
        mu2 = pm.Normal("mu2", mu=time_series.mean(), sigma=100)

        # Define the prior for the standard deviation (sigma) of the observations
        # This parameter represents the noise in the data. We use a HalfNormal distribution
        # because standard deviation must be positive.
        sigma = pm.HalfNormal("sigma", sigma=10)

        # Create a function to determine the mean at each time step
        # This uses the `tau` (change point) variable.
        # pm.math.switch is used to conditionally select mu1 or mu2.
        # It's an efficient way to implement if/else logic within the PyMC model.
        idx = np.arange(n)
        mu = pm.math.switch(tau > idx, mu1, mu2)

        # Define the likelihood of the observed data
        # We assume the observed prices follow a Normal distribution
        # with the mean determined by the change point and the sigma.
        # This is the core of the model that links the priors to the data.
        observed_prices = pm.Normal(
            "observed_prices",
            mu=mu,
            sigma=sigma,
            observed=time_series,
        )

        # Perform MCMC sampling to infer the posterior distributions
        logger.info("Sampling from the posterior distribution...")
        trace = pm.sample(
            num_samples,
            tune=1000,
            cores=num_chains,
            random_seed=42,
            return_inferencedata=True
        )

    logger.info("Model fitting complete.")
    return trace

if __name__ == '__main__':
    # Define file paths relative to the script's location
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    processed_data_path = os.path.join(project_root, 'data', 'processed', 'processed_data.csv')
    
    try:
        # Load the processed data
        processed_df = pd.read_csv(processed_data_path, index_col='Date', parse_dates=True)
        
        # Fit the model
        inference_data = fit_model(processed_df)
        
        # Print a summary of the results
        logger.info("\n--- Model Inference Summary ---")
        # Log a summary of the trace
        logger.info(str(pm.summary(inference_data, hdi_prob=0.95)))

        # In a real-world scenario, you would save this `inference_data` object for later analysis.
        # For this example, we'll just log the summary.
        # For example: inference_data.to_netcdf("trace.nc")
        
    except FileNotFoundError:
        logger.error(f"Error: Processed data file not found at {processed_data_path}. Please run `data_preparation.py` first.")
    except Exception as e:
        logger.error(f"An error occurred during model fitting: {e}", exc_info=True)
