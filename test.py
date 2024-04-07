import tkinter as tk

def show_page(page):
    page.tkraise()

def create_page1(container):
    page1 = tk.Frame(container)
    
    label = tk.Label(page1, text="Page 1")
    label.pack()
    
    button = tk.Button(page1, text="Go to Page 2", command=lambda: show_page(page2))
    button.pack()

    return page1

def create_page2(container):
    page2 = tk.Frame(container)
    
    label = tk.Label(page2, text="Page 2")
    label.pack()
    
    button = tk.Button(page2, text="Go to Page 1", command=lambda: show_page(page1))
    button.pack()

    return page2

root = tk.Tk()
root.title("Multiple Pages")

container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)

page1 = create_page1(container)
page2 = create_page2(container)

page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")

show_page(page1)

root.mainloop()
