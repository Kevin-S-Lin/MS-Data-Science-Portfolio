## Boston Housing: Regression via Multilayer Perceptron

### Project Goal

Predict median home values (MEDV) using a multilayer perceptron (MLP) and analyze the impact of network depth on convergence speed and error rates.

### Implementation Details

* **Data Processing:** Standardized input features using a Scikit-Learn pipeline to prevent data leakage during cross-validation.
* **Architecture:** Built a feedforward neural network with ReLU activation and MSE loss.
* **Evaluation:** Used k-fold cross-validation to calculate mean error and standard deviation across different folds.
* **Custom Framework:** Developed a modular function to generate fully connected networks of arbitrary depth for comparative testing.

### Key Analysis

* **Network Depth:** Compared performance between a single-hidden-layer baseline and deeper architectures.
* **Convergence:** Tested how increasing layers affected the number of epochs required to reach a stable Mean Squared Error (MSE).
* **Performance:** Achieved a target error rate of approximately 20 (MSE).

### Tech Stack

* **Framework:** [TensorFlow/PyTorch/Keras]
* **Libraries:** Scikit-Learn, NumPy, Pandas
* **Modeling:** K-fold Cross-Validation, ReLU, MSE Loss