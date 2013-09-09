import GoldenAge
import GoldenAge.tools
import random

test = GoldenAge.Book("Simple Example")
test.add_author("Bill Shakespeare")
test.edit_description("The age old story of a boy and a girl.  But not really 'and'.")

node = test.add_branch(text="There was a boy.")
test.terminate_branch(node)
test.add_branch(node, "  He died.")
test.add_branch(node, "  He lived.")

node = test.insert_branch(node, 11)
node = test.add_branch(node, " girl.  She lived.")

node = test.insert_branch(node, 16)
test.add_branch(node, " happily ever after!")

print test.get_info()
print
print "------------------------------"
print

#for id, node in sorted(test._nodes.items()):
#    print id
#    print node._text
#    for link in node.get_links():
#        print link, "  ",
#    print
#    print
#print "------------------------------"

print test.dump("OLD")
print
print test.dump("NEW")
print
#print test.dump("POPULAR")
#print

trials = set()
for i in xrange(100):
    trials.add(test.dump("RANDOM"))
for text in sorted(trials):
    print text

GoldenAge.tools.make_graph(test)
