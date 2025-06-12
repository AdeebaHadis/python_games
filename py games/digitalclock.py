
import tkinter as tk
from time import strftime

# Function to update time every second
def time():
    string = strftime('%H:%M:%S %p')  # 24-hour with AM/PM
    label.config(text=string)
    label.after(1000, time)

# GUI setup
root = tk.Tk()
root.title('Digital Clock')
root.geometry('300x100')
root.configure(bg='black')

label = tk.Label(root, font=('Helvetica', 40), background='black', foreground='green')
label.pack(anchor='center')

time()  # Start the clock
root.mainloop()
