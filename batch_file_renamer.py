# Batch File Renamer

import os

def findFileType(f):
    '''
    Input: file name
    Return: file type extension and start position of file type
    '''
    revFileType = ''
    fileType = ''
    hasFileType = bool
    position = 0
    for letter in reversed(f):
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
        return ('', len(f))

def createNewName(f, removeLetter, replaceWith):
    '''
    Input: file name
    Return: file name with characters replaced and file extension added
    '''
    fileType = findFileType(f)[0]
    fileTypePos = findFileType(f)[1]
    fileWithoutType = f[:fileTypePos]

    return fileWithoutType.replace(removeLetter, replaceWith) + fileType

def fileRename(request, fileDirectory, removeLetter, replaceWith):
    '''
    Input: request [print: displays changes, y: writes changes]
    Output: prints list of changes or writes changes
    '''
    file_list = os.listdir(fileDirectory)
    if request == 'y':
        for f in file_list:
            os.rename(os.path.join(fileDirectory, f), os.path.join(fileDirectory, createNewName(f, removeLetter, replaceWith)))
    elif request == 'print':
        for f in file_list:
            print(createNewName(f, removeLetter, replaceWith))
        return [createNewName(f, removeLetter, replaceWith) for f in file_list]
    

if __name__ == "__main__":

    continue_program = 'y'

    while continue_program == 'y':

        fileDirectory = input("Place a file from the directory: ")
        fileDirectory = os.path.dirname(os.path.realpath(fileDirectory))
        print("Chosen file directory:", fileDirectory)
        removeLetter = input("What character to remove? ")
        replaceWith = input("What to replace with? ")
        
        fileRename('print', fileDirectory, removeLetter, replaceWith)
        confirm = input("Press y to confirm: ").lower()
        if confirm == 'y':
            fileRename(confirm, fileDirectory, removeLetter, replaceWith)
        continue_program = input("Press y to continue renaming: ").lower()
