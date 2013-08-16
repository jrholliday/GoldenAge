from GoldenAge._Node import Node

import cPickle as pickle
import datetime
import dateutil.parser
import random

import os

class Book(object):
    def __init__(self, title):
        self._BEGIN = datetime.datetime.now().isoformat()
        self._END   = datetime.datetime.max.isoformat()
        self._END   = datetime.datetime.min.isoformat()
        # Initialize Book members
        self._title  = str(title).strip()
        self._desc   = str()
        self._author = list()
        self._meta   = dict()
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

    def get_info(self):
        first = dateutil.parser.parse(
            sorted(self._nodes.keys())[ 0]).strftime("%d %b %Y")
        last  = dateutil.parser.parse(
            sorted(self._nodes.keys())[-1]).strftime("%d %b %Y")
        info  = ""
        #
        info += self._title + "\n\n"
        info += self._desc + "\n\n"
        for author in self._author:
            info += author + "\n"
        info += "\n"
        info += first + " - " + last
        #
        return info

    def get_title(self):
        return self._title

    def get_desc(self):
        return self._desc

    def get_authors(self):
        return self._author.copy()

    def get_meta(self):
        return self._meta.copy()

    def edit_title(self, title):
        self._title = str(title).strip()
        return None

    def edit_description(self, description):
        self._desc = str(description).strip()
        return None

    def add_author(self, author):
        self._author.append(str(author).strip())
        return None

    def add_meta(self, tag, text):
        self._meta[str(tag).strip()] = str(text).strip()
        return None        

    def add_branch(self, node=None, text=None):
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
        assert(node in self._nodes)
        self._nodes[node].add_link(self._END)
        return None

    def insert_branch(self, node, break_pt):
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
        text = ""
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
        pickle.dump(self, open(filename, "w"))
        return os.path.abspath(filename)
