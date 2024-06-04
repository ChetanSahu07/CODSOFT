import tkinter as tk
from tkinter import scrolledtext
from chatbot import Chatbot

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pizza Restaurant Chatbot")
        self.window.geometry("700x600")
        self.window.configure(bg='#e5ddd5')

        self.chatbot = Chatbot()

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        # Create and pack widgets
        self.main_frame = tk.Frame(self.window, bg='#e5ddd5')
        self.main_frame.pack(expand=True)

        self.chat_log = scrolledtext.ScrolledText(self.main_frame, state='disabled', width=80, height=20, wrap=tk.WORD, bg='#ffffff', fg='#000000', font=("Helvetica", 12), bd=0, padx=10, pady=10)
        self.chat_log.grid(row=0, column=0, padx=10, pady=10)

        self.entry_frame = tk.Frame(self.main_frame, bg='#e5ddd5')
        self.entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.entry_box = tk.Entry(self.entry_frame, bg='#ffffff', fg='#000000', font=("Helvetica", 12), bd=0, insertbackground='#000000')
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=5)
        self.entry_box.bind("<Return>", self.process_user_input)

        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.process_user_input, bg='#075e54', fg='white', font=("Helvetica", 12), bd=0, activebackground='#128c7e', activeforeground='white', padx=10, pady=5)
        self.send_button.pack(side=tk.RIGHT)

    def style_widgets(self):
        # Set consistent width for the chat log and entry box
        self.chat_log.config(width=80)
        self.entry_box.config(width=70)

    def process_user_input(self, event=None):
        user_input = self.entry_box.get()
        self.entry_box.delete(0, tk.END)

        self.update_chat_log(f"User: {user_input}")

        response = self.chatbot.get_response(user_input)
        self.update_chat_log(f"Bot: {response}")

    def update_chat_log(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state='disabled')
        self.chat_log.yview(tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = ChatbotGUI()
    gui.run()
