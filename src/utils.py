import matplotlib.pyplot as plt
import pandas as pd

def plot_time_series_with_events(df_prices, df_events, title='Brent Oil Prices with Key Events', price_col='Price'):
    """
    Plots the Brent oil price time series and overlays key events.

    Args:
        df_prices (pd.DataFrame): DataFrame containing the time series of Brent oil prices.
                                  Expected to have a DatetimeIndex and a 'Price' column.
        df_events (pd.DataFrame): DataFrame containing key events.
                                  Expected to have a 'Date' column (datetime) and 'Event' column (str).
        title (str): Title of the plot.
        price_col (str): Name of the column in df_prices that contains the price data.
    """
    plt.figure(figsize=(15, 7))
    plt.plot(df_prices.index, df_prices[price_col], label='Brent Oil Price', color='blue')

    # Overlay events
    for index, row in df_events.iterrows():
        plt.axvline(pd.to_datetime(row['Date']), color='red', linestyle='--', lw=1, alpha=0.7)
        plt.text(pd.to_datetime(row['Date']), plt.gca().get_ylim()[1] * 0.95,
                 row['Event'], rotation=90, verticalalignment='top', fontsize=9, color='red')

    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()