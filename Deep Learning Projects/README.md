# Deep Learning Projects

## Multilayer Perceptron
- Dataset: Pima Indians diabetes dataset.
- Part 1
    - Model: Keras Sequential with Dense(12, relu) -> Dense(8, relu) -> Dense(1, sigmoid).
    - Training: Compiles with binary_crossentropy, adam, metrics accuracy; fits for 150 epochs, batch_size=10, silent training (verbose=0).
    - Output: Predicts on the training set, thresholds at 0.5 and prints first 5 predicted vs expected labels.
- Part 2
    - Model factory: create_model(optimizer='adam', init='glorot_uniform') builds same architecture but sets kernel_initializer=init.
    - Hyperparameters: Grid over optimizer (rmsprop, adam), init (glorot_uniform, normal, uniform), epochs (50,100,150), batch_size (5,10,20).
    - Search: Wraps model with KerasClassifier, runs GridSearchCV (cv=3), prints best score/params and all mean/std results.
    - Output: Finds best hyperparameter combination and reports cross-validated scores.
## Boston Housing - Network Depth Comparison
Predict median home values (MEDV) using a multilayer perceptron (MLP) and analyze the impact of network depth on convergence speed and error rates.

## IMDB Sentiment Analysis
Classify movie reviews as positive or negative using the IMDB dataset. The project compares traditional baseline models against Convolutional Neural Networks (CNN) leveraging word embeddings.

## LSTM Alphabet Sequence Prediction
Developed a Recurrent Neural Network (RNN) using Long Short-Term Memory (LSTM) units to solve a character-level sequence prediction task. The model was trained to predict the succeeding letter in the alphabet given a single-character input, establishing a foundation for more complex time-series and sequence modeling.

## MNIST Digit GAN
Implemented a Generative Adversarial Network (GAN) to synthesize handwritten digits from the MNIST dataset. The project involved designing a zero-sum game between a Generator, which creates images from noise, and a Discriminator, which learns to distinguish real data from synthetic outputs.