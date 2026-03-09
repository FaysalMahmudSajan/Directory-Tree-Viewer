import os
import tkinter as tk
from tkinter import filedialog, scrolledtext

def print_directory_tree(path='.', max_depth=3, prefix='', depth=0, output=[]):
    if depth > max_depth:
        return
    try:
        items = os.listdir(path)
    except PermissionError:
        return
    
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    
    for i, item in enumerate(dirs + files):
        is_last = i == len(dirs + files) - 1
        output.append(prefix + ('└── ' if is_last else '├── ') + item)
        
        if item in dirs and depth < max_depth:
            new_prefix = prefix + ('    ' if is_last else '│   ')
            print_directory_tree(os.path.join(path, item), max_depth, new_prefix, depth+1, output)
    return output

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        tree = print_directory_tree(folder, max_depth=3)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "\n".join(tree))

root = tk.Tk()
root.title("Directory Tree Viewer")

browse_button = tk.Button(root, text="Select Folder", command=browse_folder)
browse_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=80, height=30)
text_area.pack()

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_area.get(1.0, tk.END))

copy_btn = tk.Button(text_area, text="📋", command=copy_to_clipboard)
copy_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

root.mainloop()
