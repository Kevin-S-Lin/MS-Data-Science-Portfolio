# Optimizations and Algorithms

## Synthetic Trials
- **Purpose:** Demonstrate Bayesian updating, Monte Carlo simulation, and geometric intuition in high dimensions through short reproducible experiments.
- **Notebook:** `Optimizations and Algorithms/Synthetic Trials.ipynb`
- **Tasks / Methods:**
  - **Bayesian Categorical (3‑sided die):** analytic Dirichlet posterior vs. MLE; verify with PyMC Dirichlet + Categorical sampling and ArviZ plots.
  - **High‑Dim Norms:** draw 10,000 samples from N(0,I) in 10D and 100D; plot Euclidean norm histograms and report mean distance (illustrates concentration of measure ≈ √d).
  - **Beta‑Binomial (coin flips):** posterior Beta(1+heads,1+tails) for 120/200; sample with PyMC and visualize posterior.
  - **Random Walk Exit Time:** simulate 10,000 symmetric random walks starting at 0; record steps to exit [-10,10]; compute average exit time.
- **Tech stack:** Python, NumPy, Matplotlib, PyMC (v5), ArviZ.
- **Deliverables:** analytic solutions, MCMC traces/posterior plots, histograms, average statistics, and simulation code in the notebook.
- **How to run:** open the notebook and execute cells (requires a Python env with `pymc`, `arviz`, `numpy`, `matplotlib`). Example:
  - python -m pip install pymc arviz numpy matplotlib
  - open `Optimizations and Algorithms/Synthetic Trials.ipynb` and run all cells.
- **Expected insights:** confirms Bayesian analytic vs. sampled posteriors, shows √d scaling of distances in high dimensions, and yields empirical estimate of random‑walk exit time (order a² for interval radius a).

## Entropy & Kullback-Leibler Divergence
- **Purpose**: Teach and demonstrate information‑theoretic concepts—entropy, maximum entropy, Kullback–Leibler divergence, and source coding—via analytic work and Python examples.
- **Tasks / Methods**:
  - Compute entropy for a 4‑sided die (analytic and Python).
  - Find the distribution that maximizes entropy for a 4‑symbol source and compute its value.
  - Compute KL divergence between two coin distributions (both directions) using `scipy.stats.entropy`.
  - Compute source entropy for a 5‑symbol source and build a Huffman code; calculate average bits/symbol and compare to entropy.
- **Tech stack**: Python (math, scipy.stats), Jupyter notebook, Matplotlib (if plotting needed).
- **Deliverables**: worked analytic solutions, runnable Python cells that print entropy/KL values, a sample Huffman code and average bit-length calculation.
- **How to run**:
  - Ensure Python env with `scipy` installed:  
    pip install scipy
  - Open the notebook and run all cells.
- **Key takeaways**:
  - Entropy quantifies average information (example: die entropy = 1.75 bits).
  - Uniform distribution maximizes entropy for a fixed alphabet.
  - KL divergence is asymmetric and measures how one distribution diverges from another.
  - Huffman coding approaches entropy but uses integer bit lengths; average code length should be ≥ entropy and close for skewed distributions.

## Bayesian vs Frequentist Logistic Regression
- **Purpose**: Explore and model the Pima Indians diabetes dataset with frequentist and Bayesian logistic regression.
- **Dataset**: Loads diabetes.csv (unzips archive.zip), X = first 8 features, y = Outcome.
- **Preprocessing**: Minimal — reads CSV into a DataFrame; no feature scaling or train/test split in the notebook.
- **Frequentist model**: Fits sklearn.linear_model.LogisticRegression (max_iter=1000), prints intercept and coefficients.
- **Bayesian model**: Builds a PyMC model with Normal priors (w0–w8, mu=0, sigma=100), linear predictor linreg, p_outcome = pm.invlogit(linreg), and Bernoulli likelihood.
- **Inference**: Computes MAP via pm.find_MAP() and draws MCMC samples with pm.sample(400, tune=1000, step=pm.Metropolis()); visualizes posteriors with arviz.plot_posterior.
- **Interpretation provided**: Explains priors, likelihood, meaning of pm.invlogit, map_est, and concludes Diabetes Pedigree Function has comparatively large coefficient in posterior summaries.
- **Notes / caveats**: No held-out evaluation or preprocessing; uses Metropolis sampler (compute/convergence considerations); PyMC API adjusted for newer pymc version (sigma keyword).