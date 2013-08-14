import datetime

class Node(object):
    def __init__(self):
        self._id    = datetime.datetime.now().isoformat()
        self._text  = str()
        self._links = dict()
        return None
    
    def _set_id(self, id):
        self._id = str(id).strip()
        return self._id

    def set_text(self, text):
        self._text = str(text).strip()
        return None
    
    def _set_links(self, links):
        self._links = links.copy()
        return None
    
    def add_link(self, node, weight=0.0):
        self._links[node] = float(weight)
        return self._links.copy()
    
    def edit_weight(self, node, weight):
        assert(node in self._links)
        self._links[node] = float(weight)
        return self._links[node]
    
    def get_text(self):
        return self._text
    
    def get_links(self):
        return self._links.copy()
    
    def get_id(self):
        return self._id
