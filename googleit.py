import tkinter as tk, webbrowser as wb, urllib.parse as ulib

# install konqueror for KDE environments

def searchWeb(event):
	wb.open("https://www.google.com/search?q=" + ulib.quote(search.get()))

def close(event):
	root.destroy()

def select_all(event):
	event.widget.select_range(0, 'end')
	event.widget.icursor('end')

root = tk.Tk()
root.title('GoogleIT')
root.geometry('500x20')

search=tk.StringVar()
e = tk.Entry(root, textvariable=search, width=495)
e.configure(insertbackground='white')

e.bind('<Return>', searchWeb)
e.bind('<Control-KeyRelease-a>', select_all)
e.bind('<Escape>', close)

e.pack()
e.focus()
root.mainloop()
