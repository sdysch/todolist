# common helper scripts

#====================================================================================================

def stripTODO(string):
    if string.endswith(".todo"):
        return string[:-5]
    return string

#====================================================================================================

def getFileContent(filename):
    with open(filename, "r") as f:
        return f.read()

#====================================================================================================

def getFilePath(listName):
    import os
    import sys

    installdir = os.getenv("TODOLISTDIR")
    listdir = installdir + "/lists/"
    filename = listdir + listName + ".todo"
    if not os.path.isfile(filename):
        print("List `{listname}' does not exist".format(listname=listName))
        sys.exit()
    return filename
