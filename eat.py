myfile = open("myfile.txt")
print(myfile.read())
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
myfile.readlines()

with open("myfile.txt", mode="a") as f:
    f.write("Add new file contexts using write method")
    print(f)

with open("example.txt", mode="w") as tx:
    tx.write("File was created using python")

with open("example.txt", mode="r") as tx:
    print(tx.read())