import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import data_management as dm


class StudentProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Profile")
        self.root.geometry('400x600')

        self.bg_color = "white"
        self.students_database = dm.load_data("./database/students.json")
        
        self.main_student = dm.Student(self.students_database, 20230783)

        self.create_main_frames()

    def create_main_frames(self):
        self.create_frame2()

    def create_frame1(self):
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

    def create_frame2(self):
        frame2 = tk.Frame(self.root, bg="grey", width=390, height=590)
        frame2.pack_propagate(False)
        frame2.pack()

        header = tk.Frame(frame2, bg="lightblue", width=390, height=50)
        header.pack_propagate(False)
        header.pack()

        back_button = ttk.Button(header, width=3)
        back_button.pack(side="left", padx=10)

        delete_button = ttk.Button(header, width=3)
        delete_button.pack(side="right", padx=10)

        body1 = tk.Frame(frame2, bg="lightgreen", width=390, height=300)
        body1.pack_propagate(False)
        body1.pack()

        # Image PFP
        canvas = tk.Canvas(body1, width=175, height=175, bg="pink", highlightthickness=0)
        canvas.pack(pady=20)

        image = Image.open("./assets/image.jpg")
        image = image.resize((175, 175))
        photo = ImageTk.PhotoImage(image)

        canvas.create_image(87.5, 87.5, image=photo, anchor=tk.CENTER)
        canvas.image = photo  # Keep a reference to avoid garbage collection

        canvas.create_oval(-50, -50, 225, 225, outline="lightgreen", width=100)

        # Full Name
        full_name = tk.Label(body1, bg=self.bg_color, text="Neil Anthony Balbutin", font=("Helvetica", 16))
        full_name.pack()

        # ID Number
        id = tk.Label(body1, bg=self.bg_color, text="2023-0783", font=("Helvetica", 10))
        id.pack()

        # Border
        border = tk.Canvas(body1, width=340, height=10, bg=self.bg_color, highlightthickness=0)
        border.pack(side="bottom")

        border.create_line(0, 5, 340, 5, width=3)

        # BODY 2
        body2 = tk.Frame(frame2, width=390, height=250, bg="pink")
        body2.pack_propagate(False)
        body2.pack()

        tk.Frame(body2, bg=self.bg_color, height=40).pack()

        # Sex
        sex_frame = tk.Frame(body2, bg="lightblue", width=350, height=40)
        sex_frame.pack_propagate(False)
        sex_frame.pack()

        sex_label = tk.Label(sex_frame, text="Sex", font=("Helvetica", 10))
        sex_label.pack(side="left", padx=50)
        sex_value = tk.Label(sex_frame, text="M", font=("Helvetica", 10))
        sex_value.pack(side="right", padx=50)

        # Year Level
        year_frame = tk.Frame(body2, bg="lightblue", width=350, height=40)
        year_frame.pack_propagate(False)
        year_frame.pack()

        year_label = tk.Label(year_frame, text="Year Level")
        year_label.pack(side="left", padx=50)
        year_value = tk.Label(year_frame, text="2nd Year")
        year_value.pack(side="right", padx=50)

        # Program Code
        program_frame = tk.Frame(body2, bg="lightblue", width=350, height=40)
        program_frame.pack_propagate(False)
        program_frame.pack()

        program_label = tk.Label(program_frame, text="Program Code")
        program_label.pack(side="left", padx=50)
        program_value = tk.Label(program_frame, text="BSCS")
        program_value.pack(side="right", padx=50)


        

def main():
    root = tk.Tk()
    app = StudentProfileApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()