# file = open("example.txt", "w")
# file.write("Hello, this is a test.")
# file.close()




# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()



file = open("example.txt", "a")
file.write("\nThis is an additional line.")
file.close()