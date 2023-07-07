# Text-Generation-Neural-Network
Since recurrent neural networks and LSTMs in particular have a short term memory, we can train it to “guess” the next letter based on the letters that came before. That leads to our network producing these texts like Shakespeare. 

## Installation
```bash
pip install tensorflow
```
## Usage
First get the training data for your neural network, then build the Reccurent Neural Network and train it on the training data.
After that you can start generating text, playing around with the length and the temperature. The first sentence (40 characters) will be taken from the original file and the rest of the characters will be generated.

## Results
If you consider the fact that our computer doesn’t even understand what a word or a sentence is, these results are mind-blowing. Of course, they are not perfect and a lot of times (especially when choosing a high temperature), we will end up with some creative word creations. But still it is kind of impressive.
```python
print(generate_text(300, 0.2))
```
```bash
but weakness
to bear the matter thus; mean the word with the words,
the ame the word of the foothed have soul.

paris:
the war would not with the brother that stath
the brother to the word of the word and with the stather.

polixenes:
what see the seat the seat and the bearth,
the world to the part soul the word the brother,
the seat and
```
```python
print(generate_text(300, 0.4))
```
```bash
's curse is fallen upon my head;
'when have part of the brother with the word.

king henry vi:
he were hard of the greens and the boness
of my son with fair so the fallores and him,
the with his head the strong and stride with state
that word may speak the daughter and the brather
word the hast of the heaven soul of him speak,
whose to th
```
```python
print(generate_text(300, 0.6))
```
```bash
edward:
o warwick, warwick! that plantater and good
look here i read of the kings.

king richard ii:
who should let your foot in the great horse,
set not the heremones with him that my man
so his doners of my part is stride,
the worth are here, in the groncest the bast
our daughter consean in the king,
and that i actount of him in the br
```
```python
print(generate_text(300, 0.8))
```
```bash
tly, for one would kill the other. thou!
bow so not in the rather counter not to their
princious lifford that i spetk our dear!
edward leave of the bather strien-stands their
grief word with your child, he hast to thee:
both to set a ase's oft!

mucter:
i am he betting stand it
the artaitous woos like to the master,
so as not now promised
```
```python
print(generate_text(300, 1.0))
```
```bash
ull of grief;
yet, gracious madam, bear thismon, scour?     

pauticuing:
but a great past, he then but did?

nurse:
march, quues out some swooldod, i'll much     
say the friom lies, my statrent gander.       
our is, what risher with to queer, than sewth,
but state to the fortune intittuest head wrove
as faysol heard with save too--
say you scarners, in
```
