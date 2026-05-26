# Time Series Analysis Projects

## Fundamentals & Moving Averages


* **Key Concepts:** Autoregression (AR) simulation and moving average filters.
* **Exercises:**
* Generates $n=100$ observations from an AR(2) process ($x_t = -0.9x_{t-2} + w_t$).
* Applies a 4-point moving average filter ($v_t$) to analyze how smoothing affects the behavior of the original series.



## Variance & Portfolio Diversification

* **Key Concepts:** Financial time series and risk management.
* **Exercises:**
* Demonstrates the mathematical benefits of diversification using variance-covariance inequalities.
* Explores why splitting investments between two non-perfectly correlated assets reduces the total standard deviation of a portfolio.



## Operators & Stationary Processes

* **Key Concepts:** Backshift operators and autocovariance functions.
* **Exercises:**
* Calculates the autocovariance and autocorrelation for a stationary moving average process ($v_t = \frac{1}{4}w_{t-1} + \frac{1}{2}w_t + \frac{1}{4}w_{t+1}$).
* Analyzes the equivalence and differences between various backshift operator applications, such as $(1-B^{-1})$ vs. $-(1-B)$.



## ARMA Modeling

* **Key Concepts:** Moving Average (MA) processes and the Autocorrelation Function (ACF).
* **Exercises:**
* Proves theoretical bounds for the autocorrelation of an MA(1) process ($|\rho_x(1)| \leq 0.5$).
* Simulates MA(1) processes to observe how varying the parameter $\theta$ impacts the ACF.



## Sunspot Activity & ARIMA

* **Key Concepts:** Real-world data analysis and ARIMA forecasting.
* **Exercises:**
* Analyzes historical sunspot data using `statsmodels` to identify cyclic trends and seasonality.
* Fits an AR(2) model and evaluates its performance using the Bayesian Information Criterion (BIC).



## Fourier Analysis & Signal Generation

* **Key Concepts:** Spectral analysis and frequency domain modeling.
* **Exercises:**
* Simulates complex signals by combining multiple cosine waves with varying frequencies and phases.
* Replicates classic Fourier analysis examples to distinguish periodic signals from background noise.



## STL Decomposition & Exponential Smoothing

* **Key Concepts:** Robust STL and Holt-Winters Method.
* **Exercises:**
* Performs Seasonal-Trend decomposition using LOESS (STL) on sunspot data.
* Compares Robust vs. Non-robust STL methods and applies Holt-Winters exponential smoothing for multi-step forecasting.



## Advanced Forecasting: Prophet Model

* **Key Concepts:** Prophet forecasting and external trends.
* **Exercises:**
* Implements the Facebook Prophet model to forecast mortgage trends.
* Critical evaluation of model performance, noting where the Prophet model fails to capture sudden upward shifts in data.



## SIR Epidemic Modeling & VAR

* **Key Concepts:** Epidemiological models and Vector Autoregression (VAR).
* **Exercises:**
* Mathematically proves outbreak conditions for the SIR model ($R_0 < 1$) and calculates required vaccination fractions to prevent epidemics.
* Uses a VAR(1) model to analyze multivariate time series relationships.



## Unit Root Testing & Volatility (ARCH/GARCH)

* **Key Concepts:** Stationarity testing and conditional heteroskedasticity.
* **Exercises:**
* Applies Augmented Dickey-Fuller (ADF) and KPSS tests to AR(1) processes with high persistence ($\phi=0.98$).
* Models volatility in financial data using ARCH(1), ARCH(2), and GARCH(1,1) models, ranking them by BIC scores.