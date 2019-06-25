# ASAG

ASAG or Automated Short Answer Grading is an application that can be used to automatically correct and grade student answers given question and reference answer.

## Installation

- Install all the dependencies specified in requirements.txt .
- Download the pre-trained model weights of word2vec using this [link](http://wikipedia2vec.s3.amazonaws.com/models/en/2018-04-20/enwiki_20180420_100d.txt.bz2), unzip the file and place the 'enwiki_20180420_100d.txt' file in the main directory
- Download the ELMO tensorflow-hub module (Download using this [link](https://tfhub.dev/google/elmo/2?tf-hub-format=compressed)), unzip it and place the contents in a folder named 'elmo_module' in the root directory. 
- Download the Universal Sentence Encoder tensorflow-hub module (Download using this [link](https://tfhub.dev/google/universal-sentence-encoder/2?tf-hub-format=compressed)), unzip it and place the contents in a folder named 'uni_encoder' in the root directory.


## Usage

In the terminal, execute the following command

```
python app.py
```
