
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.recommend import recommend

def get_recommendations():
    user_id = user_id_entry.get().strip()
    if user_id.isdigit():
        user_id = int(user_id)
        recommendations = recommend(user_id)
        recommendation_table.delete(*recommendation_table.get_children())
        if recommendations is not None:
            if not recommendations.empty:
                for idx, movie in recommendations.iterrows():
                    recommendation_table.insert("", "end", values=(movie['title'],))
            else:
                recommendation_table.insert("", "end", values=("No recommendations available",))
        else:
            messagebox.showinfo("Info", "User ID does not exist.")
    else:
        recommendation_table.delete(*recommendation_table.get_children())
        messagebox.showerror("Error", "Invalid user ID. Please enter a valid user ID.")


root = tk.Tk()
root.title("Movie Recommendation System")


window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")


input_frame = ttk.Frame(root, padding="20")
input_frame.pack()

user_id_label = ttk.Label(input_frame, text="Enter User ID:")
user_id_label.grid(row=0, column=0, sticky=tk.W)

user_id_entry = ttk.Entry(input_frame, width=10)
user_id_entry.grid(row=0, column=1)

recommend_button = ttk.Button(input_frame, text="Recommend Movies", command=get_recommendations)
recommend_button.grid(row=0, column=2, padx=(10, 0))


output_frame = ttk.Frame(root, padding="20")
output_frame.pack(fill="both", expand=True)


recommendation_table = ttk.Treeview(output_frame, columns=("Title",), show="headings", height=10)
recommendation_table.heading("Title", text="Title")
recommendation_table.pack(fill="both", expand=True)


root.mainloop()
