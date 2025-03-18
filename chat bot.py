import tkinter as tk
from tkinter import scrolledtext

# Simple chatbot responses
def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I help?",
        "hi": "Hi there! How can I help?",
        "hey": "Hi there! How can I help?",
        "how are you": "I'm just a bot, but I'm doing fine!",
        "bye": "Goodbye! Have a great day!",
        "what is your name" :"my name is bot",
        "what my name":"Your Name Is Prerna Singh",
        "waht is python maam name":"Vibha",
        "what is your age":"1month",
        "tell something about athrava college":"The Atharva brand is synonymous for Excellence. Over the past decade, ‘Brand Atharva’ has carved an important niche in the academic sector in the country. Today, we have, in the vast verdant landscape of the Atharva Educational Complex, several world class institutions.",
        
   }
    return responses.get(user_input.lower(), "I don't understand that.")

def send_message():
    user_input = user_entry.get().strip()
    if user_input:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + user_input + "\n", "user")
        response = get_response(user_input)
        chat_box.insert(tk.END, "Bot: " + response + "\n", "bot")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)
        user_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")
root.configure(bg="#2C3E50")

chat_box = scrolledtext.ScrolledText(root, height=20, width=50, state=tk.DISABLED, bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12))
chat_box.pack(padx=10, pady=10)
chat_box.tag_config("user", foreground="#2980B9", font=("Arial", 12, "bold"))
chat_box.tag_config("bot", foreground="#E74C3C", font=("Arial", 12, "bold"))

user_entry = tk.Entry(root, width=40, font=("Arial", 12))
user_entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12, "bold"), bg="#3498DB", fg="white")
send_button.pack(pady=5)

root.mainloop()
