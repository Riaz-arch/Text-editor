from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Set up root window

window = Tk()
window.title("My text editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

#function tto open a file

def open_file():
    """Open a file for editing"""
    filepath=askopenfilename(filetypes=[("Text Files","*.txt"),("ALL FILES","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)

    #IF file is open,display content of file

    with open(filepath,"r")as input_file:

        #Read content of the input file

        text = input_file.read()

        #insert content of the file in the editor box

        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"My text editor - {filepath}" )

    #Function to save a file

def save_file():

    #Save the current file as a new file

    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("text files","*.txt"),("all files","*.*")],)
    if not filepath:
        return
    with open(filepath,"w")as output_file:

    # Read the edited content and update in the output file

        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")

# Add widgets in the application

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()