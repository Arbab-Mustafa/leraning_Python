import tkinter as tk
from time import strftime

# def update_time():
#     """
#     Updates the clock label with the current time.
#     Uses strftime for optimized performance and ensures smooth updates.
#     """
#     try:
#         current_time = strftime('%H:%M:%S')  # Get the current time in HH:MM:SS format
#         label.config(text=current_time)  # Update the label text
#         root.after(1000, update_time)  # Schedule the function to run again after 1 second
#     except Exception as e:
#         label.config(text="Error")  # Display an error message in case of failure
#         print(f"An error occurred: {e}")  # Print the error for debugging

# # Initialize the Tkinter root window
# root = tk.Tk()
# root.title("Simple Clock")  # Set the window title
# root.geometry("250x100")  # Set the window size
# root.resizable(False, False)  # Disable window resizing

# # Create a label widget to display the time
# label = tk.Label(root, font=('Arial', 40), fg='black', bg='white')
# label.pack(expand=True)

# update_time()  # Start updating the time

# root.mainloop()  # Run the Tkinter event loop





# ////////////////////////////////////






def updateTime():
    try:
        cur_time = strftime('%H:%M:%S')
        label.config(text=cur_time)
        root.after(1000, updateTime)
    except Exception as e:
        print(f"An error occurred: {e}")




root = tk.Tk()
root.title("Simple Clock")
root.geometry("250x100")
root.resizable(False, True)
 

label = tk.Label(root, font=('Arial', 40), fg='black', bg='white')
label.pack(expand=True)
# updateTime()

root.mainloop()

    
