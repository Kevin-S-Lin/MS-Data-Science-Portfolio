## Generative Adversarial Network (GAN) for MNIST Digit Synthesis

### Project Goal

Implemented a Generative Adversarial Network (GAN) to synthesize handwritten digits from the MNIST dataset. The project involved designing a zero-sum game between a Generator, which creates images from noise, and a Discriminator, which learns to distinguish real data from synthetic outputs.

### Implementation Details

* **Architectural Design:**
* **Generator:** Developed a network to transform a latent noise vector into a $28 \times 28$ grayscale image.
* **Discriminator:** Engineered a binary classifier to assign probabilities to inputs, determining whether they originated from the training set or the generator.


* **Adversarial Training Logic:**
* **Discriminator Optimization:** Calculated and backpropagated the total loss by combining binary cross-entropy results from both real data (ground truth labels) and synthetic data (fake labels).
* **Generator Optimization:** Optimized the generator by maximizing the probability of the discriminator making an incorrect classification on synthetic samples.


* **Model Training:** Executed a 200-epoch training cycle, monitoring the evolving competition between the two sub-networks.

### Key Analysis

* **Loss Trend Interpretation:** Analyzed the oscillation and convergence patterns of the generator and discriminator loss curves, identifying the equilibrium point where the generator successfully "fooled" the discriminator.
* **Epoch-Based Visual Evolution:** Documented the qualitative improvement of image synthesis at the 1st, 50th, 100th, 150th, and 200th epochs, tracing the transition from random Gaussian noise to recognizable digits.
* **Stability:** Evaluated the impact of learning rates and noise vector dimensions on training stability and mode collapse prevention.

### Tech Stack

* **Framework:** [Keras / TensorFlow / PyTorch]
* **Architecture:** Generative Adversarial Network (GAN)
* **Dataset:** MNIST (Handwritten Digits)
* **Optimization:** Binary Cross-Entropy Loss, Adam/SGD Optimizers