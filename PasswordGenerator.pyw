import random
from tkinter import *
from tkinter import messagebox
import clipboard

# Define window
app = Tk()
app.geometry("205x100")
app.title("Password Generator")

# Items used to generate password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
# From which items you want to generate password
upper, lower, nums = True, True, True

everything = ""
# Add items what you want to everything variable
if upper:
    everything += uppercase_letters
if lower:
    everything += lowercase_letters
if nums:
    everything += digits

length = 20 # Lenght of your password
amount = 1 # Amount of generated passwords

Generated = Label(app, text="Generated password:") 
Generated.grid(row=0, column=1)

Space = Label(app, text="") # Program must look good
Space.grid(row=1, column=0)

PasswordText = Entry(app, width=25) # Text box
PasswordText.grid(row=1, column=1)

# Generating password function
def generate_password():
    PasswordText.delete(0, END) # Clear text box before writing a new password
    for x in range(amount):
        password = "".join(random.sample(everything, length))
        PasswordText.insert(0, password) # Past password into text box
    Completed = Label(app, text="Password generated.", fg="green") # Show info
    Completed.grid(row=3, column=1)

Submit = Button(app, text="Generate", command=generate_password) # Generating button
Submit.grid(row=2, column=1)

# Copying password to clipboard
def copytoclipboard():
    clipboard.copy(PasswordText.get())
    messagebox.showinfo(title="Info", message="Password copied to clipboard.")
    
Copy = Button(app, text="Copy", command=copytoclipboard) # Copying button
Copy.grid(row=1, column=3)

app.mainloop() # Password Generator is made by Brais
