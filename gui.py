import tkinter as tk
import tkinter.filedialog

import os
import batch_file_renamer as renamer 

class App():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Batch Renamer")

        sv = tk.StringVar()
        sv2 = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.keyPress(sv))
        sv2.trace("w", lambda name, index, mode, sv2=sv2: self.keyPress2(sv2))

        self.entryField1 = tk.Entry(self.root, state='disabled', textvariable=sv)
        self.entryField2 = tk.Entry(self.root, state='disabled', textvariable=sv2)
        self.label = tk.Label(self.root, text="Batch Renamer", pady=20)
        self.butFile = tk.Button(self.root, text="Open File", command=self.fileOpen)
        self.butRename = tk.Button(self.root, text="Rename", command=self.renameConfirm) # begin state as disabled
        self.listB = tk.Listbox(self.root)

    def renameConfirm(self):
        print(f"The value of entry field 1: {self.entryField1.get()} and entry field 2: {self.entryField2.get()}")
        try:
            renamer.fileRename('y', self.get_file_path(), self.entryField1.get(), self.entryField2.get())
            print("Changes made.")
        except:
            print("Write error.")

    def keyPress(self, event):
        print(f"Entry field 1 updated to {self.entryField1.get()}")
        self.updateList(renamer.fileRename('print', self.fileDirectoryPath, self.entryField1.get(), self.entryField2.get()))

    def keyPress2(self, event):
        print(f"Entry field 2 updated to {self.entryField2.get()}")
        self.updateList(renamer.fileRename('print', self.get_file_path(), self.entryField1.get(), self.entryField2.get()))

    def fileOpen(self):
        file1 = tk.filedialog.askopenfile()
        try:
            self.fileDirectoryPath = os.path.dirname(os.path.realpath(file1.name))
            self.entryField1.config(state="normal")
            self.entryField2.config(state="normal")
            print(self.fileDirectoryPath)
            self.updateList(renamer.fileRename('print', self.fileDirectoryPath, self.entryField1.get(), self.entryField2.get()))
            self.rename_func() 
        except AttributeError:
            print("No file path selected...")

    def updateList(self, lst):
        self.listB.delete(0, tk.END)
        self.listB.insert(tk.END, *lst)

    def get_file_path(self):
        return self.fileDirectoryPath

    def get_entry_fields_tuple(self):
        return (self.entryField1.get(), self.entryField2.get())

    def render(self):
        self.label.grid(row=0, column=1)
        self.entryField1.grid(row=1, column=0)
        self.entryField2.grid(row=1, column=2)
        self.butFile.grid(row=2, column=1)
        self.butRename.grid(row=3, column=1)
        self.listB.grid(row=4, column=1)

    def rename_func(self):
        fileDirectory = main_app.get_file_path()
        print(fileDirectory)
        removeLetter, replaceWith = main_app.get_entry_fields_tuple()
        renamer.fileRename('print', fileDirectory, removeLetter, replaceWith)
    
    def run_app(self):
        self.root.mainloop()


if __name__ == "__main__":
    main_app = App()
    main_app.render()
    main_app.run_app()