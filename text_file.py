file = open("Demo_file.txt","w")
file.write("Hello! This is the first line in the file.\n")
file.write("Python file handling demonstration.\n")
file.close()

print("Data written successfully.\n")

file = open("Demo_file.txt","r")
print("Reading file contents:")
content = file.read()
print(content)
file.close()

file = open("Demo_file.txt","a")
file.write("This is added later using append mode.\n")
file.close()

print("Data appended successfully.\n")

file = open("Demo_file.txt","r")
print("Updated file contents:")
updated_content = file.read()
print(updated_content)
file.close()