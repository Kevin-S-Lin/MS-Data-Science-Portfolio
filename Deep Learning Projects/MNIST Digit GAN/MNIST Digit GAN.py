from numpy import expand_dims
from numpy import zeros
from numpy import ones
from numpy import vstack
from numpy.random import randn
from numpy.random import randint
from keras.datasets.mnist import load_data
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Reshape
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import Conv2DTranspose
from keras.layers import LeakyReLU
from keras.layers import Dropout
from matplotlib import pyplot as plt

class MNIST_GAN:

    # Architecture adapted from class example 02_gan_mnist.py

    def __init__(self, latent_dim):
        self.latent_dim = latent_dim
        self.d_model = self.build_discriminator()
        self.g_model = self.build_generator()
        self.gan_model = self.build_gan()

        # Load and preprocess the MNIST dataset
        (self.trainX, _), (_, _) = load_data()
        self.trainX = expand_dims(self.trainX, axis=-1)  # Add channel dimension
        self.trainX = self.trainX.astype('float32') / 255.0
    
    def get_real_samples(self, n_samples):
        # Select random samples from the dataset
        ix = randint(0, self.trainX.shape[0], n_samples)
        X = self.trainX[ix]

        # Create labels of 1 for real images
        y = ones((n_samples, 1))

        return X, y

    def get_latent_points(self, n_samples):
        # Generate random noise points in the latent space
        x_input = randn(self.latent_dim * n_samples)
        x_input = x_input.reshape(n_samples, self.latent_dim)
        return x_input
        
    def get_fake_samples(self, n_samples):
        # Generate random noise points
        x_input = self.get_latent_points(n_samples)

        # Use generator to create fake images
        X = self.g_model.predict(x_input)

        # Create labels of 0 for fake images
        y = zeros((n_samples, 1))

        return X, y

    def build_discriminator(self):
        model = Sequential()

        # First layer
        model.add(Conv2D(64, (3,3), strides=(2, 2), padding='same', input_shape=(28,28,1)))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.5))

        # Second layer
        model.add(Conv2D(64, (3,3), strides=(2, 2), padding='same'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.5))

        # Smaller third layer
        model.add(Conv2D(128, (3,3), strides=(1, 1), padding='same'))
        model.add(LeakyReLU(alpha=0.2))

        # Flatten and classify 1 for real, 0 for fake
        model.add(Flatten())
        model.add(Dense(1, activation='sigmoid'))

        # Compile the model with Adam optimizer and binary crossentropy loss, lower learning rate
        # from example since Discriminator was improving too quickly
        opt = Adam(learning_rate=0.0001, beta_1=0.5)
        model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])

        return model
    
    def build_generator(self):
        model = Sequential()

        # Calculate number of nodes for reshaping (7x7x128)
        n_nodes = 128 * 7 * 7

        # Noise vector -> feature map
        model.add(Dense(n_nodes, input_dim=self.latent_dim))
        model.add(LeakyReLU(alpha=0.2))

        # 7x7x128
        model.add(Reshape((7, 7, 128)))

        # 7x7 -> 14x14
        model.add(Conv2DTranspose(128, (5,5), strides=(2,2), padding='same'))
        model.add(LeakyReLU(alpha=0.2))

        # 14x14 -> 28x28
        model.add(Conv2DTranspose(128, (5,5), strides=(2,2), padding='same'))
        model.add(LeakyReLU(alpha=0.2))

        # 28x28x1
        model.add(Conv2D(1, (7,7), activation='sigmoid', padding='same'))

        return model

    def build_gan(self):
        # Don't have generator training bleeding into discriminator training
        self.d_model.trainable = False

        # GAN model
        model = Sequential()
        model.add(self.g_model)
        model.add(self.d_model)

        # Generator optimizer like example, but with a higher learning rate
        # to allow it to catch up with the discriminator
        opt = Adam(learning_rate=0.0003, beta_1=0.5)
        model.compile(loss='binary_crossentropy', optimizer=opt)
        
        return model
    
    def train(self, n_epochs=200, batch_size=256):
        # Calculate number of batches per epoch
        num_batches = self.trainX.shape[0] // batch_size

        # Halve the batch size for discriminator training
        half_batch = int(batch_size / 2)

        # Prepare lists to store losses for plotting
        d_losses, g_losses = [], []

        # Loop over epochs
        print("Starting training...")
        for epoch in range(n_epochs):
            for batch_num in range(num_batches):
                # Print progress
                print(f'Epoch {epoch+1}/{n_epochs}, Batch {batch_num+1}/{num_batches}', end='\r')
                
                # Get real samples
                X_real, y_real = self.get_real_samples(half_batch)

                # Get fake samples
                X_fake, y_fake = self.get_fake_samples(half_batch)

                # Combine real and fake samples
                X, y = vstack((X_real, X_fake)), vstack((y_real, y_fake))

                # Train discriminator on combined batch
                d_loss, _ = self.d_model.train_on_batch(X, y)

                # Generate points in latent space as input for the generator
                x_input = self.get_latent_points(batch_size)

                # Create inverted labels for the generator (all 1s)
                y_gan = ones((batch_size, 1))

                # Train generator via GAN model
                g_loss = self.gan_model.train_on_batch(x_input, y_gan)

            # Print and save losses for each epoch
            print(f'Epoch {epoch+1}/{n_epochs}, Discriminator Loss: {d_loss:.4f}, Generator Loss: {g_loss:.4f}')
            d_losses.append(d_loss)
            g_losses.append(g_loss)

            # Generate and save images every 50 epochs and first epoch
            if (epoch + 1) % 50 == 0 or epoch == 0:
                self.save_generated_images(epoch + 1)

        return d_losses, g_losses

    def save_generated_images(self, epoch, n=4):
        # Generate images
        X, _ = self.get_fake_samples(n * n)

        # Plot images
        plt.figure(figsize=(10, 10))
        for i in range(n * n):
            plt.subplot(n, n, 1 + i)
            plt.axis('off')
            plt.imshow(X[i, :, :, 0], cmap='gray_r')
        plt.tight_layout()
        plt.savefig(f'generated_images_epoch_{epoch}.png')
        plt.close()

    def make_and_save_plot(self, disc_loss, gen_loss):
      # Plot discriminator and generator losses as separate lines on the same graph
      plt.figure(figsize=(12, 6))
      plt.plot(disc_loss, label='Discriminator Loss', color='blue')
      plt.plot(gen_loss, label='Generator Loss', color='orange')
      plt.title('Discriminator and Generator Losses')
      plt.xlabel('Epochs')
      plt.ylabel('Loss')
      plt.legend()
      plt.grid()
      plt.savefig('discriminator_generator_losses.png')
      plt.show()


mnist_gan = MNIST_GAN(latent_dim=100)
disc_loss, gen_loss = mnist_gan.train()
mnist_gan.make_and_save_plot(disc_loss, gen_loss)