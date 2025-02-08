import tkinter as tk

import data_management as dm
import widgets as ws


class StudentProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Profile")
        self.root.geometry('400x600')
        self.root.resizable(False, False)

        self.bg_color = "white"
        self.students_database = dm.load_data("./database/students.json")
        
        self.main_student =     {
        "fname": "None",
        "lname": "None",
        "gender": "None",
        "ID#": 00000000,
        "program code": "None"
    }

        self.create_main_frames()

    def create_main_frames(self):
        self.frame1_obj = ws.Frame1(self)
        self.frame2_obj = ws.Frame2(self)

        self.transition_frames(2)

    def transition_frames(self, i):
        if i == 1:
            for frame in self.root.winfo_children():
                frame.pack_forget()
            self.frame1_obj.transition()

        if i == 2:
            for frame in self.root.winfo_children():
                frame.pack_forget()
            self.frame2_obj.transition()


    # Getter methods
    def getRoot(self):
        return self.root
    
    def getBg(self):
        return self.bg_color
    
    def getStudentDb(self):
        return self.students_database
    
    def getMainStud(self):
        return self.main_student

    def setMainStud(self, student):
        self.main_student = student

        

def main():
    root = tk.Tk()
    app = StudentProfileApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()