import tkinter as tk
from tkinter import ttk
import data_management as dm
from data_management import Student as s


def main():
    # mydata = dm.load_data("database/students.json")
    # ms = dm.Student("Dustin", "Aamian", "Male", 20230456, "BSCS")
    # mydata.append(ms.student_data)
    # dm.write_data("database/students.json", sorted(mydata, key=lambda x: x['lname']))

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

    scrollbar = ttk.Scrollbar(master=bot_frame,orient='vertical')
    scrollbar.pack(side="right")

    bot_frame.pack()
    # Start the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()