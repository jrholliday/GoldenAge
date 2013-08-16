import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import networkx


def make_graph(book, filename="graph.png"):
        G = networkx.DiGraph()
        for node in book._nodes:
            for link, weight in book._nodes[node].get_links().iteritems():
                G.add_edge(book._nodes[node].get_text(),
                           book._nodes[link].get_text(),
                           weight=weight)

        networkx.draw(G, font_size=8, node_size=5000, node_color="yellow")
        matplotlib.pyplot.savefig(filename)
