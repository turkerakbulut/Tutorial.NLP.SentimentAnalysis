# Türker Akbulut

# Aşağıdaki linkleri inceleyebilirsiniz. Oldukça faydalı örnek kullanımlar mevcuttur.
# http://billchambers.me/tutorials/2015/01/14/python-nlp-cheatsheet-nltk-scikit-learn.html
# https://web.stanford.edu/class/cs124/lec/naivebayes.pdf
# imdb labeled sentences sample
# https://archive.ics.uci.edu/ml/machine-learning-databases/00331/

import nltk
import pickle
from nltk.tokenize import word_tokenize
from os import path


def get_train_data():
    file_name = "C:/Work/Tutorial.NLP.SentimentAnalysis/imdb_labelled.txt";
    lines = open(file_name, encoding="UTF-8").readlines()
    data = []
    for line in lines:
        values = line.split("\t")
        data.append(values)
    return data;

def naive_bayes_classifier(sentence):
    trainer_file = "C:/Work/Tutorial.NLP.SentimentAnalysis/nbc.p"
    all_words = set(word.lower() for passage in get_train_data() for word in word_tokenize(passage[0]))
    if (path.exists(trainer_file)):
        classifier = pickle.load(open(trainer_file, 'rb'))
    else:
        t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in get_train_data()]
        classifier = nltk.NaiveBayesClassifier.train(t)
        pickle.dump(classifier, open(trainer_file, 'wb'), protocol=None, fix_imports=True)
    test_sent_features = {word.lower(): (word in word_tokenize(sentence.lower())) for word in all_words}
    return classifier.classify(test_sent_features);
