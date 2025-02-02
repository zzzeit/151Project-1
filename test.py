import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title("Student Profile")
    window.geometry('400x600')

    top_frame = tk.Frame(master=window, bg="lightgreen", width=380, height=50)
    top_frame.pack_propagate(False)
    search_entry = ttk.Entry(master=top_frame)
    search_entry.pack(pady=5)
    top_frame.pack(pady=20)

    bot_frame = tk.Frame(master=window, bg="lightgreen", width=380, height=400)
    bot_frame.pack_propagate(False)
    bot_frame.pack()

    canvas = tk.Canvas(bot_frame, bg="lightgreen", width=380, height=400)
    scrollbar = ttk.Scrollbar(master=bot_frame, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = tk.Frame(canvas, bg="red")

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
    for i in range(10):
        tk.Frame(scrollable_frame, bg="lightblue", height=50, width=10).pack()
        tk.Label(scrollable_frame, text=f"Label {i}", bg="lightgreen").pack()

    window.mainloop()

if __name__ == "__main__":
    main()