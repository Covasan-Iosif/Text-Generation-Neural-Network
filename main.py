import random
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation
from keras.optimizers import RMSprop

# download the file into our script and start reading and decoding it
filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# convert all of the text into lower-case so that we have fewer possible choices
text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()

# processing a total of 500,000 characters, which should be enough for pretty descent results.
text = text[300000:800000] 

# sorted set of all the unique characters that occur in the text
characters = sorted(set(text))

# easily convert a character into a unique numerical representation and vice versa
char_to_index = dict((c, i) for  i, c in enumerate(characters))

index_to_char = dict((i, c) for  i, c in enumerate(characters))

SEQ_LENGTH = 40
STEP_SIZE = 3

'''
sentences = []
next_characters = []

# iterate through the whole text and gather all sentences and their next character
# training data for our neural network
for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH])
    next_characters.append(text[i+SEQ_LENGTH])


x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=np.bool_)
y = np.zeros((len(sentences), len(characters)), dtype=np.bool_)

# one dimension for the sentences
# one dimension for the positions of the characters within the sentences
# one dimension to specify which character is at this position

for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i, t, char_to_index[character]] = 1
    y[i, char_to_index[next_characters[i]]] = 1

# Building Recurrent Neural Network

model = Sequential()
model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters)))) # Long-Short-Term Memory neural network
model.add(Dense(len(characters)))
model.add(Activation('softmax')) # scales the output so all the values add up to 1
# the output is always a probability of how likely a certain character is going to be the next character

# we compile the model and train it with our training data
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))

model.fit(x, y, batch_size=256, epochs=4)

model.save('textgenerator.model')
'''
# the model is trained but it only outputs the probabilities for the next character
model = tf.keras.models.load_model('textgenerator.model')

# Helper function
# it takes the result of the prediction and a temperature as the parameters
# high temperature => less likely / risky characters
# low temperature => conservative/safe character

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# generating the text
# copy the first 40 characters and then generate
def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1) # start at a random position
    generated = ''
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, character in enumerate(sentence):
            x[0, t, char_to_index[character]] = 1

        predictions = model.predict(x, verbose=0)[0]
        next_index = sample(predictions, temperature)
        next_character = index_to_char[next_index]

        generated += next_character 
        sentence = sentence[1:] + next_character

    return generated

# print('-----0.2-----')
# print(generate_text(300, 0.2))
# print('-----0.4-----')
# print(generate_text(300, 0.4))
# print('-----0.6-----')
# print(generate_text(300, 0.6))
# print('-----0.8-----')
# print(generate_text(300, 0.8))
# print('-----1.0-----')
# print(generate_text(300, 1.0))
print(generate_text(300, 1.0))
