import tkinter as tk
import random
import string

def generate_password(length=12):
    # Define characters to be used in password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure at least one character from each category
    password = random.choice(string.ascii_lowercase) + \
               random.choice(string.ascii_uppercase) + \
               random.choice(string.digits) + \
               random.choice(string.punctuation)
    
    # Fill the rest of the password with random characters
    password += ''.join(random.choice(characters) for i in range(length - 4))
    
    # Shuffle the characters to make the password more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def generate_passwords():
    try:
        num_passwords = int(num_passwords_entry.get())
        length = int(length_entry.get())
        
        passwords = [generate_password(length) for _ in range(num_passwords)]
        
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Generated Passwords:\n")
        for i, password in enumerate(passwords):
            output_text.insert(tk.END, f"Password {i+1}: {password}\n")
    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
num_passwords_label = tk.Label(root, text="Number of Passwords:")
num_passwords_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

num_passwords_entry = tk.Entry(root)
num_passwords_entry.grid(row=0, column=1, padx=5, pady=5)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI
root.mainloop()
