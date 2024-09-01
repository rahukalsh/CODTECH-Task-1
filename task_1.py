import re
from tkinter import *


def check_password_strength(password):

    # Initialize the strength score & feedback
    strength = 0
    feedback = []  
    
    # Length check
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. Minimum length is 8 characters.")
    elif length > 12:
        strength += 2
        feedback.append("Password length is good.")
    else:
        strength += 1
        feedback.append("Password length is acceptable.")

    # Complexity checks
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character like   (@$#!%*?&).")

    # Uniqueness check
    if len(set(password)) / length > 0.7:
        strength += 1
        feedback.append("Password has a good level of uniqueness.")
    else:
        feedback.append("Password could be more unique. Avoid repetitive characters.")

    # Strength rating
    final_feedback = ""
    if strength <= 2:
        final_feedback = "Very Weak"
    elif strength == 3:
        final_feedback = "Weak"
    elif strength == 4:
        final_feedback= "Moderate"
    elif strength == 5:
        final_feedback = "Strong"
    else:
        final_feedback = "Very Strong"
    
    return feedback, final_feedback
    
# Function to toggle the visibility of the password in the entry widget.
def toggle_password_visibility():
    
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        visibility_button.config(text="Show Password")
    else:
        password_entry.config(show="")
        visibility_button.config(text="Hide Password")

# To Start
def on_beginning():
    password = password_entry.get()
    feedback, overall_feedback = check_password_strength(password)
    feedback_output = Text(root, height=10, width=62)
    feedback_output.pack(pady=10)
    feedback_output.insert(END, "Password Strength Feedback :\n\n", "bold")
    for item in feedback:
        feedback_output.insert(END, "- " + item + "\n")
    feedback_output.tag_configure("bold", font=("Georgia", 10, "bold" ))
    Label(root, text=f"Overall Password is {overall_feedback}", font=("Georgia", 12, "bold" )).pack()
    Button(root, text= "  Exit :)  ", font=("Calibri",12,"italic"), cursor="hand2", command=closing).pack(pady=60)

# To Close
def closing():
    root.quit()

# Initialize the main application window
root = Tk()
root.title("Ninja PassStrenCheck")
root.geometry("620x640")

f1 = Frame(root, borderwidth=4, relief=SUNKEN)
f1.pack(pady=10)
l = Label(f1, text="Password Strength Checker Tool", font="Georgia 16 bold", pady=5, padx=5 )
l.pack()
f2 = Frame(root)
f2.pack(pady=20)

password_label = Label(f2, text="Enter Password:", font="Georgia 12")
password_label.pack(padx=10, side=LEFT, )

password_entry = Entry(f2, show="*", width=30,font=("Times", 14 ))
password_entry.pack(side=LEFT,padx=15, pady=10 )

visibility_button = Button(f2, text="Show Password", cursor="hand2", command=toggle_password_visibility)
visibility_button.pack(side=LEFT, padx=10)

check_button = Button(root, text="Check Strength", font=("Arial", 12), cursor="hand2", activebackground="Black", activeforeground="White", command=on_beginning)
check_button.pack(pady=30)

root.mainloop()
