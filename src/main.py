import tkinter as tk
from tkinter import ttk
import data_management as dm

class StudentProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Profile")
        self.root.geometry('400x600')

        self.create_widgets()

    def create_widgets(self):
        frame1 = tk.Frame(self.root, bg="grey", width=390, height=590)
        frame1.pack_propagate(False)
        frame1.pack()

        top_frame = tk.Frame(master=frame1, bg="lightgreen", width=380, height=50)
        top_frame.pack_propagate(False)
        search_entry = ttk.Entry(master=top_frame)
        search_entry.pack(pady=5)
        top_frame.pack(pady=20)

        bot_frame = tk.Frame(master=frame1, bg="lightgreen", width=380, height=400)
        bot_frame.pack_propagate(False)
        bot_frame.pack()

        canvas = tk.Canvas(bot_frame, bg="lightgreen", width=380, height=400)
        scrollbar = ttk.Scrollbar(master=bot_frame, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollable_frame = tk.Frame(canvas, bg="lightblue")
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Example list of widgets
        for i in range(50):
            tk.Label(scrollable_frame, text=f"Label {i}", bg="lightblue").pack()



def main():
    root = tk.Tk()
    app = StudentProfileApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()