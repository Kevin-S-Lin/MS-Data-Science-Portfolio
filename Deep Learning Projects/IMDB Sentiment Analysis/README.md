## IMDB Sentiment Analysis: Comparative Modeling with CNNs and Embeddings

### Project Goal

Classify movie reviews as positive or negative using the IMDB dataset. The project compares traditional baseline models against Convolutional Neural Networks (CNN) leveraging word embeddings.

### Implementation Details

* **Data Preprocessing:** Restricted vocabulary to the top 5,000 words and applied sequence padding to standardize input length.
* **Feature Engineering:** Implemented an **Embedding Layer** to map discrete word integers into continuous vector space.
* **Architectures:**
* **Baselines:** Logistic Regression and a Feed-Forward Neural Network.
* **CNN:** Utilized `Conv1D` for spatial feature extraction across word sequences and `MaxPooling1D` for dimensionality reduction.


* **Optimization:** Evaluated performance using binary cross-entropy loss and accuracy metrics; tuned epochs and batch sizes for convergence.
* **Preprocessing Experiment:** Conducted a comparative test by removing stopwords to measure the impact of noise reduction on model accuracy.

### Key Analysis

* **Model Comparison:** Evaluated the performance gap between linear baselines and sequence-aware CNN models.
* **Spatial Feature Extraction:** Analyzed how 1D convolutions capture local dependencies in text compared to standard dense layers.
* **Performance:** Achieved a classification accuracy exceeding 85%.

### Tech Stack

* **Framework:** [Keras / TensorFlow / PyTorch]
* **Key Layers:** Embedding, Conv1D, MaxPooling1D, Dense
* **NLP Techniques:** Word Embeddings, Sequence Padding, Stopword Removal