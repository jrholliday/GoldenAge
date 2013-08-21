import datetime

###############################################################################

class Node(object):
    """Linked-List Node object for a Book.
       Nodes contain an ID, text, and links to other Nodes.

    """

    def __init__(self):
        """Initialize a new Node object"""
        self._id    = datetime.datetime.now().isoformat()
        self._text  = str()
        self._links = dict()
        return None

    #-------------------------------------------------------------------------#
    
    def _set_id(self, id):
        """Set the _id of the node to the specified (and reformatted) id"""
        self._id = str(id).strip()
        return self._id

    #-------------------------------------------------------------------------#
    
    def set_text(self, text):
        """Set the _text of the node to the specified (and stripped) text"""
        self._text = str(text).strip()
        return None
    
    #-------------------------------------------------------------------------#
    
    def _set_links(self, links):
        """Replace the _links list with a copy of the specified links list"""
        self._links = links.copy()
        return None
    
    #-------------------------------------------------------------------------#
    
    def add_link(self, node, weight=0.0):
        """Add a new connection from this node to the specified node.

           Input Arguments:
               node   - ID of node to connect to
               weight - branch/link weight.  Default is 0.0

           Returns:
               Copy of newly edited _links list

        """
        assert(node not in self._links)
        self._links[node] = float(weight)
        return self._links.copy()
    
    #-------------------------------------------------------------------------#
    
    def edit_weight(self, node, weight):
        """Edit connection weight from this node to the specified node.

           Input Arguments:
               node   - ID of node to edit connect weight
               weight - new branch/link weight.

           Returns:
               Copy of newly edited _links list

        """
        assert(node in self._links)
        self._links[node] = float(weight)
        return self._links[node]
    
    #-------------------------------------------------------------------------#
    
    def get_text(self):
	"""Return a copy of the node _text"""
        return self._text
    
    #-------------------------------------------------------------------------#
    
    def get_links(self):
	"""Return a copy of the node _links list"""
        return self._links.copy()
    
    #-------------------------------------------------------------------------#
    
    def get_id(self):
	"""Return the (re)formatted _id of the node"""
        return self._id
