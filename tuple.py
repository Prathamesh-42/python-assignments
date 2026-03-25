tup=(1,2,3,4,5,6,7)
print("Access first element:",tup[0])
print("Access elements[1:4]:",tup[1:4])

nested_tuple=(1,2,(3,4,5),(6,7))
print("Access nested element: ",nested_tuple[2][1])

repeat_tuple=(2,4,6)*3
print("Tuple repetition: ",repeat_tuple)

tup_1=(2,4,6)
tup_2=(8,10,12)
concatenate=tup_1+tup_2
print("Concatenation of tuples: ",concatenate)