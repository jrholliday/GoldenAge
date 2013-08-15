import cPickle as _pickle

from Book import Book

def license():
    """Display license and copyright notice for the GoldenAge package."""

    import pydoc

    # Read in the license text
    file = open( path + '/license.txt' )
    text = file.read()
    file.close()

    # Use python pager to display the license text
    pydoc.pager(text)

    # End license()
    return None


def load(filename):
    book = _pickle.load(open(filename))
    return book
