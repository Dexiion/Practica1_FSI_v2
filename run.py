# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
cf = search.GPSProblem('C', 'F'
                       , search.romania)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())

print("A - B")

bnb = search.BandB_graph_search(ab)
print(bnb.path(), "\tVisited:", bnb.visited, "Generated:", bnb.generated)

bnb_sub = search.BandB_Sub_graph_search(ab)
print(bnb_sub.path(), "\tVisited:", bnb_sub.visited, "\tGenerated:", bnb_sub.generated)

print("\nC - F ")

bnb2 = search.BandB_graph_search(cf)
print(bnb2.path(), "\tVisited:", bnb2.visited, "Generated:", bnb2.generated)

bnb_sub2 = search.BandB_Sub_graph_search(cf)
print(bnb_sub2.path(), "\tVisited:", bnb_sub2.visited, "\tGenerated:", bnb_sub2.generated)
