# Create a file named mydata.txt
# Open the file without with (Open in try)
# Catch FileNotFoundError
# In else print contents
# In finally
# Open nonexistent file mydat.txt

try:
    myFile = open("mydat.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("File : ", myFile.read())
    myFile.close()

finally:
    print("Finished working with File")
