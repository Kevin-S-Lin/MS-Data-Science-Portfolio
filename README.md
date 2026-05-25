# MS Data Science Portfolio
Showcase of accomplished projects.

## Machine Learning Projects
- Comparing Classifiers
    - Built LDA, Decision Tree, kNN, SVM on original features.
    - Applied PCA and re-tested kNN/SVM with 5, 10, 15 components.
- MNIST Digit Classification
    - Loaded IDX MNIST data into PyTorch.
    - Compared FFNN vs LeNet-5-style CNN (with custom pooling).
    - Ran multiple trials and reported average test accuracy.
- Diabetes Classification
    - Used LDA on key numeric health features.
    - Evaluated tree split quality via Gini impurity and information gain.
- Pizza Brand Classification (Margin Perceptrons)
    - Trained one-vs-one linear margin perceptrons: A/B, A/C, B/C.
    - Computed geometric margins.
    - Combined pairwise models with majority-vote fusion for multiclass prediction.
- Pizza PCA Practice
    - Computed mean, covariance/scatter, eigenpairs.
    - Projected/reconstructed samples with top 2 PCs.
    - Repeated after z-score standardization.
- Gradient Descent Visualization
    - Optimized a 2D objective and plotted iterate paths.
    - Compared exact line search vs backtracking.
    - Repeated under a second matrix setup.
- Backpropagation From Scratch
    - Implemented a 2–2–1 ReLU network manually.
    - Performed forward/backward passes and gradient updates.
    - Tracked and plotted loss over 50 iterations.
- Ensemble Classification (Bagging)
    - Trained 50 bootstrapped neural nets on moonDataset.
    - Plotted individual model error distribution.
    - Built ensembles (5/10/15/20) and showed error vs ensemble size.
- Autoencoders
    - Trained linear and ReLU autoencoders on Pizza features.
    - Swept hidden size (h=1..6), plotted MSE vs (h).
    - Linked optimal linear autoencoder MSE to discarded singular values.
- Clustering + EM
    - Visualized labeled 2D clusters.
    - Ran K-means for (k=2..7), selected (k=4) via silhouette (Euclidean/Manhattan).
    - Implemented GMM-EM (E/M/log-likelihood), estimated (\pi_k,\mu_k,\Sigma_k), and plotted density contours.

## Deep Learning Projects


## Optimizations and Algorithms

## Communicating via Visuals and Graphs in R

## Data Systems Projects

## Time Series Analysis Projects
