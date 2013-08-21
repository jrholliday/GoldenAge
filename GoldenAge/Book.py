from GoldenAge._Node import Node

import cPickle as pickle
import datetime
import dateutil.parser
import random

import os

###############################################################################

class Book(object):
    """Collection of linked nodes/writtings.  Taken together, they form a Book"""
    def __init__(self, title):
        """Initialize a new Book object with a specified title"""
        self._BEGIN = datetime.datetime.now().isoformat()
        self._END   = datetime.datetime.max.isoformat()
        self._END   = datetime.datetime.min.isoformat()
        # Initialize Book members
        self._title  = str(title).strip()
        self._author = list()
        self._meta   = dict({'desc':str()})
        self._nodes  = dict()
        # Create "Book Cover"
        self._nodes[self._BEGIN] = Node()
        self._nodes[self._BEGIN]._set_id(self._BEGIN)
        self._nodes[self._BEGIN].set_text("[ "+self._title+" ]")
        # Create "End Page"
        self._nodes[self._END] = Node()
        self._nodes[self._END]._set_id(self._END)
        self._nodes[self._END].set_text("The End")
        #
        return None

    #-------------------------------------------------------------------------#

    def get_info(self):
        """Return a formatted description of The Book (perfect for dust jackets)"""
        first_edit = dateutil.parser.parse(
            sorted(self._nodes.keys())[ 0]).strftime("%d %b %Y")
        last_edit  = dateutil.parser.parse(
            sorted(self._nodes.keys())[-1]).strftime("%d %b %Y")
        info  = str()
        #
        info += self._title + "\n\n"
        #
        if self._meta['desc'] != "":
            info += self._meta["desc"] + "\n\n"
        for author in self._author:
            info += author + "\n"
        info += "\n"
        info += first_edit + " - " + last_edit
        #
        return info

    def get_title(self):
        """Return a copy of _title"""
        return self._title

    def get_description(self):
        """Return a short description of the Book"""
        return self._meta['desc']

    def get_authors(self):
        """Return a copy of the _author list"""
        return self._author.copy()

    def get_meta(self):
        """Return a copy of the _meta dict"""
        return self._meta.copy()

    def edit_title(self, title):
        """Edit and (re)format the title of the Book"""
        self._title = str(title).strip()
        return None

    def edit_description(self, description):
        """Edit and (re)format a short description of the Book"""
        self._meta['desc'] = str(description).strip()
        return None

    def add_author(self, author):
        """Add a (re)formatted Author to the _author list"""
        self._author.append(str(author).title().strip())
        return None

    def add_meta(self, tag, text):
        """Add a (re)formatted tag/text pair to the _meta dict"""
        self._meta[str(tag).strip()] = str(text).strip()
        return None        

    def add_branch(self, node=None, text=None):
        """Add new node to specified existing node.

           Input Arguments:
               node - ID of node to branch off.  Default is START_OF_BOOK
               text - Text to associate with newly created node.  Default is ""

           Returns:
               ID of newly created node

        """
        node = node or self._BEGIN
        assert(node in self._nodes)
        new_node = Node()
        new_id   = new_node.get_id()
        if text is not None:
            new_node.set_text(text)
        self._nodes[new_id] = new_node
        self._nodes[node].add_link(new_id)
        return new_id

    def terminate_branch(self, node):
        """Add link to connect specified node to END_OF_BOOK

           Input Arguments:
               node - ID of node to connect to END_OF_BOOK

           Returns:
               None

        """
        assert(node in self._nodes)
        self._nodes[node].add_link(self._END)
        return None

    def insert_branch(self, node, break_pt):
        """Break a specified node in two, thus introducing a new branch point.

           Input Arguments:
               node     - ID of node to insert branch point
               break_pt - location in node for new branch point

           Returns:
               ID of original node

        """
        assert(node in self._nodes)
        assert(0 < break_pt < len(self._nodes[node].get_text()))
        new_node = Node()
        new_id   = new_node.get_id()
        new_node.set_text(self._nodes[node].get_text()[break_pt:])
        new_node._set_links(self._nodes[node].get_links())
        self._nodes[new_id] = new_node
        self._nodes[node].set_text(self._nodes[node].get_text()[0:break_pt])
        self._nodes[node]._set_links({new_id: 0.0})
        return node

    def dump(self, mode):
        """Create a representation of the Book.

           Input Arguments:
               mode - method for determining how to traverse the nodes
                      "RANDOM"  - create representation following random nodes [default]
                      "OLD"     - create representation following oldest (original) nodes
                      "NEW"     - create representation following newest nodes
                      "POPULAR" - create representation following most popular nodes

           Returns:
               text string

        """
        text = str()
        node = self._BEGIN
        while node != self._END:
            text += self._nodes[node].get_text() + " "
            nodes = self._nodes[node].get_links()
            if len(nodes) == 0:
                break
            if mode == "OLD":
                node = sorted(nodes)[0]
            elif mode == "NEW":
                node = sorted(nodes)[-1]
            elif mode == "POPULAR":
                node = sorted(nodes)[-1]
            else:
                node = random.choice(nodes.keys())
        return text.strip()

    def save(self, filename):
        """Serialize (pickle) the Book and write it to file.

           Input Arguments:
               filename - relative path to output file

           Returns:
               absolute path to created pickle file

        """
        pickle.dump(self, open(filename, "w"))
        return os.path.abspath(filename)
