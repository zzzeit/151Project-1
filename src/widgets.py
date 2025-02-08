import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import main

class MiniProfile:
    def __init__(self, master, student):
        frame = tk.Frame(master, width=330, height=80)
        frame.pack_propagate(False)
        frame.pack(pady=5)

        canvas = tk.Canvas(frame, bg="lime", width=50, height=50)
        canvas.pack(side="left", padx=(40, 0))
        image = Image.open("./assets/image.jpg")
        image = image.resize((53, 53))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        canvas.image = photo

        student_info = tk.Frame(frame)
        student_info.pack(side="left", padx=40)

        nameframe = tk.Frame(student_info)
        nameframe.pack()
        name = tk.Label(nameframe, text=student["fname"] + " " + student["lname"], font=("Helvetica", 12))
        name.pack(side="left")

        idframe = tk.Frame(student_info)
        idframe.pack()
        id = tk.Label(student_info, text=str(student["ID#"])[:4] + "-" + str(student["ID#"])[4:8])
        id.pack(side="left")

class Frame1:
    def __init__(self, app):
        self.app = app
        self.entry_str_var = tk.StringVar()
        self.entry_str_var.trace_add(mode="write", callback=self.on_entry_updated)
        self.create_widgets(app)

        self.acquired_student_profiles = app.getStudentDb()

    def create_widgets(self, app):
        self.frame1 = tk.Frame(app.getRoot(), bg="grey", width=390, height=590)
        self.frame1.pack_propagate(False)
        # self.frame1.pack()

        self.top_frame = tk.Frame(master=self.frame1, bg="lightgreen", width=380, height=50)
        self.top_frame.pack_propagate(False)
        self.search_entry = ttk.Entry(master=self.top_frame, font=("Helvetica", 15), textvariable=self.entry_str_var)
        self.search_entry.pack(pady=5)
        self.top_frame.pack(pady=20)

        self.bot_frame = tk.Frame(master=self.frame1, bg="lightgreen", width=380, height=600)
        self.bot_frame.pack_propagate(False)
        self.bot_frame.pack()

        self.canvas = tk.Canvas(self.bot_frame, bg="pink", width=380, height=400)
        self.scrollbar = ttk.Scrollbar(master=self.bot_frame, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas, bg="lightblue")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n", width=360)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        
        # for i in range(14):
        #     MiniProfile(self.scrollable_frame)
            # tk.Label(self.scrollable_frame, text=f"Label {i}", bg="lightblue").pack()
    
    def on_entry_updated(self, *args):
        for widget in self.scrollable_frame.winfo_children():
            widget.pack_forget()

        temp = []
        for student in self.acquired_student_profiles:
            match = True
            for i, letter in enumerate(self.entry_str_var.get()):
                if i >= len(student["fname"]) or letter.upper() != student["fname"][i].upper():
                    match = False
                    break
            if match:
                temp.append(student)

   
        for student in temp:
            MiniProfile(self.scrollable_frame, student)

        if not self.entry_str_var.get():
            for widget in self.scrollable_frame.winfo_children():
                widget.pack_forget()
            self.acquired_student_profiles = self.app.getStudentDb()

    def getMainFrame(self):
        return self.frame1




class Frame2:
    def __init__(self, app):
        self.frame2 = tk.Frame(app.getRoot(), bg="grey", width=390, height=590)
        self.frame2.pack_propagate(False)
        # self.frame2.pack()

        header = tk.Frame(self.frame2, bg="lightblue", width=390, height=50)
        header.pack_propagate(False)
        header.pack()

        back_button = ttk.Button(header, width=3, command=app.transition_frames(1))
        back_button.pack(side="left", padx=10)

        delete_button = ttk.Button(header, width=3)
        delete_button.pack(side="right", padx=10)

        body1 = tk.Frame(self.frame2, bg="lightgreen", width=390, height=300)
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
        full_name = tk.Label(body1, bg=app.getBg(), text="Neil Anthony Balbutin", font=("Helvetica", 16))
        full_name.pack()

        # ID Number
        id = tk.Label(body1, bg=app.getBg(), text="2023-0783", font=("Helvetica", 10))
        id.pack()

        # Border
        border = tk.Canvas(body1, width=340, height=10, bg=app.getBg(), highlightthickness=0)
        border.pack(side="bottom")

        border.create_line(0, 5, 340, 5, width=3)

        # BODY 2
        body2 = tk.Frame(self.frame2, width=390, height=250, bg="pink")
        body2.pack_propagate(False)
        body2.pack()

        tk.Frame(body2, bg=app.getBg(), height=40).pack()

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

    def getMainFrame(self):
        return self.frame2