
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg="#e7dcf0")

# Title Label
title_label = tk.Label(
    root,
    text="Welcome to my GUI App!",
    font=("Arial", 18),
    bg="#5D5D80"
)
title_label.pack(pady=20)

# Name Label
name_label = tk.Label(
    root,
    text="Enter your name:",
    font=("Arial", 12),
    bg="#C459A4"
)
name_label.pack()

# Name Entry
name_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30
)
name_entry.pack(pady=10)


# Greeting Function
def greet_user():
    name = name_entry.get()

    if name:
        greeting_label.config(
            text=f"Hello, {name}!",
            fg="green"
        )
    else:
        greeting_label.config(
            text="Please enter your name!",
            fg="red"
        )


# Reset Function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")


# Greet Button
greet_button = tk.Button(
    root,
    text="Greet Me",
    command=greet_user,
    font=("Arial", 12),
    bg="#585869",
    fg="white"
)
greet_button.pack(pady=10)


# Reset Button
reset_button = tk.Button(
    root,
    text="Reset",
    command=reset,
    font=("Arial", 12),
    bg="#C23D2B",
    fg="white"
)
reset_button.pack(pady=5)


# Greeting Label
greeting_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="purple"
)
greeting_label.pack(pady=20)


# Run the app
root.mainloop()
