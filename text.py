import tkinter as tk

title = "My Info"
desc = "This is a simple program that displays information about me."

root = tk.Tk()
root.title(title)
root.geometry("300x200")
 

# Create and display the label with the description text
label = tk.Label(root, text=desc, font=('Arial', 12), fg='black', bg='white', wraplength=280)
label.pack(pady=20)  # Pack the label with padding

root.mainloop()
