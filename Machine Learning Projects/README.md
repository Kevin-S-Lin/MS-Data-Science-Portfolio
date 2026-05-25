# Machine Learning Projects

## Comparing Classifiers
- Part 1: builds and tests 4 classifiers on the original features:
    - Linear Discriminant Analysis
    - Decision Tree
    - k-Nearest Neighbors
    - Support Vector Machine
- Part 2: applies Principal Component Analysis (PCA) and then evaluates:
    - k-Nearest Neighbors with 5, 10, and 15 principal components
    - Support Vector Machine with 5, 10, and 15 principal components

## MNIST Digit Image Classification
- Loads MNIST IDX files with idx2numpy
- Converts images and labels into PyTorch tensors and DataLoaders
- Trains and evaluates two models:
    - a feedforward network, FeedForwardNN
    - a CNN based on LeNet-5, LeNet5
- Uses a custom pooling layer, TrainablePoolingCoeff, for the CNN
- Repeats training/testing multiple times with FFNN and CNN
- Reports average test accuracy for both approaches via test_FFNN and test_CNN

## Diabetes Classification
- Part (a): Linear Discriminant Analysis
    - Uses the numerical features:
        - age
        - bmi
        - HbA1c_level
        - blood_glucose_level
    - Standardizes the features by subtracting the mean and dividing by the standard deviation.
    - Splits the data into diabetes vs no diabetes groups.
    - Computes:
        - the within-class scatter matrix S_W
        - the between-class scatter matrix S_B
    - Solves for the LDA direction vector w using:
        - S_W^-1 (m1 - m0)
        - and also via the dominant eigenvector of S_W^-1 S_B
- Part (b): Decision Tree Split Metrics
    - Uses the categorical features:
        - hypertension
        - heart_disease
    - Calculates:
        - Gini impurity
        - Information gain
    - Compares which attribute would be better for the first decision tree split.

## Slicing Pizza with Margin Perceptrons
- Part (a): Margin Perceptron
    - Loads the dataset and removes the id column.
    - Splits the data by brand: A, B, and C.
    - Trains a margin perceptron for each pair of classes:
        - A vs B
        - A vs C
        - B vs C
    - Tests each classifier on held-out data and reports accuracy.
- Part (b): Margin Calculation
    - Computes the actual geometric margins for each learned separating hyperplane.
    - Measures how far the closest samples from each class are from the decision boundary.
- Part (c): Fusion Rule for Multiclass Classification
    - Uses the three one-vs-one classifiers to classify new samples.
    - Applies a voting-based fusion rule:
        - A vs B
        - A vs C
        - B vs C
    - Classifies three given examples:
        - s1
        - s2
        - s3

## Pizza PCA Practice
- Loads dataset and selects features: mois, prot, fat, ash, sodium, carb, cal.
- (a) Computes mean feature vector.
- (b) Computes scatter/covariance matrix and finds eigenvalues/eigenvectors (principal components).
- (c) Uses the first two principal components to compute 2‑D approximations for the first two samples (projection + reconstruction).
- (d) Standardizes features (z-score), recomputes covariance, principal components, and repeats the 2‑component approximations.
- Outputs: mean vector, scatter matrix, eigenvalues/eigenvectors, standardized components, and reconstructed approximations.

## Visualize Gradient Descent and Variations
- Goal: solve a 2D constrained optimization via gradient descent and visualize the iterate sequence x^k.
- Objective: f(x) = 0.5 x^T P x + q^T x + log(exp(-2 x1) + exp(-x2)). Implements f and its gradient.
- Problem 1
    - Part (a): gradient descent with exact line search (scipy.optimize.minimize_scalar). P = [[3,4],[4,6]], q = [-2,4], x0 = [1,2]. Stop when ||∇f|| < 0.01. Plots the (x1,x2) trajectory.
    - Part (b): same setup but using backtracking line search (α_init=0.15, γ=0.7, β=0.8). Plots the trajectory.
- Problem 2
    - Repeats Parts (a) and (b) with a different quadratic term P_new = [[5.005,4.995],[4.995,5.005]]; same q and x0. Plots trajectories for each run.

## Backpropagation from scratch (nitty-gritty)
- Goal: implement backpropagation for a fixed small neural network and visualize training loss.
- Network architecture (hard-coded):
    - Input: 2-d vector x = [[2],[1]]
    - Hidden layer: 2 neurons (theta1 shape 2x2, b1 shape 2x1)
    - Output layer: 1 neuron (theta2 shape 1x2, b2 shape 1x1)
    - Activation: ReLU (and its derivative used in backprop)
    - Loss: 0.5*(y - a2)^2 with target y = 3
    - Learning rate gamma = 0.05
    - Weights/biases initialized uniformly in (0,1)
- Training:
    - Forward pass computes z1, a1, z2, a2 and returns loss
    - Backward pass computes gradients via chain rule:
        - delta2 = a2 - y, dtheta2 = delta2 @ a1.T, db2 = delta2
        - delta1 = theta2.T @ delta2 * ReLU'(z1), dtheta1 = delta1 @ x.T, db1 = delta1
    - Parameters updated with gradient descent
    - Loop runs 50 iterations, losses collected
- Output:
    - Loss vs iteration plot showing training progress

## Classification with Ensemble Models
- Dataset: moonDataset.csv — first 150 rows used for training, last 50 for testing.
- Part (a): create 50 bootstrap training datasets (size 150 each).
- Part (b): train 50 feedforward neural nets (input_size=3, one hidden layer of 10 units, sigmoid output, BCELoss, SGD lr=0.05) — 50 training iterations per model. Evaluate each model on the 50-sample test set and plot a histogram of individual error rates.
- Part (c): form bagging ensembles of sizes 5, 10, 15, 20 by sampling trained models; aggregate predictions by majority vote (threshold 0.5) and plot ensemble error rate versus ensemble size.

## Autoencoder Loss Visualized
- Dataset: Pizza.csv — uses 7 feature columns (cols 3–9) as input X (converted to a torch tensor).
- Problem 1
    - Implements a 3-layer autoencoder class in PyTorch (manual parameters with requires_grad=True and manual gradient update).
    - Encoder/decoder:
        - Linear encoder/decoder (no activation) and a ReLU encoder variant.
        - Trains separate autoencoders for hidden dimensions h ∈ {1,2,3,4,5,6}.
    - Training details:
        - MSE loss (mean squared error), learning rate gamma = 1e-4, 1000 iterations per model.
        - Records final MSE for each h and plots MSE vs hidden dimension for both linear and ReLU variants.
- Problem 2
    - Short theoretical answer: MSE of the optimal linear autoencoder with code dimension h equals the variance not captured by the top-h singular values of X (i.e., sum of squared singular values omitted, averaged → reconstruction MSE).
- Outputs
    - Two plots: MSE vs hidden nodes for linear encoder/decoder and for ReLU encoder.
    - Printed sample inputs and final loss arrays.

## Clustering and Expectation Maximization
- Part (a): Data visualization
    - Loads 2D data with known labels.
    - Plots a scatter chart colored by the true label to show the underlying cluster structure.
- Part (b): K-means + silhouette analysis
    - Implements K-means from scratch (assignment/update/convergence checks).
    - Runs K-means for k = 2 to 7.
    - Computes average silhouette coefficients for each k using:
        - Euclidean distance
        - Manhattan distance
    - Plots silhouette score vs. k and concludes the best k is 4 for both metrics.
- Part (c): EM for Gaussian Mixture Model
    - Implements EM from scratch for a 4-component GMM:
        - E-step: posterior responsibilities
        - M-step: updates for (\pi_k), (\mu_k), (\Sigma_k)
        - Log-likelihood tracking for convergence
    - Initializes means from K-means centroids (for faster convergence).
    - Prints estimated (\pi_k) and (\mu_k) and compares them to provided “real” values.
- Final visualization
    - Generates a contour plot of the fitted GMM density over the 2D plane.