from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = loadtxt('diabetes.csv', delimiter=',', skiprows=1)
X = dataset[:, 0:8]
Y = dataset[:, 8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
predictions = model.predict(X)
predictions = (predictions > 0.5).astype(int)

for i in range(5):
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], Y[i]))
