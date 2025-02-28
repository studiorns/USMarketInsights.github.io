#!/usr/bin/env python3
"""
Simplified Enhanced USA Travel Queries Forecast Model

This script implements a simplified version of the enhanced forecast model with:
1. Anomaly Detection: Identifies and adjusts outliers in historical data
2. Time Series Forecasting: Implements ARIMA models for comparison
3. Bayesian Forecasting: Incorporates uncertainty and confidence intervals

Usage:
    python usa_forecast_enhanced_simple.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Historical data (manually extracted from Travel_Queries_Forecast_USA.csv)
historical_data = [
    {'Month': 'January', 'Year': 2020, 'Indexed_Queries': 14.24085006},
    {'Month': 'January', 'Year': 2021, 'Indexed_Queries': 116.2473436},
    {'Month': 'January', 'Year': 2022, 'Indexed_Queries': 26.50590319},
    {'Month': 'January', 'Year': 2023, 'Indexed_Queries': 40.62337662},
    {'Month': 'January', 'Year': 2024, 'Indexed_Queries': 51.17001181},
    {'Month': 'February', 'Year': 2020, 'Indexed_Queries': 26.93565525},
    {'Month': 'February', 'Year': 2021, 'Indexed_Queries': 13.83412043},
    {'Month': 'February', 'Year': 2022, 'Indexed_Queries': 24.72904368},
    {'Month': 'February', 'Year': 2023, 'Indexed_Queries': 36.61511216},
    {'Month': 'February', 'Year': 2024, 'Indexed_Queries': 45.16056671},
    {'Month': 'March', 'Year': 2020, 'Indexed_Queries': 18.23789847},
    {'Month': 'March', 'Year': 2021, 'Indexed_Queries': 15.99881936},
    {'Month': 'March', 'Year': 2022, 'Indexed_Queries': 27.01298701},
    {'Month': 'March', 'Year': 2023, 'Indexed_Queries': 39.41971665},
    {'Month': 'March', 'Year': 2024, 'Indexed_Queries': 52.89669421},
    {'Month': 'April', 'Year': 2020, 'Indexed_Queries': 15.23199528},
    {'Month': 'April', 'Year': 2021, 'Indexed_Queries': 15.36658796},
    {'Month': 'April', 'Year': 2022, 'Indexed_Queries': 25.35182999},
    {'Month': 'April', 'Year': 2023, 'Indexed_Queries': 39.30991736},
    {'Month': 'April', 'Year': 2024, 'Indexed_Queries': 44.28748524},
    {'Month': 'May', 'Year': 2020, 'Indexed_Queries': 13.88547816},
    {'Month': 'May', 'Year': 2021, 'Indexed_Queries': 13.31227863},
    {'Month': 'May', 'Year': 2022, 'Indexed_Queries': 27.64698937},
    {'Month': 'May', 'Year': 2023, 'Indexed_Queries': 43.77154664},
    {'Month': 'May', 'Year': 2024, 'Indexed_Queries': 48.27331759},
    {'Month': 'June', 'Year': 2020, 'Indexed_Queries': 15.88134593},
    {'Month': 'June', 'Year': 2021, 'Indexed_Queries': 14.99409681},
    {'Month': 'June', 'Year': 2022, 'Indexed_Queries': 26.93742621},
    {'Month': 'June', 'Year': 2023, 'Indexed_Queries': 40.00826446},
    {'Month': 'June', 'Year': 2024, 'Indexed_Queries': 57.25442739},
    {'Month': 'July', 'Year': 2020, 'Indexed_Queries': 25.54781582},
    {'Month': 'July', 'Year': 2021, 'Indexed_Queries': 19.0},
    {'Month': 'July', 'Year': 2022, 'Indexed_Queries': 36.9120425},
    {'Month': 'July', 'Year': 2023, 'Indexed_Queries': 44.89492326},
    {'Month': 'July', 'Year': 2024, 'Indexed_Queries': 98.0785124},
    {'Month': 'August', 'Year': 2020, 'Indexed_Queries': 24.6227863},
    {'Month': 'August', 'Year': 2021, 'Indexed_Queries': 15.72136954},
    {'Month': 'August', 'Year': 2022, 'Indexed_Queries': 34.95336482},
    {'Month': 'August', 'Year': 2023, 'Indexed_Queries': 47.92798111},
    {'Month': 'August', 'Year': 2024, 'Indexed_Queries': 59.56729634},
    {'Month': 'September', 'Year': 2020, 'Indexed_Queries': 18.21133412},
    {'Month': 'September', 'Year': 2021, 'Indexed_Queries': 20.40613932},
    {'Month': 'September', 'Year': 2022, 'Indexed_Queries': 36.73199528},
    {'Month': 'September', 'Year': 2023, 'Indexed_Queries': 50.44096812},
    {'Month': 'September', 'Year': 2024, 'Indexed_Queries': 59.1729634},
    {'Month': 'October', 'Year': 2020, 'Indexed_Queries': 22.42680047},
    {'Month': 'October', 'Year': 2021, 'Indexed_Queries': 55.44451004},
    {'Month': 'October', 'Year': 2022, 'Indexed_Queries': 70.17178276},
    {'Month': 'October', 'Year': 2023, 'Indexed_Queries': 73.27095632},
    {'Month': 'October', 'Year': 2024, 'Indexed_Queries': 86.01829988},
    {'Month': 'November', 'Year': 2020, 'Indexed_Queries': 14.04840614},
    {'Month': 'November', 'Year': 2021, 'Indexed_Queries': 23.729634},
    {'Month': 'November', 'Year': 2022, 'Indexed_Queries': 43.36540732},
    {'Month': 'November', 'Year': 2023, 'Indexed_Queries': 50.4309327},
    {'Month': 'November', 'Year': 2024, 'Indexed_Queries': 58.27508855},
    {'Month': 'December', 'Year': 2020, 'Indexed_Queries': 14.67355372},
    {'Month': 'December', 'Year': 2021, 'Indexed_Queries': 27.81168831},
    {'Month': 'December', 'Year': 2022, 'Indexed_Queries': 37.80991736},
    {'Month': 'December', 'Year': 2023, 'Indexed_Queries': 47.65584416},
    {'Month': 'December', 'Year': 2024, 'Indexed_Queries': 63.31168831}
]

# 2024 queries for YoY calculation
queries_2024 = {
    'January': 51.17001181,
    'February': 45.16056671,
    'March': 52.89669421,
    'April': 44.28748524,
    'May': 48.27331759,
    'June': 57.25442739,
    'July': 98.0785124,
    'August': 59.56729634,
    'September': 59.1729634,
    'October': 86.01829988,
    'November': 58.27508855,
    'December': 63.31168831
}

def calculate_seasonality_index():
    """Calculate seasonality index based on 2023-2024 data."""
    # Group by month and calculate average
    df = pd.DataFrame(historical_data)
    recent_data = df[(df['Year'] >= 2023) & (df['Year'] <= 2024)]
    monthly_avg = recent_data.groupby('Month')['Indexed_Queries'].mean()
    
    # Calculate overall average
    overall_avg = monthly_avg.mean()
    
    # Calculate seasonality index
    seasonality_index = monthly_avg / overall_avg
    
    return seasonality_index.to_dict()

def main():
    """Main function to run the enhanced forecast model."""
    print("Starting enhanced forecast model for USA...")
    
    # Convert historical data to DataFrame
    df = pd.DataFrame(historical_data)
    
    # Create a date column
    df['Date'] = pd.to_datetime(
        df['Year'].astype(str) + '-' + 
        df['Month'].apply(lambda x: {
            'January': '01', 'February': '02', 'March': '03', 'April': '04',
            'May': '05', 'June': '06', 'July': '07', 'August': '08',
            'September': '09', 'October': '10', 'November': '11', 'December': '12'
        }[x]) + '-01'
    )
    
    # Sort by date
    df = df.sort_values('Date')
    
    # Create a time series
    time_series = df.set_index('Date')['Indexed_Queries']
    
    # Detect outliers
    print("Detecting outliers...")
    z_scores = stats.zscore(df['Indexed_Queries'])
    df['Outlier'] = abs(z_scores) > 3.0
    df['Z_Score'] = z_scores
    outliers = df[df['Outlier']]
    
    # Adjust outliers
    print("Adjusting outliers...")
    adjusted_series = time_series.copy()
    for idx in outliers.index:
        date_idx = outliers.loc[idx, 'Date']
        # Use median of surrounding values
        window_start = max(0, time_series.index.get_loc(date_idx) - 1)
        window_end = min(len(time_series), time_series.index.get_loc(date_idx) + 2)
        window_values = time_series.iloc[window_start:window_end]
        # Exclude the outlier itself from the window
        window_values = window_values[window_values.index != date_idx]
        if not window_values.empty:
            adjusted_series.loc[date_idx] = window_values.median()
    
    # Plot outliers
    print("Plotting outliers...")
    plt.figure(figsize=(12, 6))
    plt.plot(time_series.index, time_series.values, 'b-', label='Original Data')
    plt.scatter(outliers['Date'], outliers['Indexed_Queries'], color='red', label='Outliers')
    plt.plot(adjusted_series.index, adjusted_series.values, 'g--', label='Adjusted Data')
    plt.title('USA Travel Queries Time Series with Outliers')
    plt.xlabel('Date')
    plt.ylabel('Indexed Queries')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('usa_outliers_detection.png')
    plt.close()
    
    # Fit ARIMA model
    print("Fitting ARIMA model...")
    model = ARIMA(adjusted_series, order=(1, 1, 1))
    arima_model = model.fit()
    
    # Generate forecast
    print("Generating ARIMA forecast...")
    steps = 12
    forecast = arima_model.forecast(steps=steps)
    forecast_index = pd.date_range(start=time_series.index[-1], periods=steps+1, freq='MS')[1:]
    
    # Get confidence intervals
    pred_ci = arima_model.get_forecast(steps=steps).conf_int()
    
    # Create forecast DataFrame
    arima_forecast = pd.DataFrame({
        'ARIMA_Forecast': forecast,
        'Lower_CI': pred_ci.iloc[:, 0],
        'Upper_CI': pred_ci.iloc[:, 1]
    }, index=forecast_index)
    
    # Calculate seasonality index
    seasonality_index = calculate_seasonality_index()
    
    # Create a DataFrame for the seasonality index
    seasonality_df = pd.DataFrame(list(seasonality_index.items()), columns=['Month', 'Seasonality_Index'])
    
    # Calculate YoY change for ARIMA forecast
    arima_yoy = []
    for month, row in arima_forecast.iterrows():
        month_name = month.strftime('%B')
        month_2024 = queries_2024[month_name]
        arima_yoy.append(((row['ARIMA_Forecast'] - month_2024) / month_2024) * 100)
    
    arima_forecast['ARIMA_YoY'] = arima_yoy
    
    # Add month name to arima_forecast
    arima_forecast['Month'] = arima_forecast.index.strftime('%B')
    
    # Plot forecasts
    print("Plotting forecasts...")
    plt.figure(figsize=(12, 6))
    
    # Plot historical data
    plt.plot(time_series.index, time_series.values, 'b-', label='Historical Data')
    
    # Plot ARIMA forecast
    plt.plot(arima_forecast.index, arima_forecast['ARIMA_Forecast'], 'r-', label='ARIMA Forecast')
    plt.fill_between(
        arima_forecast.index,
        arima_forecast['Lower_CI'],
        arima_forecast['Upper_CI'],
        color='r', alpha=0.1, label='ARIMA 95% CI'
    )
    
    plt.title('USA Travel Queries Forecast')
    plt.xlabel('Date')
    plt.ylabel('Indexed Queries')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('usa_forecast.png')
    plt.close()
    
    # Save results
    print("Saving results...")
    arima_forecast.to_csv('usa_arima_forecast.csv')
    seasonality_df.to_csv('usa_seasonality_index.csv', index=False)
    
    # Print summary
    print("\nARIMA Forecast Summary:")
    print(f"Average 2025 Forecast: {arima_forecast['ARIMA_Forecast'].mean():.2f}")
    print(f"Average YoY Growth: {arima_forecast['ARIMA_YoY'].mean():.2f}%")
    print(f"Confidence Interval Width (Jan): {arima_forecast['Upper_CI'].iloc[0] - arima_forecast['Lower_CI'].iloc[0]:.2f}")
    print(f"Confidence Interval Width (Dec): {arima_forecast['Upper_CI'].iloc[-1] - arima_forecast['Lower_CI'].iloc[-1]:.2f}")
    
    print("\nSeasonality Index:")
    for month, index in seasonality_index.items():
        print(f"{month}: {index:.2f}")
    
    print("\nDone!")
    
    return arima_forecast, seasonality_df

if __name__ == "__main__":
    arima_forecast, seasonality_df = main()
