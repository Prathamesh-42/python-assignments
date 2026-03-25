l1=[1,2,3,4,5]
print("Access first element:",l1[0])
print("Access last element:",l1[-1])

l1.append(6)
print("After append:",l1)

l1.insert(2,20)
print("After insert:",l1)

l1.remove(20)
print("After remove:",l1)

r_element=l1.pop()
print("After pop:",l1)

n=[5,4,3,2,1,7,9]
n.sort()
print("Sorted List: ",n)

n.reverse()
print("Reversed list: ",n)