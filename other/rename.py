import os
os.getcwd()
collection = "new-guns/new/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("new-guns/new/" + filename, "new-guns/1/" + str(i) + ".jpg")
    

