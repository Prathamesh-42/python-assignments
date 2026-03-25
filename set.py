s_a={1,2,3,4,5}
s_b={4,5,6,7,8}
print("Set A: ",s_a)
print("Set B: ",s_b)

union=s_a.union(s_b)
print("Union(AUB): ",union)

intersection=s_a.intersection(s_b)
print("Intersection(A∩B): ",intersection)

difference=s_a.difference(s_b)
print("Difference(A-B): ",difference)