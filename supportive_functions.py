import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import bpy

def select_thing(things, message = None):
    selected = None
    # Function to handle button click event
    def on_select():
        nonlocal selected
        # Get the selected item
        selected = listbox.get(listbox.curselection())
        # Show a message box with the selected item
        #messagebox.showinfo("Selection", f"You selected {selected}")
        root.destroy()
    # Create the main window
    root = tk.Tk()
    root.title("Listbox Example")

    if message:
        tk.Label(root, text=message).pack()

    # Create a listbox widget
    listbox = tk.Listbox(root, selectmode='single') # set selectmode to single
    listbox.pack()

    # Insert the items into the listbox
    for thing in things:
        listbox.insert(tk.END, thing)

    # Create a button to handle the selection
    select_button = tk.Button(root, text="Select", command=on_select)
    select_button.pack()

    # Run the main loop
    root.mainloop()
    return selected

def add_word_to_list_items(lst, word):
    return [word+"." + item for item in lst]

def get_filepath():
    roots = tk.Tk()
    roots.withdraw()

    browse_filepath = filedialog.askopenfilename()
    return browse_filepath

def get_meshes_names(file_path):
    # Open the .blend file
    bpy.ops.wm.open_mainfile(filepath=file_path)

    # Get a list of all objects in the scene
    objects = bpy.data.objects

    # Extract the names of plain axis objects and store them in a list
    object_names = [obj.name for obj in objects if obj.type == 'EMPTY' and obj.empty_display_type == 'PLAIN_AXES']

    # Close the .blend file
    bpy.ops.wm.save_mainfile()
    bpy.ops.wm.quit_blender()
    return object_names
