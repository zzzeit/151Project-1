import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from data_management import *

import main

class MiniProfile:
    def __init__(self, app, master, student):
        frame = tk.Frame(master, bg=app.getColor(2), width=620, height=30)
        frame.pack_propagate(False)
        frame.pack(pady=5, padx=(10, 0))
        frame.bind("<Button-1>", lambda event: [ app.setMainStud(student), app.transition_frames(app.frame2_obj)])

        x = [3, 6,]
        for i in range(0, 7):
            t = student[i]
            if i == ID:
                t = text=str(student[ID])[:4] + "-" + str(student[ID])[4:8]
            l = tk.Label(frame, text=t, bg=app.getColor(2), width=11)
            l.pack_propagate(False)
            l.pack(padx=(3, 0), side="left")
            l.bind("<Button-1>", lambda event: [ app.setMainStud(student), app.transition_frames(app.frame2_obj)])

class Frame1:
    def __init__(self, app):
        self.app = app
        self.entry_str_var = tk.StringVar()
        self.entry_str_var.trace_add(mode="write", callback=self.on_entry_updated)
        self.acquired_student_profiles = app.getStudentDb()
        self.create_widgets(app)

    def create_widgets(self, app):
        self.frame1 = tk.Frame(app.getRoot(), width=682.5, height=590, bg=self.app.getColor(0))
        self.frame1.pack_propagate(False)

        self.top_frame = tk.Frame(master=self.frame1, width=665, height=50, bg=app.getColor(0))
        self.top_frame.pack_propagate(False)
        self.top_frame_container = tk.Frame(self.top_frame, bg=app.getColor(0))
        self.search_entry = ttk.Entry(master=self.top_frame_container, width=30, font=("Helvetica", 15), textvariable=self.entry_str_var)
        self.top_frame_container.pack()
        self.top_frame.pack(pady=(20,0))

        self.top_row_frame = tk.Frame(master=self.frame1, width=665 , height=25, bg=app.getColor(2))
        self.top_row_frame.pack_propagate(False)
        self.top_row_frame.pack(pady=(10, 15))

        self.labels_frame = tk.Frame(master=self.top_row_frame, bg=app.getColor(2))
        self.labels_frame.pack(padx=(0, 10), side="left")
        labels = {"First N":35, "Last N":47, "Sex":55, "ID#":66, "Year Level":43, "College":35, "Code":45}
        for i in list(labels.keys()):
            self.label_ = tk.Label(master=self.labels_frame, bg=app.getColor(2), text=i)
            self.label_.pack(side="left", padx=(labels[i],0))

        self.bot_frame = tk.Frame(master=self.frame1, width=665, height=600, bg="pink")
        self.bot_frame.pack_propagate(False)
        self.bot_frame.pack(pady=(3,0))

        self.canvas1 = tk.Canvas(self.bot_frame, width=680, height=400, bg=app.getColor(1))
        self.scrollbar = ttk.Scrollbar(master=self.bot_frame, orient='vertical', command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas1, bg=app.getColor(1))
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas1.configure(
                scrollregion=self.canvas1.bbox("all")
            )
        )
        self.canvas1.configure(bg=app.getColor(1))
        self.canvas1.create_window((0, 0), window=self.scrollable_frame, anchor="n", width=620)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas1.pack(side="left", fill="both", expand=True)

        self.canvas1.bind_all("<MouseWheel>", lambda event: self.canvas1.yview_scroll(int(-1*(event.delta/120)), "units"))

        self.add_student_button = ttk.Button(self.top_frame_container, width=5, text="Add", command=lambda: app.transition_frames(app.frame3_obj))
        self.settings_button = ttk.Button(self.top_frame_container, text="Settings", command=lambda: app.transition_frames(app.frame4_obj))
        self.add_student_button.pack(side="left")
        self.search_entry.pack(side="left", padx=100)
        self.settings_button.pack(side="left")


    def on_entry_updated(self, *args):
        for widget in self.scrollable_frame.winfo_children():
            widget.pack_forget()

        SEARCH_TYPE = self.app.getSearchSet()
        temp = []
        for student in self.acquired_student_profiles:
            match = True
            for i, letter in enumerate(self.entry_str_var.get()):
                if i >= len(student[SEARCH_TYPE]) or letter.upper() != student[SEARCH_TYPE][i].upper():
                    match = False
                    break
            if match:
                temp.append(student)

   
        for student in temp:
            MiniProfile(self.app, self.scrollable_frame, student)

        if not self.entry_str_var.get():
            for widget in self.scrollable_frame.winfo_children():
                widget.pack_forget()
            # self.scrollbar.pack_forget()
            # self.canvas1.pack_forget()
            self.acquired_student_profiles = self.app.getStudentDb()
            self.show_list()



    def show_list(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.pack_forget()
        for student in self.acquired_student_profiles:
            MiniProfile(self.app, self.scrollable_frame, student)

    def transition(self):
        self.frame1.pack()
        self.acquired_student_profiles = self.app.getStudentDb()
        self.show_list()

    def getMainFrame(self):
        return self.frame1

class Frame2:
    def __init__(self, app):
        self.app = app
        self.frame2 = tk.Frame(app.getRoot(), width=682.5, height=590, bg=app.getColor(0))
        self.frame2.pack_propagate(False)
        # self.frame2.pack()

        self.header = tk.Frame(self.frame2, width=682.5, height=50, bg=app.getColor(0))
        self.header.pack_propagate(False)
        self.header.pack()

        self.back_button = ttk.Button(self.header, text="Back", width=5, command=lambda: app.transition_frames(app.frame1_obj))
        self.back_button.pack(side="left", padx=10)

        self.delete_button = ttk.Button(self.header, text="Delete", width=6, command=lambda: [app.delete_student(app.getMainStud()[ID]), app.transition_frames(app.frame1_obj)])
        self.delete_button.pack(side="right", padx=10)

        self.body1 = tk.Frame(self.frame2, width=682.5, height=300, bg=app.getColor(0))
        self.body1.pack_propagate(False)
        self.body1.pack()

        # Image PFP
        self.canvas2 = tk.Canvas(self.body1, width=175, height=175, highlightthickness=0)
        self.canvas2.pack(pady=20)

        image = Image.open("./assets/image.jpg")
        image = image.resize((175, 175))
        photo = ImageTk.PhotoImage(image)

        self.canvas2.create_image(87.5, 87.5, image=photo, anchor=tk.CENTER)
        self.canvas2.image = photo  # Keep a reference to avoid garbage collection

        self.canvas2.create_oval(-50, -50, 225, 225, outline=app.getColor(0), width=100)

        self.nameFrame = tk.Frame(self.body1, bg=app.getColor(0))
        self.nameFrame.pack()
        # Full Name
        self.full_name_var = tk.StringVar(value="Empty")
        self.full_name = tk.Label(self.nameFrame, textvariable=self.full_name_var, font=("Helvetica", 16), bg=app.getColor(0), foreground="white")
        self.full_name.pack()

        # ID Number
        self.id_var = tk.StringVar(value="0000-0000")
        self.id = tk.Label(self.nameFrame, textvariable=self.id_var, font=("Helvetica", 10), bg=app.getColor(0), foreground="white")
        self.id.pack()

        # Border
        self.border = tk.Canvas(self.body1, width=340, height=10, highlightthickness=0, bg=app.getColor(0))
        self.border.pack(side="bottom")

        self.border.create_line(0, 5, 340, 5, width=3, fill=app.getColor(3))

        # BODY 2
        self.body2 = tk.Frame(self.frame2, width=682.5, height=250, bg=app.getColor(0))
        self.body2.pack_propagate(False)
        self.body2.pack()

        # Sex
        self.sex_frame = tk.Frame(self.body2, width=350, height=40, bg=app.getColor(2))
        self.sex_frame.pack_propagate(False)
        self.sex_frame.pack(pady=(40, 0))

        self.sex_label = tk.Label(self.sex_frame, text="Sex", font=("Helvetica", 10), bg=app.getColor(2))
        self.sex_label.pack(side="left", padx=50)
        self.sex_value_var = tk.StringVar(value="")
        self.sex_value = tk.Label(self.sex_frame, textvariable=self.sex_value_var, font=("Helvetica", 10), bg=app.getColor(2))
        self.sex_value.pack(side="right", padx=50)

        # Year Level
        self.year_frame = tk.Frame(self.body2, width=350, height=40, bg=app.getColor(2))
        self.year_frame.pack_propagate(False)
        self.year_frame.pack()

        self.year_label = tk.Label(self.year_frame, text="Year Level", bg=app.getColor(2))
        self.year_label.pack(side="left", padx=50)
        self.year_value_var = tk.StringVar(value="")
        self.year_value = tk.Label(self.year_frame, textvariable=self.year_value_var, bg=app.getColor(2))
        self.year_value.pack(side="right", padx=50)

        # Program Code
        self.program_frame = tk.Frame(self.body2, width=350, height=40, bg=app.getColor(2))
        self.program_frame.pack_propagate(False)
        self.program_frame.pack()

        self.program_label = tk.Label(self.program_frame, text="Program Code", bg=app.getColor(2))
        self.program_label.pack(side="left", padx=(50,0))
        self.program_value_var = tk.StringVar(value="")
        self.program_value = tk.Label(self.program_frame, textvariable=self.program_value_var, bg=app.getColor(2))
        self.program_value.pack(side="right", padx=(0,50))

    def update_stud_info_values(self):
        self.full_name_var.set(self.app.getMainStud()[FNAME] + " " + self.app.getMainStud()[LNAME])
        self.id_var.set(str(self.app.getMainStud()[ID])[:4] + "-" + str(self.app.getMainStud()[ID])[4:8])
        self.sex_value_var.set(self.app.getMainStud()[SEX])
        self.year_value_var.set(self.app.getMainStud()[YRLVL] + " Year")
        self.program_value_var.set(self.app.getMainStud()[PCODE] + " ({})".format(self.app.getMainStud()[CCODE]))


    def transition(self):
        self.update_stud_info_values()
        self.frame2.pack()

    def getMainFrame(self):
        return self.frame2
    
class Frame3:
    def __init__(self, app):
        colorNum = app.getColor(2)
        self.app = app
        self.frame3 = tk.Frame(app.getRoot(), width=682.5, height=590, bg=app.getColor(0))
        self.frame3.pack_propagate(False)

        self.header = tk.Frame(self.frame3, width=682.5, height=50, bg=app.getColor(0))
        self.header.pack_propagate(False)
        self.header.pack()

        style = ttk.Style()
        style.configure('TButton', background=app.getColor(0), foreground=app.getColor(0))
        self.back_button = ttk.Button(self.header, text="Back", width=5, command=lambda: [self.clear_entries, app.transition_frames(app.frame1_obj)], style='TButton')
        self.back_button.pack(side="left", padx=10)

        self.body1 = tk.Frame(self.frame3, width=682.5, height=540, bg=app.getColor(0))
        self.body1.pack_propagate(False)
        self.body1.pack()

        # Image PFP
        self.canvas2 = tk.Canvas(self.body1, width=175, height=175, highlightthickness=0)
        self.canvas2.pack(pady=20)

        image = Image.open("./assets/image.jpg")
        image = image.resize((175, 175))
        photo = ImageTk.PhotoImage(image)

        self.canvas2.create_image(87.5, 87.5, image=photo, anchor=tk.CENTER)
        self.canvas2.image = photo  # Keep a reference to avoid garbage collection

        self.canvas2.create_oval(-50, -50, 225, 225, outline=app.getColor(0), width=100)

        # Frame for Entries
        self.entry_frame_height = 40
        self.entry_frame = tk.Frame(self.body1, width=290, height=200, bg=app.getColor(0))
        self.entry_frame.pack()

        # First Name
        self.first_name_frame = tk.Frame(self.entry_frame, width=290, height=self.entry_frame_height, bg=colorNum)
        self.first_name_frame.pack_propagate(False)
        self.first_name_frame.pack()

        self.first_name_label = tk.Label(self.first_name_frame, text="First Name:", font=("Helvetica", 13), bg=colorNum)
        self.first_name_label.pack(side="left", padx=(20, 0))

        self.first_name_entry = ttk.Entry(self.first_name_frame)
        self.first_name_entry.pack(side="right", padx=(0, 20))

        # Last Name
        self.last_name_frame = tk.Frame(self.entry_frame, width=290, height=self.entry_frame_height, bg=colorNum)
        self.last_name_frame.pack_propagate(False)
        self.last_name_frame.pack()

        self.last_name_label = tk.Label(self.last_name_frame, text="Last Name:", font=("Helvetica", 13), bg=colorNum)
        self.last_name_label.pack(side="left", padx=(20, 0))

        self.last_name_entry = ttk.Entry(self.last_name_frame)
        self.last_name_entry.pack(side="right", padx=(0, 20))

        # ID Number
        self.id_num_frame = tk.Frame(self.entry_frame, width=290, height=self.entry_frame_height, bg=colorNum)
        self.id_num_frame.pack_propagate(False)
        self.id_num_frame.pack()

        self.id_num_label = tk.Label(self.id_num_frame, text="ID Number:", font=("Helvetica", 13), bg=colorNum)
        self.id_num_label.pack(side="left", padx=(20, 0))

        self.id_num_entry = ttk.Entry(self.id_num_frame)
        self.id_num_entry.pack(side="right", padx=(0, 20))

        # Sex
        self.sex_frame = tk.Frame(self.entry_frame, width=290, height=self.entry_frame_height, bg=colorNum)
        self.sex_frame.pack_propagate(False)
        self.sex_frame.pack()

        self.sex_label = tk.Label(self.sex_frame, text="Sex:", font=("Helvetica", 13), bg=colorNum)
        self.sex_label.pack(side="left", padx=(20, 0))

        values = ["Male", "Female"]
        self.sex_cb = ttk.Combobox(self.sex_frame, values=values, state='readonly', width=17)
        self.sex_cb.pack(side="right", padx=(0, 20))

        # Year Level
        self.year_level_frame = tk.Frame(self.entry_frame, width=290, height=self.entry_frame_height, bg=colorNum)
        self.year_level_frame.pack_propagate(False)
        self.year_level_frame.pack()

        self.year_level_label = tk.Label(self.year_level_frame, text="Year Level:", font=("Helvetica", 13), bg=colorNum)
        self.year_level_label.pack(side="left", padx=(20, 0))

        values = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        self.year_level_cb = ttk.Combobox(self.year_level_frame, values=values, state='readonly', width=17)
        self.year_level_cb.pack(side="right", padx=(0, 20))

        # College Code
        self.college_code_frame = tk.Frame(self.entry_frame, width=290, height=self.entry_frame_height, bg=colorNum)
        self.college_code_frame.pack_propagate(False)
        self.college_code_frame.pack()

        self.college_code_label = tk.Label(self.college_code_frame, text="College:", font=("Helvetica", 13), bg=colorNum)
        self.college_code_label.pack(side="left", padx=(20, 0))

        collegeData = load_data("./database/colleges.csv")
        collegeValues = []
        for i in collegeData:
            if i[0] not in collegeValues:
                collegeValues.append(i[0])
        self.college_code_cb = ttk.Combobox(self.college_code_frame, values=collegeValues, state='readonly', width=17)
        self.college_code_cb.pack(side="right", padx=(0, 20))



        # Program Code
        self.program_code_frame = tk.Frame(self.entry_frame, width=290, height=self.entry_frame_height, bg=colorNum)
        self.program_code_frame.pack_propagate(False)
        self.program_code_frame.pack()

        self.program_code_label = tk.Label(self.program_code_frame, text="Program:", font=("Helvetica", 13), bg=colorNum)
        self.program_code_label.pack(side="left", padx=(20, 0))

        programValues = []
        self.program_code_cb = ttk.Combobox(self.program_code_frame, values=programValues, state='readonly', width=17)
        self.program_code_cb.pack(side="right", padx=(0, 20))   

        self.college_code_cb.bind("<<ComboboxSelected>>", self.update_program_values)


        # Submit
        self.entries = None
        self.submit_button = ttk.Button(self.body1, text="Submit", command=self.submit_func)
        self.submit_button.pack(pady=(10, 0))
    
    def update_program_values(self, event):
        self.program_code_cb.set('')
        college = self.college_code_cb.get()
        programValues = []
        collegeData = load_data("./database/colleges.csv")
        for i in collegeData:
            if (college == i[0]):
                programValues.append(i[1])
        self.program_code_cb['values'] = programValues

    def submit_func(self):
        self.entries = [self.first_name_entry, self.last_name_entry, self.sex_cb, self.id_num_entry, 
                   self.year_level_cb, self.college_code_cb, self.program_code_cb]
        values = []
        for e in self.entries:
            if not e.get():
                self.alert_message("Input Error", "All fields must be filled out.")
                return
            values.append(e.get())
        values[FNAME] = values[FNAME].capitalize()
        values[LNAME] = values[LNAME].capitalize()
        # Name Error
        for c in values[FNAME].replace(" ", ""):
            if not c.isalpha():
                self.alert_message("Input Error", "First Name must not contain digits or any symbols.")
                return
        for c in values[LNAME].replace(" ", ""):
            if not c.isalpha():
                self.alert_message("Input Error", "Last Name must not contain digits or any symbols.")
                return

        # ID Number error
        if "-" in values[ID]:
            values[ID] = values[ID].replace("-", "")

        for c in values[ID]:
            if c.isalpha():
                self.alert_message("Input Error", "ID Number must only contain digits or '-'.")
                return
        
        if len(values[ID]) != 8:
            self.alert_message("Input Error", "ID Numbers must be 8 digits.")
            return

        if self.app.get_student(values[ID]) != None:
            self.alert_message("Input Error", "Student with {} ID already exists.".format(values[3]))
            return
        
        values[YRLVL] = values[YRLVL][:3]
        studdb = self.app.getStudentDb()
        studdb.append(values)
        write_data("./database/students.csv", studdb)
        self.clear_entries()

    def alert_message(self, title, text):
        tk.messagebox.showerror(title, text)


    def clear_entries(self):
        for e in self.entries:
            if isinstance(e, ttk.Entry):
                e.delete(0, tk.END)

        self.sex_cb.set('')
        self.year_level_cb.set('')
        self.program_code_cb.set('')
        self.college_code_cb.set('')
        self.app.transition_frames(self.app.frame1_obj)

    def transition(self):
        self.frame3.pack()

class Frame4:
    def __init__(self, app):
        self.app = app

        self.frame4 = tk.Frame(app.getRoot(), bg=app.getColor(0))
        self.frame4.pack()

        # Search By
        self.search_frame = tk.Frame(self.frame4, width=150, height=20)
        self.search_frame.pack_propagate(False)
        self.search_frame.pack(pady=(10,0))

        self.search_label = tk.Label(self.search_frame, text="Search By: ")
        self.search_label.pack(side="left")

        self.searchValues = {"First Name" : 0, "Last Name" : 1, "ID#" : 3, "Year Level" : 4}
        self.search_cb = ttk.Combobox(self.search_frame, state='readonly', values=list(self.searchValues.keys()), width=8)
        self.search_cb.pack(side="right")
        self.search_cb.set("First Name")

        # Sort By
        self.sort_frame = tk.Frame(self.frame4, width=150, height=20)
        self.sort_frame.pack_propagate(False)
        self.sort_frame.pack(pady=(10,0))

        self.sort_label = tk.Label(self.sort_frame, text="Order: ")
        self.sort_label.pack(side="left")

        self.sortValues = {"Ascending" : True, "Descending" : False}
        self.sort_cb = ttk.Combobox(self.sort_frame, state='readonly', values=list(self.sortValues.keys()), width=8)
        self.sort_cb.pack(side="right")
        self.sort_cb.set("Ascending")

        # Done
        self.done_button = ttk.Button(self.frame4, text="DONE", command=self.done_button)
        self.done_button.pack(pady=10)
    
    def done_button(self):
        self.app.setSearchSet(self.searchValues[self.search_cb.get()])
        self.app.sort_students(self.searchValues[self.search_cb.get()], self.sortValues[self.sort_cb.get()])
        self.app.transition_frames(self.app.frame1_obj)

    def transition(self):
        self.frame4.pack()