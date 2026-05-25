## Alphabet Sequence Prediction using Stacked LSTM Networks

### Project Goal

Developed a Recurrent Neural Network (RNN) using Long Short-Term Memory (LSTM) units to solve a character-level sequence prediction task. The model was trained to predict the succeeding letter in the alphabet given a single-character input, establishing a foundation for more complex time-series and sequence modeling.

### Implementation Details

* **Data Encoding:** Mapped the English alphabet to integer representations (0-25) and applied **One-Hot Encoding** to the target variables for categorical classification.
* **Input Shaping:** Reshaped the input data into the required 3D tensor format: `[samples, time steps, features]`.
* **Architecture:** * Implemented **Stacked LSTM** layers to capture hierarchical sequence dependencies.
* Integrated Dense output layers with Softmax activation for character probability distribution.


* **Optimization:** Normalized input features and tuned the model using categorical cross-entropy loss.

### Hyperparameter Optimization & Analysis

* **Architectural Variations:** Compared the performance of single-layer vs. multi-layer (Stacked) LSTM configurations, analyzing the impact on gradient flow and accuracy.
* **Parameter Sensitivity Testing:** Systematically varied the following hyperparameters to identify optimal convergence points:
* **Hidden Size:** Evaluated the memory capacity of the LSTM cells.
* **Learning Rate:** Optimized the optimizer’s step size to balance training speed and stability.
* **Network Depth:** Observed the correlation between layer count and model generalization.


* **Performance:** Achieved a character prediction accuracy exceeding 80% through iterative refinement.

### Tech Stack

* **Framework:** [Keras / TensorFlow / PyTorch]
* **Model Type:** Recurrent Neural Network (LSTM)
* **Preprocessing:** Integer Mapping, One-Hot Encoding, Min-Max Normalization