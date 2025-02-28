# USA Enhanced Forecast Rationale

## Overview

This document explains the rationale behind the enhanced forecast model for USA travel queries. The enhanced model incorporates statistical and machine learning approaches to complement the original factor-based model, providing additional insights and validation.

## Enhanced Model Approach

The enhanced model adds three key capabilities to the original factor-based approach:

1. **Anomaly Detection**: Identifies and adjusts outliers in historical data
2. **Time Series Forecasting**: Implements ARIMA models alongside the factor-based approach
3. **Bayesian Forecasting**: Incorporates uncertainty and confidence intervals in predictions

## Methodology

### Anomaly Detection

The model uses Z-scores to identify outliers in the historical data:
- Data points with Z-scores > 3.0 (more than 3 standard deviations from the mean) are flagged as outliers
- Outliers are adjusted using a median window approach, where each outlier is replaced with the median of surrounding values
- This preprocessing step improves forecast accuracy by removing anomalous data points that could skew the model

### ARIMA Model

The enhanced model implements an ARIMA (AutoRegressive Integrated Moving Average) model:
- ARIMA(1,1,1) parameters were selected based on the characteristics of the time series
- The model captures temporal patterns and autocorrelations in the data
- It provides a statistical baseline forecast that complements the factor-based approach

### Confidence Intervals

The ARIMA model provides 95% confidence intervals for the forecasts:
- These intervals quantify the uncertainty in the predictions
- Wider intervals indicate greater uncertainty
- The intervals widen as the forecast extends further into the future

## Key Findings

### Forecast Comparison

The enhanced model provides four different forecast scenarios for 2025:

1. **Conservative Scenario**: Average of 68.36 indexed queries per month, representing an 8.7% year-over-year growth from 2024. This scenario applies a 5% base growth factor with conservative multipliers for media effectiveness, flight search correlation, and brand health.

2. **Moderate Scenario**: Average of 74.46 indexed queries per month, representing an 18.4% year-over-year growth from 2024. This scenario applies a 10% base growth factor with moderate multipliers.

3. **Ambitious Scenario**: Average of 80.57 indexed queries per month, representing a 28.1% year-over-year growth from 2024. This scenario applies a 15% base growth factor with aggressive multipliers.

4. **ARIMA Forecast**: Average of 65.27 indexed queries per month, representing a 14.1% year-over-year growth from 2024. This is a statistical projection based on historical patterns.

The factor-based scenarios (Conservative, Moderate, Ambitious) incorporate domain knowledge about seasonality, media impressions, flight searches, and brand health metrics. In contrast, the ARIMA model relies solely on historical patterns in the time series data. This difference highlights the complementary nature of the two approaches.

Interestingly, the ARIMA forecast falls between the Conservative and Moderate scenarios in terms of overall growth, suggesting that a moderate growth projection is most aligned with historical patterns.

### Monthly Variations

The different forecast scenarios show interesting monthly patterns:

**ARIMA Model**:
- For July, the ARIMA forecast (65.27) is significantly lower than the 2024 value (98.08), suggesting that the 2024 July spike may be an anomaly
- For October, the ARIMA forecast (65.27) is also lower than the 2024 value (86.02), indicating another potential anomaly
- For most other months, the ARIMA forecast suggests growth over 2024 values, with particularly strong growth in February (44.5%) and April (47.4%)

**Factor-Based Models**:
- All factor-based scenarios show strong growth in July and October, with the Ambitious scenario projecting increases of 68.3% and 81.5% respectively
- February and April show decreases in the Conservative scenario (-15.1% and -12.4%) and mixed results in the Moderate scenario
- The seasonality index has a strong influence on the factor-based forecasts, with higher values for July (1.34) and October (1.50) driving the projections for these months

### Confidence Intervals

The 95% confidence intervals for the ARIMA forecasts provide valuable insights into forecast uncertainty:
- January 2025: 43.09 to 87.34 (range width: 44.25)
- December 2025: 32.82 to 97.72 (range width: 64.90)

The widening confidence intervals throughout the year reflect increasing uncertainty as the forecast extends further into the future. This information can be valuable for risk assessment and scenario planning.

### Seasonality Index

The calculated seasonality index based on 2023-2024 data shows significant monthly variations:
- Highest seasonality: October (1.50), July (1.34)
- Lowest seasonality: February (0.77), April (0.79)

This seasonality pattern differs from what might be expected for travel queries, with October showing the highest seasonality rather than traditional summer months. This could reflect specific market characteristics for USA travel to this destination.

## Implications for Strategy

The enhanced model provides several strategic implications:

1. **Growth Projections**: The four scenarios provide a range of growth projections from 8.7% (Conservative) to 28.1% (Ambitious), with the ARIMA forecast (14.1%) falling between the Conservative and Moderate scenarios. This range provides flexibility in planning.

2. **Risk Assessment**: The confidence intervals for the ARIMA forecast provide a quantitative measure of uncertainty, which can inform risk management strategies. The factor-based scenarios offer additional perspectives on potential outcomes.

3. **Seasonal Adjustments**: The factor-based scenarios incorporate seasonality, suggesting higher resource allocation for peak months (July, October), while the ARIMA forecast suggests a more even distribution throughout the year.

4. **Media Planning**: The Media Multiplier in the factor-based models quantifies the impact of planned media impressions on travel queries, which can inform media budget allocation decisions.

5. **Scenario Planning**: The multiple forecast scenarios enable robust scenario planning, allowing stakeholders to prepare for different potential outcomes.

## Recommendations

Based on the enhanced model results, we recommend:

1. **Use the Moderate scenario as the primary forecast** for planning purposes, as it aligns closely with the ARIMA forecast and represents a balanced view of growth potential.

2. **Consider the Conservative scenario for risk management** and the Ambitious scenario for stretch goals and opportunity planning.

3. **Consider the confidence intervals when making commitments** that depend on forecast accuracy. For high-stakes decisions, consider the lower bound of the confidence interval as a worst-case scenario.

4. **Allocate resources according to the seasonality pattern** identified in the factor-based models, with increased focus on July and October.

5. **Adjust media investments** based on the Media Multiplier calculations, potentially increasing investments in months where the multiplier shows higher effectiveness.

6. **Monitor actual performance against all forecast scenarios** to continuously improve the models. If actual performance consistently aligns with one scenario over others, adjust planning accordingly.

7. **Allocate a portion of the budget as a contingency** to address the uncertainty quantified by the confidence intervals, particularly for the latter half of the year where uncertainty is greatest.

## Conclusion

The enhanced forecast model provides valuable insights into the expected travel queries for the USA market in 2025. By incorporating multiple approaches—factor-based scenarios, ARIMA time series forecasting, anomaly detection, and confidence intervals—the enhanced model offers a comprehensive view of potential outcomes.

The factor-based scenarios provide growth projections ranging from 8.7% to 28.1%, with the ARIMA forecast of 14.1% falling between the Conservative and Moderate scenarios. This alignment suggests that a moderate growth projection is most consistent with historical patterns.

The seasonality index and monthly variations highlight the importance of July and October as peak months, while the confidence intervals quantify the increasing uncertainty in long-term projections. Together, these insights provide a robust foundation for strategic planning, resource allocation, and risk management for the USA market in 2025.
