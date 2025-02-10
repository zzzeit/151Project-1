import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import main

class MiniProfile:
    def __init__(self, app, master, student):
        frame = tk.Frame(master, width=330, height=80)
        frame.pack_propagate(False)
        frame.pack(pady=5)
        frame.bind("<Button-1>", lambda event: [ app.setMainStud(student), app.transition_frames(2)])

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
        self.id = tk.Label(student_info, text=str(student["ID#"])[:4] + "-" + str(student["ID#"])[4:8])
        self.id.pack(side="left")

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

        self.canvas1 = tk.Canvas(self.bot_frame, bg="pink", width=380, height=400)
        self.scrollbar = ttk.Scrollbar(master=self.bot_frame, orient='vertical', command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas1, bg="lightblue")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas1.configure(
                scrollregion=self.canvas1.bbox("all")
            )
        )

        self.canvas1.create_window((0, 0), window=self.scrollable_frame, anchor="n", width=360)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas1.pack(side="left", fill="both", expand=True)

        
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
            MiniProfile(self.app, self.scrollable_frame, student)

        if not self.entry_str_var.get():
            for widget in self.scrollable_frame.winfo_children():
                widget.pack_forget()
            self.acquired_student_profiles = self.app.getStudentDb()

    def transition(self):
        self.frame1.pack()

    def getMainFrame(self):
        return self.frame1




class Frame2:
    def __init__(self, app):
        self.app = app
        self.frame2 = tk.Frame(app.getRoot(), bg="grey", width=390, height=590)
        self.frame2.pack_propagate(False)
        # self.frame2.pack()

        self.header = tk.Frame(self.frame2, bg="lightblue", width=390, height=50)
        self.header.pack_propagate(False)
        self.header.pack()

        self.back_button = ttk.Button(self.header, width=3, command=lambda: app.transition_frames(1))
        self.back_button.pack(side="left", padx=10)

        self.delete_button = ttk.Button(self.header, width=3)
        self.delete_button.pack(side="right", padx=10)

        self.body1 = tk.Frame(self.frame2, bg="lightgreen", width=390, height=300)
        self.body1.pack_propagate(False)
        self.body1.pack()

        # Image PFP
        self.canvas2 = tk.Canvas(self.body1, width=175, height=175, bg="pink", highlightthickness=0)
        self.canvas2.pack(pady=20)

        image = Image.open("./assets/image.jpg")
        image = image.resize((175, 175))
        photo = ImageTk.PhotoImage(image)

        self.canvas2.create_image(87.5, 87.5, image=photo, anchor=tk.CENTER)
        self.canvas2.image = photo  # Keep a reference to avoid garbage collection

        self.canvas2.create_oval(-50, -50, 225, 225, outline="lightgreen", width=100)

        # Full Name
        self.full_name_var = tk.StringVar(value="Empty")
        self.full_name = tk.Label(self.body1, bg=app.getBg(), textvariable=self.full_name_var, font=("Helvetica", 16))
        self.full_name.pack()

        # ID Number
        self.id_var = tk.StringVar(value="0000-0000")
        self.id = tk.Label(self.body1, bg=app.getBg(), textvariable=self.id_var, font=("Helvetica", 10))
        self.id.pack()

        # Border
        self.border = tk.Canvas(self.body1, width=340, height=10, bg=app.getBg(), highlightthickness=0)
        self.border.pack(side="bottom")

        self.border.create_line(0, 5, 340, 5, width=3)

        # BODY 2
        self.body2 = tk.Frame(self.frame2, width=390, height=250, bg="pink")
        self.body2.pack_propagate(False)
        self.body2.pack()

        # Sex
        self.sex_frame = tk.Frame(self.body2, bg="lightblue", width=350, height=40)
        self.sex_frame.pack_propagate(False)
        self.sex_frame.pack(pady=(40, 0))

        self.sex_label = tk.Label(self.sex_frame, text="Sex", font=("Helvetica", 10))
        self.sex_label.pack(side="left", padx=50)
        self.sex_value_var = tk.StringVar(value="")
        self.sex_value = tk.Label(self.sex_frame, textvariable=self.sex_value_var, font=("Helvetica", 10))
        self.sex_value.pack(side="right", padx=50)

        # Year Level
        self.year_frame = tk.Frame(self.body2, bg="lightblue", width=350, height=40)
        self.year_frame.pack_propagate(False)
        self.year_frame.pack()

        self.year_label = tk.Label(self.year_frame, text="Year Level")
        self.year_label.pack(side="left", padx=50)
        self.year_value_var = tk.StringVar(value="")
        self.year_value = tk.Label(self.year_frame, textvariable=self.year_value_var)
        self.year_value.pack(side="right", padx=50)

        # Program Code
        self.program_frame = tk.Frame(self.body2, bg="lightblue", width=350, height=40)
        self.program_frame.pack_propagate(False)
        self.program_frame.pack()

        self.program_label = tk.Label(self.program_frame, text="Program Code")
        self.program_label.pack(side="left", padx=50)
        self.program_value_var = tk.StringVar(value="")
        self.program_value = tk.Label(self.program_frame, textvariable=self.program_value_var)
        self.program_value.pack(side="right", padx=50)

    def update_stud_info_values(self):
        self.full_name_var.set(self.app.getMainStud()['fname'] + " " + self.app.getMainStud()['lname'])
        self.id_var.set(str(self.app.getMainStud()['ID#'])[:4] + "-" + str(self.app.getMainStud()['ID#'])[4:8])
        self.sex_value_var.set(self.app.getMainStud()['sex'])
        self.year_value_var.set(self.app.getMainStud()['year lvl'] + " Year")
        self.program_value_var.set(self.app.getMainStud()['program code'])


    def transition(self):
        self.update_stud_info_values()
        self.frame2.pack()

    def getMainFrame(self):
        return self.frame2