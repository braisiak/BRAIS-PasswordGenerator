import random
from tkinter import *
from tkinter import messagebox
import clipboard
from contextlib import suppress

# Define window
app = Tk()
app.geometry("348x145")
app.title("Password Generator")
app.iconbitmap('data/icon.ico')
app.resizable(0, 0)
# Items used to generate password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = ",.<>?/':;{}[]|\=+-_)(*&^%$#@!~`"
# From which items you want to generate password
upper = BooleanVar()
lower = BooleanVar()
nums = BooleanVar()
syms = BooleanVar()

everything = ""

def check_1():
    global upper
    global everything
    if upper.get() == True:
        everything += uppercase_letters
    elif upper.get() == False:
        everything = everything.replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "")
def check_2():
    global lower
    global everything
    if lower.get() == True:
        everything += lowercase_letters
    elif lower.get() == False:
        everything = everything.replace("abcdefghijklmnopqrstuvwxyz", "")
def check_3():
    global nums
    global everything
    if nums.get() == True:
        everything += digits
    elif nums.get() == False:
        everything = everything.replace("0123456789", "")
def check_4():
    global syms
    global everything
    if syms.get() == True:
        everything += symbols
    elif syms.get() == False:
        everything = everything.replace(",.<>?/':;{}[]|\=+-_)(*&^%$#@!~`", "")
    
# Checkbuttons Labels
CheckboxLabel_1 = Label(app, text="Uppercase")
CheckboxLabel_1.grid(row=2, column=5)

CheckboxLabel_2 = Label(app, text="Lowercase")
CheckboxLabel_2.grid(row=3, column=5)

CheckboxLabel_3 = Label(app, text="Numbers")
CheckboxLabel_3.grid(row=4, column=5)

CheckboxLabel_4 = Label(app, text="Symbols")
CheckboxLabel_4.grid(row=5, column=5)

# Checkbuttons
Checkbox_1 = Checkbutton(app, text="", variable=upper, onvalue = True, offvalue= False, command=check_1)
Checkbox_1.grid(row=2, column=6)

Checkbox_2 = Checkbutton(app, text="", variable=lower, onvalue = True, offvalue= False, command=check_2)
Checkbox_2.grid(row=3, column=6)

Checkbox_3 = Checkbutton(app, text="", variable=nums, onvalue = True, offvalue= False, command=check_3)
Checkbox_3.grid(row=4, column=6)

Checkbox_4 = Checkbutton(app, text="", variable=syms, onvalue = True, offvalue= False, command=check_4)
Checkbox_4.grid(row=5, column=6)

# Length Label
LengthText = Label(app, text="Length: ")
LengthText.grid(row=0, column=5)

Space = Label(app, text="")
Space.grid(row=0, column=4)

# Length Entry
length = Entry(app, width=4) # Length of your password
length.insert(0, "20") # Default length (max. 93)
length.grid(row=0, column=6)

# Amount Label
AmountText = Label(app, text="Amount: ")
AmountText.grid(row=1, column=5)

# Amount Entry
amount = Entry(app, width=4) # Amount of generated passwords
amount.insert(0, "1") # Default amount
amount.grid(row=1, column=6)

Generated = Label(app, text="Generated passwords:") 
Generated.grid(row=0, column=1)

Space_1 = Label(app, text="")
Space_1.grid(row=1, column=0)

PasswordText = Text(app, width=25, height=3) # Text box
PasswordText.grid(row=1, column=1, rowspan=3)

# Generating password function
def generate_password():
    with suppress(ValueError): # Ignore ValueError
        PasswordText.delete("1.0", END) # Clear text box before writing a new password
        for x in range(int(amount.get())):
            password = "".join(random.sample(everything, int(length.get())))
            PasswordText.insert("1.0", password + "\n") # Past password into text box
            if PasswordText.get('end-1c', 'end') == '\n':
                PasswordText.delete('end-1c', 'end')
        Completed = Label(app, text="Password generated.", fg="green") # Show info
        Completed.grid(row=5, column=1)

Submit = Button(app, text="Generate", command=generate_password) # Generating button
Submit.grid(row=4, column=1)

# Copying password to clipboard
def copytoclipboard():
    clipboard.copy(PasswordText.get("1.0", 'end-1c'))
    messagebox.showinfo(title="Info", message="Password copied to clipboard.")
    
Copy = Button(app, text="Copy", command=copytoclipboard) # Copying button
Copy.grid(row=2, column=3)

app.mainloop() # Password Generator was made by Damian "Brais" Uździło
