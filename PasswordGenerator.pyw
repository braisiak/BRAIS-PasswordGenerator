import random
from tkinter import *
from tkinter import messagebox
import clipboard
from contextlib import suppress

# Define window
app = Tk()
app.geometry("305x125")
app.title("Password Generator")
# Items used to generate password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
# From which items you want to generate password
upper = BooleanVar()
lower = BooleanVar()
nums = BooleanVar()

everything = ""

def check_1():
    global upper, lower, nums
    global everything
    # Add items what you want to everything variable
    if upper.get() == True:
        everything += uppercase_letters
    if upper.get() == False:
        everything = everything.replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "")
def check_2():
    global upper, lower, nums
    global everything
    if lower.get() == True:
        everything += lowercase_letters
    if lower.get() == False:
        everything = everything.replace("abcdefghijklmnopqrstuvwxyz", "")
def check_3():
    global upper, lower, nums
    global everything
    if nums.get() == True:
        everything += digits
    if nums.get() == False:
        everything = everything.replace("0123456789", "")

CheckboxLabel_1 = Label(app, text="Uppercase")
CheckboxLabel_1.grid(row=2, column=5)

CheckboxLabel_2 = Label(app, text="Lowercase")
CheckboxLabel_2.grid(row=3, column=5)

CheckboxLabel_3 = Label(app, text="Numbers")
CheckboxLabel_3.grid(row=4, column=5)

Checkbox_1 = Checkbutton(app, text="", variable=upper, onvalue = True, offvalue= False, command=check_1)
Checkbox_1.grid(row=2, column=6)

Checkbox_2 = Checkbutton(app, text="", variable=lower, onvalue = True, offvalue= False, command=check_2)
Checkbox_2.grid(row=3, column=6)

Checkbox_3 = Checkbutton(app, text="", variable=nums, onvalue = True, offvalue= False, command=check_3)
Checkbox_3.grid(row=4, column=6)

LengthText = Label(app, text="Length: ")
LengthText.grid(row=0, column=5)

Space = Label(app, text="")
Space.grid(row=0, column=4)

length = Entry(app, width=4) # Length of your password
length.insert(0, "20") # Default length (max. 62)
length.grid(row=0, column=6)

AmountText = Label(app, text="Amount: ")
AmountText.grid(row=1, column=5)

amount = Entry(app, width=4) # Amount of generated passwords
amount.insert(0, "1") # Default amount
amount.grid(row=1, column=6)

Generated = Label(app, text="Generated password:") 
Generated.grid(row=0, column=1)

Space_1 = Label(app, text="")
Space_1.grid(row=1, column=0)

PasswordText = Entry(app, width=25) # Text box
PasswordText.grid(row=1, column=1)

# Generating password function
def generate_password():
    with suppress(ValueError): # Ignore ValueError
        PasswordText.delete(0, END) # Clear text box before writing a new password
        for x in range(int(amount.get())):
            password = "".join(random.sample(everything, int(length.get())))
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

app.mainloop() # Password Generator was made by Damian "Brais" Uździło
