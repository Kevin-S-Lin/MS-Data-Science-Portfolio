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


## IMDB Sentiment Analysis


## LSTM Alphabet Sequence Prediction


## MNIST Digit GAN
