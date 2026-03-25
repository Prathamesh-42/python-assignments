student={"name":"Mic","age":18,"grade":"B"}
print("Dictionary: ",student)
print("Name: ",student["name"])
print("Grade: ",student["grade"])

student["age"]=19
student["city"]="America"
print("Updated Dictionary: ",student)

del student["city"]
print("After deletion: ",student)

dic_1={"a":1,"b":2}
dic_2={"x":11,"y":12}
merge=dic_1 | dic_2
print("Merged Dictionary: ",merge)
