import cPickle as _pickle

from Book import Book

def load(filename):
    book = _pickle.load(open(filename))
    return book
