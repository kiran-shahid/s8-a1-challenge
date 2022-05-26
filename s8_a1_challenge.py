# -*- coding: utf-8 -*-
"""s8-a1-challenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aA38ldnaDpupS5Mm5qMq1EjGrVb_PBCu
"""

# Commented out IPython magic to ensure Python compatibility.
# Import the necessary libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
# %matplotlib inline

tf.keras.backend.clear_session()  # For easy reset of notebook state.

# Read the file 'IRIS.csv'

df = pd.read_csv('IRIS.csv')

# Take a quick look at the dataset
df.head()

# We use one-hot-encoding to encode the 'species' labels using pd.get_dummies

one_hot_df = pd.get_dummies(df['species'], prefix='species')

# The predictor variables are all columns except species
X = df.drop(['species'],axis=1).values

# The response variable is the one-hot-encoded species values
y = one_hot_df.values

# We divide our data into test and train sets with 80% training size

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.8)

"""Now we will use Keras to construct our MLP. You only need to add the output layer. Each step is described in the comments."""

# To build the MLP, we will use the keras library

model = tf.keras.models.Sequential(name='MLP')

# To initialise our model we set some parameters commonly defined in an MLP design

# The number of nodes in the hidden layer
n_hidden = 25

# The number of input nodes
n_input = len(X[0])

# The number of nodes in the output layer
n_output = len(y[0])

# We add the first hidden layer with `n_hidden` number of neurons and 'relu' activation
model.add((tf.keras.layers.Dense(n_hidden,input_dim= n_input, activation = 'relu',name='hidden')))

# The second layer is the final layer in our case, using 'softmax' on the output labels
model.add(tf.keras.layers.Dense(n_output, activation = 'softmax',name='output'))

# Now we compile the model using 'categorical_crossentropy' loss, optimizer as 'sgd' and 'accuracy' as a metric
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

"""You should always inspect your Keras model with the summary() method. Note the number of parameters in each layer"""

# You can see an overview of the model you built using .summary()
model.summary()

"""Now we fit (or 'train') the MLP on our data, updating the weights to minimize the loss we specified in the call to compile(). (There will be more details on how this update happens in future lectures).

One full training cycle on our data is called an 'epoch.' Usually multiple epochs are required before a model converges. Specify a number of epochs to train for.
"""

# We fit the model, and save it to a variable 'history' that can be accessed later to analyze the training profile
# We also set validation_split=0.2 for 20% of training data to be used for validation
# verbose=0 means you will not see the output after every epoch. Set verbose=1 to see it

history = model.fit(X, y, epochs = 1000, validation_split=0.2, batch_size = 16, verbose=0)

"""We can plot the training history and observe that as the weights were updated our loss declined and the accuracy improved."""

# Here we plot the training and validation loss and accuracy

fig, ax = plt.subplots(1,2,figsize = (16,4))
ax[0].plot(history.history['loss'],color='#EFAEA4',label = 'Training Loss')
ax[0].plot(history.history['val_loss'],color='#B2D7D0',label = 'Validation Loss')
ax[1].plot(history.history['accuracy'],color='#EFAEA4',label = 'Training Accuracy')
ax[1].plot(history.history['val_accuracy'],color='#B2D7D0',label = 'Validation Accuracy')
ax[0].legend()
ax[1].legend()
ax[0].set_xlabel('Epochs')
ax[1].set_xlabel('Epochs');
ax[0].set_ylabel('Loss')
ax[1].set_ylabel('Accuracy %');
fig.suptitle('MLP Training', fontsize = 24)

### edTest(test_accuracy) ###
# Once you have near-perfect validation accuracy, time to evaluate model performance on test set 

train_accuracy = model.evaluate(X_train, y_train)[1]
test_accuracy = model.evaluate(X_test,y_test)[1]
print(f'The training set accuracy for the model is {train_accuracy}\
    \n The test set accuracy for the model is {test_accuracy}')

"""## Mindchow 🍲

After marking, go back and change the number of epochs. Do you think increasing the number of epochs would give you a better performance?

*Your answer here*
"""