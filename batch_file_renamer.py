# Batch File Renamer

import os

fileDirectory = input("Place a file from the directory: ")
fileDirectory = os.path.dirname(os.path.realpath(fileDirectory))
print(os.path.dirname(os.path.realpath(fileDirectory)))
print(os.path.dirname(fileDirectory))
print(fileDirectory)
removeLetter = input("What character to remove? ")
replaceWith = input("What to replace with? ")

def findFileType(file):
    '''
    Takes in file name
    Returns file type extension and start position of file type
    '''
    revFileType = ''
    fileType = ''
    hasFileType = bool
    position = 0
    for letter in reversed(file):
        position -= 1
        if letter == ".":
            revFileType += "."
            hasFileType = True
            break
        else:
            revFileType += letter
    if hasFileType == True:
        for character in reversed(revFileType):
            fileType += character
        return fileType, position
    else:
        return ('', len(file))

def createNewName(file):
    '''
    Takes in file name
    Returns file name with characters replaced and file extension added
    '''
    fileType = findFileType(file)[0]
    fileTypePos = findFileType(file)[1]
    fileWithoutType = file[:fileTypePos]
    newName = ''

    print("here1")

    for letter in fileWithoutType:
        if letter == removeLetter:
            newName += replaceWith
        else:
            newName += letter
    return newName + fileType

def fileRename(confirm=0):
    if confirm == 1:
        for file in os.listdir(fileDirectory):
            os.rename(file, createNewName(file))
    else:
        for file in os.listdir(fileDirectory):
            print(createNewName(file))

def main():
    while True:
        fileRename()
        confirm = input("Press 1 to confirm, press c to cancel: ")
        if confirm == 'c':
            break
        else:
            fileRename(confirm)

main()