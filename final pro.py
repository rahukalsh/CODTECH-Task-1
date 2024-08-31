import re
import tkinter as tk
from tkinter import messagebox


def check_password_strength(password):

    # Initialize the strength score
    strength = 0
    feedback = []  
    
    # Length check
    length = len(password)
    if length < 8:
        feedback.append("\nPassword is too short. Minimum length is 8 characters.")
    elif length > 12:
        strength += 2
        feedback.append("\nPassword length is good.")
    else:
        strength += 1
        feedback.append("\nPassword length is acceptable.")

    # Complexity checks
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("\nPassword should include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("\nPassword should include at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("\nPassword should include at least one digit.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("\nPassword should include at least one special character like (@$!%*?&).")

    # Uniqueness check
    if len(set(password)) / length > 0.7:
        strength += 1
        feedback.append("\nPassword has a good level of uniqueness.")
    else:
        feedback.append("\nPassword could be more unique. So avoid using repetitive characters.")

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
    
    return strength, feedback, final_feedback
    
# Function to toggle the visibility of the password in the entry widget.
def toggle_password_visibility():
    
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        visibility_button.config(text="Show Password")
    else:
        password_entry.config(show="")
        visibility_button.config(text="Hide Password")

def on_check_password_strength():
    password = password_entry.get()
    score = check_password_strength(password)
    strength_label.config(text=f"Password Strength: {score}")

# Initialize the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("540x540")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

visibility_button = tk.Button(root, text="Show Password", command=toggle_password_visibility)
visibility_button.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=on_check_password_strength)
check_button.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Helvetica", 12))
strength_label.pack(pady=10)
root.mainloop()