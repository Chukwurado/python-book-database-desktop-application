"""
A program that stores book information:
Title, Author, Year, ISBN

User can:
Search an entry, Add an entry, Update entry, Delete, Close
"""
from tkinter import *
import backend

selected_tuple = ()
def get_selected_row(event):
    global selected_tuple
    if not list1.curselection():
        return
    index=list1.curselection()[0]
    selected_tuple = list1.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[4])

def veiw_command(): 
    list1.delete(0, END)
    rows = backend.view()
    for row in rows:
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    rows = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    for row in rows:
        list1.insert(END, row)

def add_command():
    list1.delete(0, END)
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    veiw_command()

def update_command():
    backend.update( selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk()

window.wm_title("BookStore")

title_label = Label(window, text="Title: ")
title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_label.grid(row=0, column=0)
title_entry.grid(row=0, column=1)


year_label = Label(window, text="Year")
year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_label.grid(row=1, column=0)
year_entry.grid(row=1, column=1)


author_label = Label(window, text="Author")
author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_label.grid(row=0, column=2)
author_entry.grid(row=0, column=3)


isbn_label = Label(window, text="ISBN")
isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_label.grid(row=1, column=2)
isbn_entry.grid(row=1, column=3)


list1 = Listbox(window, height=7, width=35)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)


b1 = Button(window, text="View all", width=12, command=veiw_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
