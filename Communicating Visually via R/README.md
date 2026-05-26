# Communicating Visually via R

## The Impact of Government Intervention on COVID19 Deaths
**Summary**
- **Purpose:** Estimate which government non-pharmaceutical interventions (NPIs) most reliably reduced COVID-19 mortality using subnational panel data and fixed-effects regression.
- **Data Sources:** OxCGRT policy metrics, Johns Hopkins / Our World in Data death counts, World Bank population data — assembled at administrative_area_level_2 (state-level) daily panel.
- **Cleaning:** Strict NA filters (30% for deaths, 50% for any policy column), impute initial gaps as 0, LOCF for mid-series gaps, trim to Mar 2023 cutoff; creates diagnostics and before/after cleaning plots.
- **Uncertainty Handling:** Converts negative/inferred policy values to absolute, and creates per-location _Inferred_Count_ variables recording days with inferred values to control for measurement quality.
- **Feature Engineering:** 
  - Outcome Y = 7-day rolling avg deaths per 100k, then weekly difference (Y_Weekly_Change_Deaths) for stationarity.
  - Predictors X = each policy smoothed (7-day rolling mean) and lagged by 21 days (Lagged_Smoothed).
  - Control = Y lagged 7 days to handle autocorrelation.
- **Modeling:** Two-way fixed effects via `felm` (lfe package), clustered SEs by id. Two models: (1) four aggregated indices (advanced metrics) + inferred-count controls; (2) fourteen individual policy predictors + inferred-count controls.
- **Results (high level):** Advanced indices and many individual policies show highly significant p-values; notable strong effects for internal/international movement restrictions, gatherings restrictions, contact tracing, facial coverings, testing, vaccination policy; school_closing and cancel_events less significant.
- **Interpretation & Recommendations:** Prioritize movement controls early; reassess cost-effectiveness of school/event closures; pair information campaigns with compliance measures due to wide CIs.
- **Limitations & Future Work:** No explicit compliance/behavior data, lag choice fixed at 21 days (could vary by policy), possible remaining data-quality issues for some policies; suggests testing alternative lag structures, distributed-lag models, and incorporating compliance measures.
- **Reproducibility notes:** Code included for data import (COVID19 package), filtering, imputation, feature engineering, model fitting, and coefficient plotting (saved PNGs).

## Heart Disease Predictors
**Summary**
- **Purpose**: Identify key factors and combinations of features that predict heart disease from the Cleveland heart dataset.
- **Data & target**: Loads `processed.cleveland.data` with columns (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num). Target recoded to `heart_disease` (Present vs Absent).
- **Preprocessing**: Sets column names, converts many fields to factors (sex, cp, fbs, restecg, exang, thal), and creates a binary outcome from `num`.
- **Exploratory analysis**:
  - **Demographics**: risk increases with age; males show higher prevalence (peak ~60–70).
  - **Stress response**: `thalach` (max heart rate) tends to decline with age and is lower for those with disease.
  - **Cholesterol & BP**: higher `chol` tends to associate with disease; 2D density of `trestbps` vs `chol` shows broader spread for diseased patients.
  - **Chest pain & exercise angina**: asymptomatic chest pain and presence of exercise-induced angina strongly associate with disease.
  - **Direct severity measures**: `oldpeak` (ST depression) and `ca` (# blocked arteries) correlate; `oldpeak` increases with more blocked arteries.
- **Key predictors identified**: higher age, lower `thalach`, higher `chol`, asymptomatic chest pain (cp), exercise-induced angina (`exang`), larger `oldpeak`, and higher `ca`.
- **Visuals & outputs**: multiple ggplot figures (density, scatter, boxplot, violin) used to illustrate relationships; code is reproducible and prints data frames.
- **Conclusion**: A compact suite of variables (age, thalach, chol, cp, exang, ca, oldpeak) provides strong signals for predicting heart disease in this dataset; recommended for use in predictive models.

## PCA Tutorial and Explanation
- **Purpose:**  Tutorial and practical walkthrough of Principal Component Analysis (PCA) in R, with intuition, examples, visualizations, and a reusable cookbook.
- **Structure:** Intro → PCA intuition (PC1/PC2, variance vs. distance interpretations) → 2D demo (`iris`) → step-by-step PCA on `USArrests` (scale, `prcomp`, summary, loadings, scores) → scree & cumulative PVE plots → biplot interpretation → cookbook (plug-and-play code) → appendix with math (eigen decomposition, PVE formulas).
- **Key code/tools used:** `prcomp(..., scale. = TRUE)`, `summary()`, `pca_object$rotation`, `pca_object$x`, `biplot()`, `ggplot2` for loadings/scree/cumulative PVE plots.
- **Main recommendations:** always scale continuous features before PCA (unless units are identical), use scree/cumulative PVE to choose number of PCs, interpret loadings (signs are arbitrary), use biplots to relate observations and features.
- **Outputs / visuals:** scatter for correlated features, PC loading bar plots, scree plot, cumulative-PVE plot, biplot, and a concise PCA cookbook for reuse.
- **Reproducibility:** fully reproducible R code blocks included (data loading, `prcomp`, plotting); ready to adapt to other datasets.

## Iraq Violence-Related Mortality
- **Purpose**: assess epistemic uncertainty and communication quality in estimates of Iraq violence-related mortality (2002–2006).  
- **Data sources discussed**: Iraq Family Health Survey (IFHS) and Iraq Body Count (press-validated counts); authors compare and reconcile differing estimates.  
- **Main uncertainty sources**: biased household surveys (under-sampling in conflict zones), missing clusters/households, underreporting from household dissolution, and differences between survey and press-based counts.  
- **Methods for uncertainty quantification** (reported in the paper): jackknife, Monte Carlo simulations, sampling-error estimation, and adjustments for missing samples and population projections.  
- **Assumptions called out**: normal-distribution assumptions for migration and excess risk in missing clusters; stated levels of underreporting that could bias totals (e.g., possible 55%–70% undercount for some groups).  
- **How uncertainty is communicated**: numeric tables by region/demo, 95% confidence intervals, detailed meta-information on sampling/response rates, and explicit discussion of assumptions and limitations.  
- **Psychological/social effects noted**: public anxiety, policymaker indecision, and real-world harms when uncertainty or data are withheld (example referenced re: COVID nursing home reporting).  
- **Author’s appraisal**: The paper is judged methodologically careful and transparent—documenting biases, assumptions, CI ranges—thus providing a trustworthy, objective treatment of a sensitive topic.

## Facetting Graphs of NBA Advanced Stats
- **Purpose:** Explore NBA advanced stats over time and visualize player career trajectories using facetted line plots.  
- **Data:** Loads `nbaNew.csv`, cleans `PlayerSalary` to numeric, filters to players who've ever earned > $20,000,000.  
- **Visualizations:** 
  - **BPM:** Box Plus/Minus by season plotted and facetted by `PlayerName` (seasonal career progressions).  
  - **VORP:** Value Over Replacement Player by season facetted by `PlayerName` for a complementary view.  
- **Findings / Notes:** Highlights visible career spikes/trends (e.g., Derrick Rose, Hassan Whiteside, LeBron/Kobe/Michael Jordan); notes selection bias from filtering to high-salary players.  
- **Tools:** `tidyverse`, `ggplot2`, `facet_wrap` for per-player panels; basic data cleaning with `readr` and `dplyr`.

