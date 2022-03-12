""" File Handling Example 1 """
import os
file = open("/home/mark/Desktop/mark.txt", 'w')
file.close()

""" File Handling Example 2 """
import os
file = open("/home/mark/Desktop/mark.txt", 'r')
print(file.read())
file.close()

""" File Handling Example 3 """
import os
file = open("/home/mark/Desktop/mark.txt", 'r')
print(file.readlines())
file.close()

""" File Handling Example 4 - For loop """
import os
file = open("/home/mark/Desktop/mark.txt", 'r')
for line in file:
    print(file.readlines())
file.close()

""" File Handling Example 1 """
import os
file = open("/home/mark/Desktop/python.txt", 'w')
file.write("Here we go")
file.write("confirmed")
file.close()


""" File Handling Example 2 """
import os
file = open("/home/mark/Desktop/python.txt", 'w')
file.write("Oops overwrite")
file.close()

""" File Handling Example 3 - Creation"""
import os
file = open("/home/mark/Desktop/edureka.txt", 'x')
file.write("New File - Edureka")
file.close()

""" Deleting a File - first check whether the file exists """
import os
if os.path.exists("/home/mark/Desktop/edureka.txt"):
    os.remove("/home/mark/Desktop/edureka.txt")
else:
    print("The file does not exist")

""" Deleting a Folder """
os.rmdir("my folder")

""" Creating a folder """
import os
os.chdir("/home/mark/Downloads")
os.mkdir("movies")



