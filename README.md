# MS Data Science Portfolio
Showcase of accomplished projects.

## Machine Learning Projects
- **Comparing Classifiers**
    - Built LDA, Decision Tree, kNN, SVM on original features.
    - Applied PCA and re-tested kNN/SVM with 5, 10, 15 components.
- **MNIST Digit Classification**
    - Loaded IDX MNIST data into PyTorch.
    - Compared FFNN vs LeNet-5-style CNN (with custom pooling).
    - Ran multiple trials and reported average test accuracy.
- **Diabetes Classification**
    - Used LDA on key numeric health features.
    - Evaluated tree split quality via Gini impurity and information gain.
- **Pizza Brand Classification (Margin Perceptrons)**
    - Trained one-vs-one linear margin perceptrons: A/B, A/C, B/C.
    - Computed geometric margins.
    - Combined pairwise models with majority-vote fusion for multiclass prediction.
- **Pizza PCA Practice**
    - Computed mean, covariance/scatter, eigenpairs.
    - Projected/reconstructed samples with top 2 PCs.
    - Repeated after z-score standardization.
- **Gradient Descent Visualization**
    - Optimized a 2D objective and plotted iterate paths.
    - Compared exact line search vs backtracking.
    - Repeated under a second matrix setup.
- **Backpropagation From Scratch**
    - Implemented a 2–2–1 ReLU network manually.
    - Performed forward/backward passes and gradient updates.
    - Tracked and plotted loss over 50 iterations.
- **Ensemble Classification (Bagging)**
    - Trained 50 bootstrapped neural nets on moonDataset.
    - Plotted individual model error distribution.
    - Built ensembles (5/10/15/20) and showed error vs ensemble size.
- **Autoencoders**
    - Trained linear and ReLU autoencoders on Pizza features.
    - Swept hidden size (h=1..6), plotted MSE vs (h).
    - Linked optimal linear autoencoder MSE to discarded singular values.
- **Clustering + EM**
    - Visualized labeled 2D clusters.
    - Ran K-means for (k=2..7), selected (k=4) via silhouette (Euclidean/Manhattan).
    - Implemented GMM-EM (E/M/log-likelihood), estimated (\pi_k,\mu_k,\Sigma_k), and plotted density contours.

## Deep Learning Projects
- **Multilayer Perceptron**
    - Pima diabetes classifier (Keras MLP). Two parts — single-run training (150 epochs, batch=10) and hyperparameter grid search (optimizers, inits, epochs, batch_size) via KerasClassifier + GridSearchCV.
- **Boston Housing — MLP to predict MEDV**
    - compares network depth effects on convergence and error.
- **IMDB Sentiment Analysis**
    - baseline models vs CNNs using word embeddings to classify reviews.
- **LSTM Alphabet Sequence Prediction**
    - character-level LSTM that predicts next letter (sequence modeling demo).
- **MNIST Digit GAN**
    - GAN (Generator vs Discriminator) trained to synthesize handwritten digits.

## Optimizations and Algorithms
- **Synthetic Trials**
  - Purpose: Bayesian updating, Monte Carlo, and high‑D geometry demos.
- **Entropy & Kullback–Leibler Divergence**
  - Purpose: Compute/illustrate entropy, max‑entropy, KL divergence, and Huffman coding.
- **Bayesian vs Frequentist Logistic Regression**
  - Purpose: Compare sklearn logistic regression and a PyMC Bayesian logistic model on the Pima diabetes dataset.

## Communicating via Visuals and Graphs in R
- **The Impact of Government Intervention on COVID19 Deaths**
    - Panel fixed‑effects analysis of OxCGRT policies vs weekly change in deaths; strict NA filtering, imputation, 7‑day smoothing, 21‑day policy lag, inferred‑count uncertainty controls, `felm` models with clustered SEs; recommends prioritizing movement restrictions.
- **Heart Disease Predictors**
    - Cleveland dataset EDA; preprocesses/categorizes variables and identifies strong predictors (age, low `thalach`, high `chol`, `cp`, `exang`, `ca`, `oldpeak`) with ggplot visuals.
- **PCA Tutorial and Explanation**
    - Practical PCA walkthrough (`iris`, `USArrests`), scaling, `prcomp`, loadings/scores, scree/cumulative PVE, biplot, and a reusable PCA cookbook.
- **Iraq Violence‑Related Mortality**
    - Critical read of IFHS vs Iraq Body Count; documents sampling biases, uncertainty quantification (jackknife, Monte Carlo), assumptions, CI reporting, and authors' transparency.
- **Facetting Graphs of NBA Advanced Stats**
    - Per‑player facetted BPM and VORP time series for high‑salary players; data cleaning and `ggplot2` faceting.

## Data Systems Projects
- **Relational DB (Comfy Mug)**
    - Designed ERD → SQLite deployment, synthetic data, analytical SQL queries; discusses normalization, migration to PostgreSQL/MySQL, sharding/replication.
- **NoSQL & Caching**
    - Migrated to MongoDB (local & Atlas), used PyMongo, deployed Redis caching, analyzed replica sets/sharding and cache effects on latency/throughput.
- **Graph Analysis**
    - Modeled data in Neo4j, ran NetworkX metrics and community detection (Louvain, Girvan‑Newman), compared Cypher vs SQL for deep traversals.
- **Semantic Search**
    - Built semantic search with ChromaDB + HuggingFace sentence‑transformers, metadata filtering, nearest‑neighbor retrieval, and evaluation vs keyword methods (BM25/TF‑IDF).
- **Student Depression (PySpark)**
    - End‑to‑end Spark pipeline on Kaggle dataset: Spark SQL cleaning/EDA, outlier checks, Spark ML preprocessing and classifiers, runnable in Google Colab.

## Time Series Analysis Projects
- **Fundamentals & Filtering**
    - AR(2) simulation and 4‑point moving‑average smoothing to study smoothing effects.
- **Risk & Diversification**
    - Variance/covariance proofs showing diversification reduces portfolio volatility for non‑perfectly correlated assets.
- **Operators & Stationarity**
    - Backshift operator algebra; autocovariance/autocorrelation for stationary MA processes.
- **ARMA/ARIMA & Sunspots**
    - MA(1) theoretical bounds and simulations; AR(2) fit to sunspot series with BIC evaluation.
- **Spectral & Signal Synthesis**
    - Fourier synthesis of multi‑frequency cosines and noise to illustrate spectral decomposition.
- **STL & Exponential Smoothing**
    - Seasonal‑Trend decomposition (STL) comparisons (robust vs non‑robust) and Holt‑Winters forecasting.
- **Prophet & Forecast Evaluation**
    - Prophet applied to mortgage trends with critique of failure modes (sudden shifts).
- **SIR & VAR**
    - SIR outbreak threshold analysis and vaccination fraction calculations; VAR(1) for multivariate temporal relationships.
- **Unit Roots & Volatility**
    - ADF/KPSS stationarity tests on persistent AR(1) processes; fit/compare ARCH(1/2) and GARCH(1,1) by BIC.